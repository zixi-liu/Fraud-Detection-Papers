## Contrastive Learning 对比学习

### 综述

- [对比学习（Contrastive Learning）相关进展梳理](https://zhuanlan.zhihu.com/p/141141365)
- [Contrastive Self-Supervised Learning](https://ankeshanand.com/blog/2020/01/26/contrative-self-supervised-learning.html)

类似的样本在特征空间里的相邻区域，不类似样本都在不相邻区域，学到的特征能够使其和其他样本区别开来。
- 如何定义目标函数: 正例pair和负例pair隔开至少 $\eta$ 的距离
- 如何构建正例和负例: 设计出合理的正例和负例pair，并且尽可能提升pair能够cover的semantic relation，才能让得到的表示在downstream task表现的更好。

**Contrastive Learning Framework**
- 学习一个映射函数f，把样本x编码成其表示f(x), 使得

 ![image](https://user-images.githubusercontent.com/46979228/190882819-ea6f469b-efce-4302-94b2-36819eaea3b9.png)

### CV

- [[MoCo] Momentum Contrast for Unsupervised Visual Representation Learning](https://arxiv.org/pdf/1911.05722.pdf)
- [[InstDisc] Unsupervised Feature Learning via Non-Parametric Instance Discrimination](https://arxiv.org/pdf/1805.01978.pdf)

