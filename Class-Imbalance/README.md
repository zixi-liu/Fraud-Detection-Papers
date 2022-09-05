## 样本均衡采样策略

- [SMOTE: Interpolating synthetic minority class examples](https://arxiv.org/pdf/1106.1813.pdf)
- [数据不平衡解决方案综述](https://cloud.tencent.com/developer/news/392287)


## Focal Loss

**Focal Loss** 损失函数是在标准交叉熵损失基础上修改得到的。这个函数可以通过减少易分类样本的权重，使得模型在训练时更专注于难分类的样本。原文 Baseline：给正负样本加上权重，负样本出现的频次多，那么就降低负样本的权重，正样本数量少，就相对提高正样本的权重。但是该办法没法控制容易分类和难分类样本的权重，于是就有了focal loss。

- [Focal Loss 论文详解](https://zhuanlan.zhihu.com/p/49981234)
  - 目的是通过调制系数减少易分类样本的权重，从而使得模型在训练时更专注于难分类的样本。
- [Focal Loss与LightGBM实现](https://maxhalford.github.io/blog/lightgbm-focal-loss/)
