## PyG

### Basics

**Data**
- torch_geometric.data：data类用于构建图数据对象。
  - 节点的属性/特征
  - 邻接/边连接信息
```
// x, y 可以用FloatTensor来表示：
x = torch.tensor([[2,1],[5,6],[3,7],[12,0]], dtype=torch.float) 
y = torch.tensor([0,1,0,1], dtype=torch.float)
```
图的节点连接信息要以COO格式进行存储。在COO格式中，COO list 是一个2*E 维的list。第一个维度的节点是源节点(source nodes)，第二个维度中是目标节点(target nodes)，连接方式是由源节点指向目标节点。对于无向图来说，存贮的source nodes 和 target node 是成对存在的。
```
​edge_index = torch.tensor([[0,1,2,0,3],
                          [1,0,1,3,2]],dtype=torch,long)
```
边索引的顺序跟Data对象无关，或者说边的存储顺序并不重要，因为这个edge_index只是用来计算邻接矩阵(Adjacency Matrix)。
```
import torch

from torch_geometric.data import Data

x = torch.tensor([[2,1],[5,6],[3,7],[12,0]],dtype=torch.float)

y = torch.tensor([[0,2,1,0,3],[3,1,0,1,2]],dtype=torch.long)

​edge_index = torch.tensor([[0,1,2,0,3],
                          [1,0,1,3,2]],dtype=torch,long)

data = Data(x=x,y=y,edge_index=edge_index)
```

**Dataset**

PyG提供两种不同的数据集类：

- InMemoryDataset
- Dataset

```
import torch
from torch_geometric.data import InMemoryDataset


class MyOwnDataset(InMemoryDataset):
    def __init__(self, root, transform=None, pre_transform=None):
        super(MyOwnDataset, self).__init__(root, transform, pre_transform)
        self.data, self.slices = torch.load(self.processed_paths[0])

    @property
    def raw_file_names(self):
        return ['some_file_1', 'some_file_2', ...]

    @property
    def processed_file_names(self):
        return ['data.pt']

    def download(self):
        # Download to `self.raw_dir`.

    def process(self):
        # Read data into huge `Data` list.
        data_list = [...]

        if self.pre_filter is not None:
            data_list [data for data in data_list if self.pre_filter(data)]

        if self.pre_transform is not None:
            data_list = [self.pre_transform(data) for data in data_list]

        data, slices = self.collate(data_list)
        torch.save((data, slices), self.processed_paths[0])
```

**DataLoader**

**MessagePassing**

需要定义三个方法：

- message
- update
- aggregation scheme

**GCN Example**

```
import torch
from torch_geometric.nn import MessagePassing
from torch_geometric.utils import add_self_loops, degree

class GCNConv(MessagePassing):
    def __init__(self, in_channels, out_channels):
        super(GCNConv, self).__init__(aggr='add')  # "Add" aggregation.
        self.lin = torch.nn.Linear(in_channels, out_channels)

    def forward(self, x, edge_index):
        # x has shape [N, in_channels]
        # edge_index has shape [2, E]

        # Step 1: Add self-loops to the adjacency matrix.
        edge_index, _ = add_self_loops(edge_index, num_nodes=x.size(0))

        # Step 2: Linearly transform node feature matrix.
        x = self.lin(x)

        # Step 3-5: Start propagating messages.
        return self.propagate(edge_index, size=(x.size(0), x.size(0)), x=x)

    def message(self, x_j, edge_index, size):
        # x_j has shape [E, out_channels]

        # Step 3: Normalize node features.
        row, col = edge_index
        deg = degree(row, size[0], dtype=x_j.dtype)
        deg_inv_sqrt = deg.pow(-0.5)
        norm = deg_inv_sqrt[row] * deg_inv_sqrt[col]

        return norm.view(-1, 1) * x_j

    def update(self, aggr_out):
        # aggr_out has shape [N, out_channels]

        # Step 5: Return new node embeddings.
        return aggr_out
```

**GraphSAGE Example**

```
import torch
from torch.nn import Sequential as Seq, Linear, ReLU
from torch_geometric.nn import MessagePassing
from torch_geometric.utils import remove_self_loops, add_self_loops
class SAGEConv(MessagePassing):
    def __init__(self, in_channels, out_channels):
        super(SAGEConv, self).__init__(aggr='max') #  "Max" aggregation.
        self.lin = torch.nn.Linear(in_channels, out_channels)
        self.act = torch.nn.ReLU()
        self.update_lin = torch.nn.Linear(in_channels + out_channels, in_channels, bias=False)
        self.update_act = torch.nn.ReLU()
        
    def forward(self, x, edge_index):
        # x has shape [N, in_channels]
        # edge_index has shape [2, E]
        
        
        edge_index, _ = remove_self_loops(edge_index)
        edge_index, _ = add_self_loops(edge_index, num_nodes=x.size(0))
        
        
        return self.propagate(edge_index, size=(x.size(0), x.size(0)), x=x)

    def message(self, x_j):
        # x_j has shape [E, in_channels]

        x_j = self.lin(x_j)
        x_j = self.act(x_j)
        
        return x_j

    def update(self, aggr_out, x):
        # aggr_out has shape [N, out_channels]


        new_embedding = torch.cat([aggr_out, x], dim=1)
        
        new_embedding = self.update_lin(new_embedding)
        new_embedding = self.update_act(new_embedding)
        
        return new_embedding
```
