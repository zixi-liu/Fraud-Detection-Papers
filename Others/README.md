## ML Knowledge Bank

用于收藏ML相关科普类文章:)

### 神经科学简史系列

文章来源：SIGAI
- [1. 理解计算与感知机](https://mp.weixin.qq.com/s?__biz=MzU4MjQ3MDkwNA==&mid=2247484981&idx=1&sn=d3003468b9853851923844812993e060&chksm=fdb69ba2cac112b4dac620d52100ebd033eb679f29340726a67297c4d6980b16c7cc91122028&scene=21#wechat_redirect)
- [2. 神经计算历史背景](https://mp.weixin.qq.com/s?__biz=MzU4MjQ3MDkwNA==&mid=2247485155&idx=1&sn=990cc7400751c36e9fef0a261e6add2a&chksm=fdb69b74cac112628bdae14c6435120f6fece20dae9bf7b1ffc8b8b25e5496a24160feca0a72&scene=21#wechat_redirect)
- [3. 神经网络数学模型](https://mp.weixin.qq.com/s?__biz=MzU4MjQ3MDkwNA==&mid=2247485592&idx=1&sn=1c5236972402ea8cb168161bc41e8e7e&chksm=fdb6950fcac11c19ad047e7cb9ced96447a85b41e21b10789a86ae4a211e4fb2ca1f911a7fc5&scene=21#wechat_redirect)
- [4. Adaline诞生/凛冬将至](https://mp.weixin.qq.com/s?__biz=MzU4MjQ3MDkwNA==&mid=2247486202&idx=1&sn=bf66be1e71272be42508e557ed93acbf&chksm=fdb6976dcac11e7b9d0f878233e8d9907825e57851e7a095f1be3a23abc9327370a77f4e2c03&scene=21#wechat_redirect)
- [5. 导数的前世今生](https://mp.weixin.qq.com/s?__biz=MzU4MjQ3MDkwNA==&mid=2247487049&idx=1&sn=e7ddcb30c8a3cc336fb59023c30f2cf9&chksm=fdb693decac11ac84377730bae28a6375650c91c4f8f9181e97848ba492d124ae36adcdcf612&scene=21#wechat_redirect)
- [6. 统计学习理论与支持向量机](https://mp.weixin.qq.com/s?__biz=MzU4MjQ3MDkwNA==&mid=2247489453&idx=1&sn=d24e8738e6d0ddd069a51c4682464809&chksm=fdb68a3acac1032c0395109c2cd092c8e61d87c81adac0af0f102ac80f22ecf55de19134f908&scene=21#wechat_redirect)
- [7. 无处不在的贝叶斯](https://mp.weixin.qq.com/s?__biz=MzU4MjQ3MDkwNA==&mid=2247490017&idx=1&sn=bc15e07ae76282c82826a64e662de0e5&chksm=fdb68476cac10d6027a7b8e9883c5652950de6e989c0f57cf460aaeba89e717d4ab84decab22&scene=21#wechat_redirect)
- [8. 深度学习发展简史](https://mp.weixin.qq.com/s/mDRo3v9UPhmFZcdSSGoacQ)

### PCA降维
- [深入理解PCA降维](https://zhuanlan.zhihu.com/p/269432722)

### 决策树

- [深入理解决策树](https://mp.weixin.qq.com/s/ZV8f3YMve2QuWNZiTtv34g)


### Boosting家族

- [深入理解Boosting算法-1 基础回归树](https://zhuanlan.zhihu.com/p/129079207)
- [深入理解Boosting算法-2 AdaBoost](https://zhuanlan.zhihu.com/p/129079870)
- [深入理解Boosting算法-3 GBDT](https://zhuanlan.zhihu.com/p/129080589)
- [深入理解Boosting算法-4 XGBoost](https://zhuanlan.zhihu.com/p/136243990) 

### ML模型评估
- [Underspecification Presents Challenges for Credibility in Modern Machine Learning](https://arxiv.org/pdf/2011.03395.pdf)

三点模型评估压力测试思路：
- 分层表现评估(Stratified performance evaluations)
  - 根据特征分层数据集，检验不同层中预测器表现是否稳定。
- 迁移表现评估(Shifted performance evaluations)
  - 图像处理-将数据映射到另一个数据分布上，测试预测器表现是否稳定。
- 对比评估(Constrastive evaluations)
  - 用特例集验证预测器表现。

### MLP

### RecSys-Wide&Deep

模型结构: Wide部分LR, Deep部分MLP。Wide部分增强模型记忆能力，Deep部分增强模型泛化能力。

<img width="553" alt="image" src="https://user-images.githubusercontent.com/46979228/178784339-c7e1c708-5c61-49d8-827f-8f4cf6a5feed.png">


**哪些特征适合Wide/Deep**


### Linear Algebra 基础

**线性代数的几何意义**

矩阵乘法是把任意一个向量变成另一个方向或长度都大多不同的新向量。这个变换的过程中，原向量主要发生旋转、伸缩变化。如果矩阵对某一个向量只发生伸缩变换，不产生旋转效果，那么这些向量称为这个矩阵的eigenvector，伸缩的比例就是eigenvalue。
- 物理意义即eigenvector在矩阵的作用下伸缩运动，伸缩幅度就由eigenvalue决定。

$A\bar{v} = \lambda\bar{v}$ 即 $|A-\lambda I| = 0$
- somehow对角矩阵是对基向量进行拉伸。
- 线性不变量：特征值再怎么变也不会离开特征空间。
- 特征值是震动的谱。






