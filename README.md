# Fraud Detection-反欺诈学习资料、应用实例

汇总反欺诈领域论文学习资料、基于传统机器学习以及图算法的反欺诈应用实例。如有侵权，以下是我的联系方式：

- Linkedin: [Zixi Liu](https://www.linkedin.com/in/betty-zixi-liu?original_referer=https%3A%2F%2Fwww.google.com%2F)

**经典论文总结**
- [反欺诈算法经典论文解读](https://zhuanlan.zhihu.com/p/85155064)
- [Awesome Collection of Fraud Detection Papers](https://github.com/benedekrozemberczki/awesome-fraud-detection-papers)
- [TitAnt: 蚂蚁金融在线实时交易欺诈检测](https://arxiv.org/pdf/1906.07407.pdf)


## 目录

### 一、概述 Overview

- [Credit card fraud detection using machine learning: A survey](https://arxiv.org/pdf/2010.06479.pdf)
- [Context-aware credit card fraud detection](https://tel.archives-ouvertes.fr/tel-02902117/document)
- [Graph-based Anomaly Detection and Description: A Survey](https://arxiv.org/pdf/1404.4679.pdf)
- [风控要略-互联网业务反欺诈之路](https://weread.qq.com/web/reader/3ef321f071fd5a9d3effb02)

**ML风控模型策略分析流程**

1. 样本提取
  - 模型开发时的跨时间验证集（OOT）：主要用于衡量同时期新模型相对于旧模型的模型效果提升度和制定决策点（Cut-off）时的效果预估。
  - 近期授信样本集（BackScore）：近期所有进入模型打分阶段的样本集，包含被模型通过和拒绝的所有样本，主要用于设定新模型在于其通过率下的模型阈值Threshold。
  
2. 模型策略的制定：一般需要在转化率Conversion Rate与坏账率之间进行权衡。

单模型策略：用于业务前期中期，模型间关联性较强时。
- 基于模型通过率与坏账率的决策点：理想状态是提高通过率并降低坏账率，可以有两种选择：
  - 保持目标模型通过率，降低坏账率（利用近期样本找到同等通过率对应的模型分作为决策点）
  - 提升模型通过率，保持坏账率（利用跨时间验证集和近期样本评估得到同等坏账率的模型分作为决策点）
- 基于lift的决策点设定：lift表示风控模型对预测目标中不良客户的识别比率高于随机识别比率的倍数。Lift分箱将所有客户的模型评分分为10-20箱，计算Cumulatively Bad(%) by Model与Cumulatively Bad(%) Randomly的比值即为lift。通过lift的大小，我们可以设定模型的决策阈值。

多模型策略：利用加权等方式将多个模型分融合成一个模型分。
- 多模型串行准入：多个模型以串行方式依次决策准入。

<img src="https://user-images.githubusercontent.com/46979228/177881184-9dc947ff-4059-4d21-ac09-e82f5d95f9d5.png" width="400"/>

- 多模型交叉准入：在生成风险等级的过程中，需要充分考虑每个交叉格子中样本量，保证其统计学意义。

<img src="https://user-images.githubusercontent.com/46979228/177881348-a5bc658f-cfdb-4086-9841-1f5017428acd.png" width="400"/>

3. 模型策略评估

4. 模型策略的上线与验证


### 二、终端风控组件 User Authentication Approaches

**设备指纹 Device Fingerprint**

**生物探针 Biometrics-Based Authentication**
- [You are How You Touch: User Verification on Smartphones via Tapping Behaviors](https://www.eecis.udel.edu/~hnw/paper/icnp14.pdf)

**智能验证码 Verification Code**

### 三、特征工程 Feature Engineering

数据预处理，特征选择，特征降维。

**1. Preprocessing 预处理**

*特征清洗*
- 清洗异常样本
- 采样：正负样本不均衡，样本权重

[基于Spark的特征处理](https://time.geekbang.org/column/article/295300)

*数值型特征*
- 归一化 Normalizer：处理特征值尺度不同问题 （i.e. min-max, scale to [-1, 1], z-score, log-based, L2, Gauss Rank, Robust Scaling etc.）
- 分箱 Binning：处理特征值分布不均匀问题（有监督分箱如卡方分箱、决策树分箱/无监督分桶如固定宽度分箱、分位数分箱等）
  - 将连续特征离散化，旨在引入非线性变换，对异常值不敏感、防止过拟合；
  - Tree-based模型中，高基数特征相对于低基数特征处于支配地位。

*类别型特征*
- 交叉组合FM/分箱 Binning/Count Encoding/Target Encoding/Odds Ratio/相关系数/WOE
  - [特征交叉组合模型演化简史](https://zhuanlan.zhihu.com/p/269730650)

*时序特征*
- 历史事件分时段统计

**2. Feature Selection 特征选择**

高质量特征有区分性(Informative)，特征之间有相互独立性(Independent)，特征应易于理解。
- 过滤法 Filter (根据目标变量与自变量之间的关联)
  - 单变量特征过滤：卡方检验，ANOVA，信息增益等。
  - 多变量特征过滤
  - [[多元特征过滤] Relief-Based Feature Selection: Introduction and Review](https://arxiv.org/pdf/1711.08421v2.pdf)
  - [[谱图] Spectral Feature Selection for Supervised and Unsupervised Learning](https://www.public.asu.edu/~huanliu/papers/icml07.pdf)
- 包装法 Wrapper
  - 根据目标函数(AUC/MSE)变化决定是否加入特征变量。
- 嵌入法 Embedded
  - 学习器自动选择特征：L1正则化，L2 Ridge，决策树，信息增益，深度学习等。
- 图特征选择 Graph-based
  - [Feature Selection with Linked Data in Social Media, 2012](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.228.8109&rep=rep1&type=pdf)
  - [Unsupervised Feature Selection for Linked Social Media Data, 2012](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.300.2277&rep=rep1&type=pdf)
  - [Efficient Partial Order Preserving Unsupervised Feature Selection on Networks](https://epubs.siam.org/doi/pdf/10.1137/1.9781611974010.10)
  - [Unsupervised Feature Selection on Networks: A Generative View](https://ojs.aaai.org/index.php/AAAI/article/view/10309/10168)

**Embedding**
- [[Word2Vec] Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/pdf/1301.3781.pdf)
- [[Word2Vec] word2vec Parameter Learning Explained](https://arxiv.org/pdf/1411.2738.pdf)
- [Embeddings of Categorical Variables for Sequential Data in Fraud Context](http://oliviercaelen.be/doc/AMLTA2018_paper_7.pdf)

**图表示学习 Network Representation Learning**

Graph Embedding模型：DeepWalk, node2cev, LINE, SDNE, Struc2Vec, GraRep.
- [[DeepWalk]: Online Learning of Social Representations](http://www.perozzi.net/publications/14_kdd_deepwalk.pdf)
- [[node2vec]: Scalable Feature Learning for Networks](https://www.kdd.org/kdd2016/papers/files/rfp0218-groverA.pdf)
- [[LINE]: Large-scale Information Network Embedding](https://arxiv.org/pdf/1503.03578.pdf)
- [[SDNE]: Structural Deep Network Embedding](https://arxiv.org/pdf/1503.03578.pdf)
- [[Struc2Vec]: Learning Node Representations from Structural Identity](https://arxiv.org/pdf/1704.03165.pdf)
- [[GraRep]:  Learning Graph Representations with Global Structural Information](https://github.com/zixi-liu/Fraud-Detection-Papers/blob/main/GNN/GraRep-%20Learning%20Graph%20Representations%20with%20Global%20Structural%20Information.pdf)
- [A novel approach for automated credit card transaction fraud detection using network-based extensions](http://eliassi.org/papers/vanvlasselaer_dss2015.pdf)
- [[Capital One (2019)] DeepTrax: Embedding Graphs of Financial Transactions](https://arxiv.org/pdf/1907.07225.pdf)


**3. 数据增强 Data Augmentation**
- [[Knowledge Graph] Injecting Semantic Background Knowledge
into Neural Networks using Graph Embeddings](https://perso.liris.cnrs.fr/pierre-edouard.portier/publications/2017_ZIEGLER_PORTIER_WETICE_injecting_semantic_background_knowledge_into_neural_networks_using_graph_embeddings.pdf)


### 四、文本挖掘 Text Mining

### 五、有监督学习 Supervised Learning

**经典树模型 Tree-Based Models**

决策树模型以及基于树模型的Boosting模型
- [The Elements of Statistical Learning, <Chapter 9, 10>](https://esl.hohoweiya.xyz/book/The%20Elements%20of%20Statistical%20Learning.pdf)
- [Greedy Function Approximation A Gradient Boosting Machine](https://projecteuclid.org/journals/annals-of-statistics/volume-29/issue-5/Greedy-function-approximation-A-gradient-boostingmachine/10.1214/aos/1013203451.full)


### 六、序列模型 Sequence Modeling

**图模型 Graphical Models**

利用关系网络识别网络中异常的网络结构和社群。
- [[JD Finance] Graph mining assisted semi-supervised learning for fraudulent cash-out detection](https://nosh.northwestern.edu/wp-content/uploads/2020/10/Graph-mining-assisted-semi-supervised-learning-for-fraudulent-cash-out-detection.pdf)

**循环神经网络 Recurrent Neural Networks**

- [[JD Finance] Session-Based Fraud Detection in Online E-Commerce Transactions Using Recurrent Neural Networks](http://ecmlpkdd2017.ijs.si/papers/paperID69.pdf)
- [[Alibaba] Online Credit Payment Fraud Detection via Structure-Aware Hierarchical
Recurrent Neural Network](https://www.ijcai.org/proceedings/2021/0505.pdf)

### 七、图神经网络 Graph Neural Network-based Modeling

**图神经网络入门**
- [Graph neural networks: A review of methods and applications](https://arxiv.org/pdf/1812.08434.pdf)
- [[GCN] Semi-Supervised Classification with Graph Convolutional Networks](https://arxiv.org/pdf/1609.02907.pdf)
- [[GraphSage] Inductive Representation Learning on Large Graphs](https://arxiv.org/pdf/1706.02216.pdf)
- [[GAT] Graph Attention Networks](https://arxiv.org/pdf/1710.10903.pdf)

**反欺诈图神经网络框架**
- [[KDD 2016] FRAUDAR: Bounding Graph Fraud in the Face of Camouflage](https://www.kdd.org/kdd2016/papers/files/rfp0110-hooiA.pdf)
- [[Ant Group] AGL: A Scalable System for Industrial-purpose Graph Machine Learning](https://arxiv.org/pdf/2003.02454.pdf)
- [[Ant Group] GeniePath: Graph Neural Networks with Adaptive Receptive Paths](https://export.arxiv.org/pdf/1802.00910)
- [[Alibaba] AliGraph: A Comprehensive Graph Neural Network Platform](https://arxiv.org/pdf/1902.08730.pdf)
- [[Pytorch Geometric] Pytorch-Geometric implementation of a series of Graph Neural Network (GNN) based fake news detection models](https://github.com/safe-graph/GNN-FakeNews)
- [PyTorch-BigGraph](https://github.com/facebookresearch/PyTorch-BigGraph)

**线上交易支付**
- [[Online Payment Services] Representing Fine-Grained Co-Occurrences for Behavior-Based Fraud Detection in Online Payment Services](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9085905)
- [[Live-Streaming] Live-Streaming Fraud Detection: A Heterogeneous Graph Neural Network Approach](https://dl.acm.org/action/downloadSupplement?doi=10.1145%2F3447548.3467065&file=3467065-vor.pdf)

**账号安全**
- [[Wechat] Unveiling Fake Accounts at the Time of Registration: An Unsupervised Approach, 2021](https://dl.acm.org/doi/pdf/10.1145/3447548.3467094)
- [[Ant Group] Heterogeneous Graph Neural Networks for Malicious Account Detection](https://arxiv.org/pdf/2002.12307.pdf)
- [[Ant Group] Adversarial Attack on Graph Structured Data](https://arxiv.org/pdf/1806.02371.pdf)

**假新闻识别**
- [Fake News Detection on Social Media using Geometric Deep Learning](https://arxiv.org/pdf/1902.06673.pdf)

**运费骗保识别**
- [[Ant Group] Uncovering Insurance Fraud Conspiracy with Network Learning](https://arxiv.org/pdf/2002.12789.pdf)

**贷款违约预测**
- [[Ant Group] Financial Risk Analysis for SMEs with Graph-based Supply Chain Mining](https://www.ijcai.org/proceedings/2020/0643.pdf)

**洗钱识别**
- [[IBM] Anti-Money Laundering in Bitcoin: Experimenting with Graph Convolutional Networks for Financial Forensics](https://arxiv.org/pdf/1908.02591.pdf)


### 八、其它相关资源

- [鲲鹏分布式平台在蚂蚁金服的应用](http://library.usc.edu.ph/ACM/KKD%202017/pdfs/p1693.pdf)
- [理解图的拉普拉斯矩阵](https://zhuanlan.zhihu.com/p/362416124)
  - 信号处理中的滤波器用于放大或缩小相关频率，消除不相关频率。线性空间中的矩阵乘法等同于尺度变化，与频域中的滤波器操作是相同的。
- [Graph Learning综述](https://zhuanlan.zhihu.com/p/373639485)
- [图算法学习-高密子图挖掘](https://zhuanlan.zhihu.com/p/45625323)
- [开源分布式图数据库](https://zhuanlan.zhihu.com/p/152399147)
- [什么是IP地址](https://zhuanlan.zhihu.com/p/509973594)
