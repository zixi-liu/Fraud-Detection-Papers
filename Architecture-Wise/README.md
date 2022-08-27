## Graph ML System Design & Computation Frameworks

- [[Google Graph Mining] Graph Mining and Learning @ NeurIPS](https://gm-neurips-2020.github.io/)



**图数据采样**

图分割
- [图分割技术总结](https://zhuanlan.zhihu.com/p/446152634)
  - 点分割（vertext partitioning or edge-cut partitioning）
  - 边分割（edge partitioning or vertex-cut partitioning）

子图采样
- 单机内存-PaGraph

**Setting up Prediction Tasks**

- How to split graph dataset into train, validation and test datasets?

1. Fixed split: We will split our dataset once
- Training set: used for optimizing GNN parameters
- Validation set: develop model/hyperparameters
- Test set: held out until we report final performance

A concern: sometimes we cannot guarantee that the test set will really be held out.

Random split: we will randomly split our dataset into training / validation / test
- We report average performance over different random seeds.

2. Transductive setting

The input graph can be observed in all the dataset splits (training, validation and test set).
-  We will only split the (node) labels.

3. Inductive setting

We break the edges between splits to get multiple graphs
- Now we have 3 graphs that are independent

Each split can only observe the graph(s) within the split.
- A successful model should generalize to unseen graphs.
