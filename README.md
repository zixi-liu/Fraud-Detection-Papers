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

### 二、终端风控组件 User Authentication Approaches

**设备指纹 Device Fingerprint**

**生物探针 Biometrics-Based Authentication**
- [You are How You Touch: User Verification on Smartphones via Tapping Behaviors](https://www.eecis.udel.edu/~hnw/paper/icnp14.pdf)

**智能验证码 Verification Code**

### 三、特征工程 Feature Engineering

**Embedding**
- [[Word2Vec] Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/pdf/1301.3781.pdf)
- [[Word2Vec] word2vec Parameter Learning Explained](https://arxiv.org/pdf/1411.2738.pdf)
- [Embeddings of Categorical Variables for Sequential Data in Fraud Context](http://oliviercaelen.be/doc/AMLTA2018_paper_7.pdf)

**网络特征学习 Network Representation Learning**

Graph Embedding模型：DeepWalk, node2cev, LINE, SDNE, Struc2Vec, GraRep.
- [[DeepWalk]: Online Learning of Social Representations](http://www.perozzi.net/publications/14_kdd_deepwalk.pdf)
- [[node2vec]: Scalable Feature Learning for Networks](https://www.kdd.org/kdd2016/papers/files/rfp0218-groverA.pdf)
- [[LINE]: Large-scale Information Network Embedding](https://arxiv.org/pdf/1503.03578.pdf)
- [[SDNE]: Structural Deep Network Embedding](https://arxiv.org/pdf/1503.03578.pdf)
- [[Struc2Vec]: Learning Node Representations from Structural Identity](https://arxiv.org/pdf/1704.03165.pdf)
- [[GraRep]:  Learning Graph Representations with Global Structural Information](https://github.com/zixi-liu/Fraud-Detection-Papers/blob/main/GNN/GraRep-%20Learning%20Graph%20Representations%20with%20Global%20Structural%20Information.pdf)
- [A novel approach for automated credit card transaction fraud detection using network-based extensions](http://eliassi.org/papers/vanvlasselaer_dss2015.pdf)


**数据增强 Data Augmentation**
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
- [A Comprehensive Survey on Graph Neural Networks](https://arxiv.org/pdf/1901.00596.pdf)
- [[GCN] Semi-Supervised Classification with Graph Convolutional Networks](https://arxiv.org/pdf/1609.02907.pdf)
- [[GraphSage] Inductive Representation Learning on Large Graphs](https://arxiv.org/pdf/1706.02216.pdf)
- [[GAT] Graph Attention Networks](https://arxiv.org/pdf/1710.10903.pdf)

**反欺诈图神经网络框架**
- [[Ant Group] AGL: A Scalable System for Industrial-purpose Graph Machine Learning](https://arxiv.org/pdf/2003.02454.pdf)
- [[Ant Group] GeniePath: Graph Neural Networks with Adaptive Receptive Paths](https://export.arxiv.org/pdf/1802.00910)
- [[Alibaba] AliGraph: A Comprehensive Graph Neural Network Platform](https://arxiv.org/pdf/1902.08730.pdf)
- [[Pytorch Geometric] Pytorch-Geometric implementation of a series of Graph Neural Network (GNN) based fake news detection models](https://github.com/safe-graph/GNN-FakeNews)

**线上支付**
- [[Online Payment Services] Representing Fine-Grained Co-Occurrences for Behavior-Based Fraud Detection in Online Payment Services](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9085905)

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


### 七、其它相关资源

- [图算法学习-高密子图挖掘](https://zhuanlan.zhihu.com/p/45625323)
- [开源分布式图数据库](https://zhuanlan.zhihu.com/p/152399147)
