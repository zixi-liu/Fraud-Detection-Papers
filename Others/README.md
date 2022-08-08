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

---

### PCA降维
- [深入理解PCA降维](https://zhuanlan.zhihu.com/p/269432722)

---

### 决策树的前世今生系列

- [深入理解决策树模型](https://zhuanlan.zhihu.com/p/359085365)
- [Induction of Decision Trees](https://hunch.net/~coms-4771/quinlan.pdf)
- [Decision Tree Algorithm, The University of Iowa](http://user.engineering.uiowa.edu/~comp/public/DecisionT1.pdf)

最早的决策树算法：CLS算法[Hunt, 1966]
- [Divide and Conquer]分而治之:假设初始训练数据集为S，选取一个属性，按照这个属性的不同取值将数据分为不同子集S1, S2,..., SN。如果某个子集的类别都是相同的或者子集为空，那么分类结束；否则继续选取新的属性，将该子集再次划分为更小的子集。
  - Divide the training data set into disjoint sets S1, S2, …, SN so that they create a partition based on a single feature.
- 最大的问题就是随机选取属性，而不同属性的分类效果差异巨大。

基于信息增益来选择属性：ID3算法[Quinlan, 1986]

- 定义事件 $a_i$ 的信息熵为
  - ![image](https://user-images.githubusercontent.com/46979228/183322460-b5f563b2-001f-42a7-981e-50a2f733356e.png)
- Entropy只与X的概率分布有关，Entropy越大，则随机变量的不确定性越大。
  - ![image](https://user-images.githubusercontent.com/46979228/183323040-765a1608-55b1-4755-b82b-e00ebf09fc50.png)
- 对于训练数据集（或者它的子集），计算其对于所有特征的信息增益，选择信息增益最大的特征作为分类属性。

基于信息增益比来选择属性：C4.5算法[1993]
- 信息增益的一个问题是它倾向于选取那些取值较多的属性。使用信息增益比可以予以矫正。
  - 信息增益比：信息增益除以属性A的不确定度。
  - [C4.5 Algorithm works with continuous features by using a discretization scheme. It also handles cases with missing data.](http://inferate.blogspot.com/2015/06/c45-decision-trees-with-missing-data.html) 

决策树算法的一般综述
- 生成空决策树与样本属性集合Feature Set（全局变量）
- 如果样本集合 T 中所有元素属于同一类，生成结点 T，并终止算法（递归基准）
- 选取一个属性（随机or信息增益or信息增益比），并生成结点（记作A）
- 根据该属性的不同取值，把 T 划分为不同子集
- 删除该属性 A
- 转到第2步，对每个子集递归调用算法的 2-6 步.

一个理想的决策树应该满足：叶子结点数最少 或 叶子结点深度最小 或 叶子结点数最少且叶子结点深度最小。

决策树的剪枝
- 防止对噪声数据或者一些孤立点的过度学习导致过拟合。降低树的复杂程度，提高泛化能力。
  - 剪枝的基本思想：极小化整体的损失函数或代价函数。
  - 找到一组具有同一父亲结点的叶结点，如果将这组叶结点删去后能使得损失函数变小，那么就删去。
  
决策树的CART算法（只生成二叉树）[Breiman 1984]
- 分类问题：Gini 指标，Towering，order Towering
  - 预测值是离散的，通常会将叶子结点中多数样本的类别作为该节点的预测类别。
  - 通过Gini最小化进行最优特征选择，决定最优切分点。样本分布越集中，Gini越小。
  - 停止条件可以是Gini小于某阈值或节点样本数小于一定阈值。
- 回归问题：MSE, MAE
  - 预测值是连续的，通常会将叶子结点中多数样本的平均值作为该节点的预测值。
  - 通过计算分裂后子节点的平方误差和，选择平方误差和最小的作为最优特征和最优切分点。
  - 停止条件可以是平方误差均相同或减小值小于某一阈值，或节点包含的样本数小于某一阈值。


---

### Boosting家族系列

- [深入理解Boosting算法-1 基础回归树](https://zhuanlan.zhihu.com/p/129079207)
- [深入理解Boosting算法-2 AdaBoost](https://zhuanlan.zhihu.com/p/129079870)
- [深入理解Boosting算法-3 GBDT](https://zhuanlan.zhihu.com/p/129080589)
- [深入理解Boosting算法-4 XGBoost](https://zhuanlan.zhihu.com/p/136243990) 
- [XGBoost常见问题解答](https://zhuanlan.zhihu.com/p/269193235)
- [Bagging和Boosting的区别](https://cloud.tencent.com/developer/news/393218#:~:text=Bagging%EF%BC%9A%E8%AE%AD%E7%BB%83%E9%9B%86%E6%98%AF%E5%9C%A8,%E7%9A%84%E5%88%86%E7%B1%BB%E7%BB%93%E6%9E%9C%E8%BF%9B%E8%A1%8C%E8%B0%83%E6%95%B4%E3%80%82&text=Boosting%EF%BC%9A%E6%A0%B9%E6%8D%AE%E9%94%99%E8%AF%AF%E7%8E%87%E4%B8%8D%E6%96%AD,%E5%A4%A7%E5%88%99%E6%9D%83%E9%87%8D%E8%B6%8A%E5%A4%A7%E3%80%82)

Boosting的基本思想是将多个弱学习器整合成一个强学习器。

**AdaBoost**
- AdaBoost为每个弱学习器赋予不同的权值。
  - 在训练过程中加大上一次分类错误样本的权重，减小分类正确样本的权重。
  - 通过分类器的误差率计算分类器的权值，分类误差率越小，权值越大。
  - 针对损失函数最小化进行优化。
  - AdaBoost能够对抗过拟合问题。

**Gradient Boosting [Friedman, 1998]**
- 与AdaBoost不同的是，GDBT将损失函数梯度下降方向作为优化目标。
- 在进行第m+1轮训练时，GDBT并不改变Fm(x)，而是在其基础上增加一个新模型h(x)。
  - ![image](https://user-images.githubusercontent.com/46979228/183329402-5cfd07e4-6a37-4b0a-868a-9de80dec572b.png)
  - 每次子模型学习的都是前面所有子模型预测值之和与真实值之间的残差。
- Shrinkage：模型的权重系数，对当前模型的进行降权，类似"learning rate"的概念。
  - Shrinkage减小时，训练轮数M会增大。
- GBDT中的样本权重：当训练集中的存在很大权重小，但是数量巨大的样本时，这样的低权重样本可能会占主导作用，抑制模型对于分类错误样本的学习；
  - 可以在训练过程中根据样本的权重，区分困难样本与简单样本；

**XGBoost**

在GBDT训练过程中，最耗时的部分在于回归树的构建过程中最优分裂特征，分裂阈值的查找过程。
- 目标函数由损失函数与正则项组成。
  - ![image](https://user-images.githubusercontent.com/46979228/183332487-da85b3ed-8891-48f4-a748-d192a701a9e0.png)
  - 训练中从损失函数到树的评分函数，得分越小，说明树的结构越好。
  - 正则项1）通过叶子节点数T控制树的复杂度， 2）控制叶子节点的权重分数，使得权重值更平滑。
- 特征最优切分点算法
  - 贪心算法
  - 近似算法
- 稀疏特征处理方式
  - 在XGBoost中，在每个节点分裂时，额外增加了一个针对缺失特征的分裂方向的判断。
- 并行训练
  - 特征维度的并行训练：训练之前，每个特征按特征值对样本进行预排序，并存储为Block结构，在后面查找特征分割点时可以重复使用。

**LightGBM**


---

### ML模型评估系列
- [Underspecification Presents Challenges for Credibility in Modern Machine Learning](https://arxiv.org/pdf/2011.03395.pdf)

三点模型评估压力测试思路：
- 分层表现评估(Stratified performance evaluations)
  - 根据特征分层数据集，检验不同层中预测器表现是否稳定。
- 迁移表现评估(Shifted performance evaluations)
  - 图像处理-将数据映射到另一个数据分布上，测试预测器表现是否稳定。
- 对比评估(Constrastive evaluations)
  - 用特例集验证预测器表现。

---

### MLP

### RecSys-Wide&Deep

模型结构: Wide部分LR, Deep部分MLP。Wide部分增强模型记忆能力，Deep部分增强模型泛化能力。

<img width="553" alt="image" src="https://user-images.githubusercontent.com/46979228/178784339-c7e1c708-5c61-49d8-827f-8f4cf6a5feed.png">


**哪些特征适合Wide/Deep**

---

### Linear Algebra 基础

**线性代数的几何意义**

矩阵乘法是把任意一个向量变成另一个方向或长度都大多不同的新向量。这个变换的过程中，原向量主要发生旋转、伸缩变化。如果矩阵对某一个向量只发生伸缩变换，不产生旋转效果，那么这些向量称为这个矩阵的eigenvector，伸缩的比例就是eigenvalue。
- 物理意义即eigenvector在矩阵的作用下伸缩运动，伸缩幅度就由eigenvalue决定。

$A\bar{v} = \lambda\bar{v}$ 即 $|A-\lambda I| = 0$
- somehow对角矩阵是对基向量进行拉伸。
- 线性不变量：特征值再怎么变也不会离开特征空间。
- 特征值是震动的谱。

**相似变换与特征值**

相似矩阵的几何意义是同一个线性变换在不同基下的表达形式。

**矩阵对角化**

对n阶矩阵A，如果可以找到逆矩阵P，使得$P^{-1}AP$ = 对角阵，则称把方阵A对角化。
- 充要条件：n阶矩阵有n个线性无关的特征向量。
- n阶实对称矩阵一定有n个线性无关的特征向量，所以实对称矩阵一定可以对角化。
- $C^{-1}AC = C^{T}AC =$ 对角矩阵

**特征值分解**

几何意义上，特征向量描述了矩阵对应的线性变换的主要变换方向。特征值描述该方向上的变换速度。把特征值排序，从小到大的特征值及特征向量能近似描述原矩阵的主要变换方向和变换速度。
- 特征值分解：特征值表示这个特征多么重要，特征向量表示这个特征是什么。
- [SVD及其应用](https://www.cnblogs.com/LeftNotEasy/archive/2011/01/19/svd-and-applications.html)




