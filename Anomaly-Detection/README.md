### Anomaly Detection相关

- [ADBench: Anomaly Detection Benchmark](https://arxiv.org/pdf/2206.09426.pdf)
- [A Unifying Review of Deep and Shallow Anomaly Detection](https://arxiv.org/pdf/2009.11732.pdf)

基于自监督学习
- [CSI: Novelty Detection via Contrastive Learning on Distributionally Shifted Instances](https://arxiv.org/pdf/2007.08176.pdf)
  - Training scheme contrasts the sample with distributionally-shifted augmentations of itself.
  - Model learns a new task of discriminating between in- and out-of-distribution, in addition to the original task of discriminating within in-distribution.
  
### Transfer Learning

**特征变换迁移**

统计特征变换迁移
- Maximum Mean Discrepancy, MMD 最大均值差异
  - 求两个概率分布映射到另一个空间中的数据的均值之差。
- 度量学习
  - 核心是聚类假设：同一簇数据极有可能属于同一级别。度量学习着重刻画样本与样本间的距离。度量学习对于类内距、类间距的学习更加重视。
  - Linear Discriminant Analysis, LDA
  - [Metric Learning: A Survey](https://people.bu.edu/bkulis/pubs/ftml_metric_learning.pdf)
  - [度量学习 Deep Metric Learning: A Survey](https://zhuanlan.zhihu.com/p/348998459)
