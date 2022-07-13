import torch
import torch.nn as nn


class WideAndDeep(nn.Module):
    def __init__(self,
                 cat_features,
                 emb_dims, encode_dim,
                 deep_fea_nums,
                 wide_fea_nums):
        """wide and deep model

        Args:
            cat_features (dict): the number of each categorical feature
            emb_dims (list): the list of layer dims
            encode_dim (int): encoded embedding dim
            deep_fea_nums (int): the number of deep features
            wide_fea_nums (int): the number of wide features
        """
        super(WideAndDeep, self).__init__()
        self.cat_features = cat_features
        self.emb_dims = emb_dims
        self.encode_dim = encode_dim
        self.deep_fea_nums = deep_fea_nums
        self.wide_fea_nums = wide_fea_nums
        self.embs = nn.ModuleDict()
        # 存储不同的embedding层
        for fea_name in self.cat_features.keys():
            fea_nums = self.cat_features[fea_name]
            emb = nn.Embedding(fea_nums, self.encode_dim)
            self.embs[fea_name] = emb
        self.dlayers = self.deep_layer()
        self.wlayer = self.wide_layer()
        self.softmax = nn.Softmax(dim=1)


    def encoder(self, features):
        # 对不同特征进行编码
        emb_dict = {}
        for fea_name in features.keys():
            if fea_name in self.embs.keys():
                emb_dict[fea_name] = self.embs[fea_name](features[fea_name])
            elif 'cat_his' in fea_name:
                
                emb_tmp = self.embs['cat'](features[fea_name])
                emb_tmp = torch.mean(emb_tmp, 1)
                emb_dict[fea_name] = emb_tmp
                
            elif 'mid_his' in fea_name:
                emb_tmp = self.embs['mid'](features[fea_name])
                emb_tmp = torch.mean(emb_tmp, 1)
                emb_dict[fea_name] = emb_tmp
        return emb_dict

    def deep_layer(self):
        # 得到deep层
        input_dim = self.deep_fea_nums * self.encode_dim
        dlayers = nn.ModuleList([nn.BatchNorm1d(input_dim), nn.Linear(input_dim, self.emb_dims[0]), nn.PReLU()])
        for i in range(1, len(self.emb_dims)):
            linear = nn.Linear(self.emb_dims[i - 1], self.emb_dims[i])
            dlayers.append(linear)
            dlayers.append(nn.PReLU())
        return dlayers

    def wide_layer(self):
        # 得到wide层
        input_dim = self.wide_fea_nums * self.encode_dim
        linear = nn.Linear(input_dim, self.emb_dims[-1])
        return linear

    def forward(self, features):
        # 得到不同特征的embedding
        emb_dict = self.encoder(features)
        # 构建deep部分的输入
        deep_emb = torch.cat(list(emb_dict.values()), 1)
        # 构建wide部分的输入
        item_emb = torch.cat([emb_dict['mid'], emb_dict['cat']], 1)
        item_his_emb = torch.cat([emb_dict['mid_his'], emb_dict['cat_his']], 1)
        wide_emb = torch.cat([item_emb, item_his_emb, item_emb * item_his_emb], 1)
        # wide部分直接经过简单的一层layer
        y_wide = self.wlayer(wide_emb)
        # deep部分通过DNN进行特征交互
        demb = deep_emb
        for i in range(len(self.dlayers)-1):
            demb = self.dlayers[i](demb)
        y_deep = demb
        final_embd = y_deep + y_wide
        output = self.softmax(final_embd)
        return output
