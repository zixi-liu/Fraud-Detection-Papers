# Graph-Based Fraud Detection Papers

#### 前言

**[数学基础] 图拉普拉斯刻画信号平滑度**

拉普拉斯算子是欧几里得空间中的二阶微分线性算子。对于n维函数f(x1, x2, ..., xn)，其拉普拉斯算子表示为:

<img width="289" alt="image" src="https://user-images.githubusercontent.com/46979228/179382850-1f74068a-55c9-4b53-b8ab-fd1896a23c1d.png">

对于离散函数f(x,y)，其拉普拉斯算子为：

<img width="574" alt="image" src="https://user-images.githubusercontent.com/46979228/179382917-eb14e15a-3981-41a5-be06-1b2232aa862e.png">

离散函数可以写成矩阵：

<img width="284" alt="image" src="https://user-images.githubusercontent.com/46979228/179382953-d789d877-2e72-40da-97bf-2dc3a4d215e1.png">

假设x和y的增量即步长全为1，则点(xi, yj)处的拉普拉斯算子可以用下面的公式近似计算

<img width="502" alt="image" src="https://user-images.githubusercontent.com/46979228/179383034-15431b75-7e96-4f1e-8279-0e00aa7b8fe2.png">

<img width="452" alt="image" src="https://user-images.githubusercontent.com/46979228/179383092-2fe06d5c-5cb5-4ae7-94af-47b37efff6c0.png">


即节点(xi, yj)的拉普拉斯算子描述的是节点与邻居节点之间信号的差异。

**图神经网络入门三篇：**
- [01. 图拉普拉斯矩阵](https://zhuanlan.zhihu.com/p/368878987)
- [02. 谱域方法](https://zhuanlan.zhihu.com/p/369382428)
- [03. 空间域方法](https://zhuanlan.zhihu.com/p/369425550)

**Message Passing消息传递范式：**
- [理解GNN消息传递机制](https://zhuanlan.zhihu.com/p/352510643)

基于消息传递范式的图神经网络（MPNN）旨在将节点的特征传播到邻居节点上，通常也会考虑添加一些权重来分配邻居之间传播特征的比例。

消息传递的两个阶段：
- 消息传递阶段
  - Aggregation Function (聚合邻居节点特征)
  - Combination Function (节点更新函数)
- 读出阶段 (聚合节点级别表示，获得图级别表示)

三篇论文对比Aggregation Function， Combination Function：
- [Every Document Owns Its Structure: Inductive Text Classification via Graph Neural Networks](https://aclanthology.org/2020.acl-main.31.pdf)
  - 将邻接矩阵与节点特征矩阵相乘，物理意义是将所有邻居特征求和。
  - 组合函数使用门控单元，由于目标是将邻居信息和节点本身信息组合起来，因此通过重置门、更新门控制邻居信息在节点更新过程中的贡献。
- [Message Passing Attention Networks for Document Understanding](https://arxiv.org/pdf/1908.06267.pdf)
  - 针对邻居信息求和后的结果，送入MLP，获得更抽象的特征表示。
- [How Powerful are Graph Neural Netowrks?](https://arxiv.org/pdf/1810.00826.pdf)
  - 聚合函数+组合函数。设计可学习参数。

### 目录


| Year  | Title | Entity | Paper | Code  |
| :---: | :---: | :---: | :---: | :---: |
| 2022  | **Representing Fine-Grained Co-Occurrences for Behavior-Based Fraud Detection in Online Payment Services** | IEEE | [[IEEE2022]](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9085905) | Code |
| 2021  | **Unveiling Fake Accounts at the Time of Registration: An Unsupervised Approach** | Tencent | [[KDD2021]](https://dl.acm.org/doi/pdf/10.1145/3447548.3467094) | Code |
| 2020 | [**Heterogeneous Graph Neural Networks for Malicious Account Detection**](#Heterogeneous-Graph-Neural-Networks-for-Malicious-Account-Detection) | Ant Group| [[arXiv2020]](https://arxiv.org/pdf/2002.12307.pdf) | Code |

### Heterogeneous Graph Neural Networks for Malicious Account Detection
#### GEM: 蚂蚁金服利用GCN针对恶意注册账户检测

1. 综述

GEM(Graph Embeddings for Malicious accounts)系统：构建的账户-不同设备异构网络，以拓扑结构和行为特征作为输入直接学习图神经网络模型。并且引入注意力机制，考虑不同类型设备的权重。

2. GEM

- **设备聚集性**

**设备定义**：设备是广义的，包括Phone Number, User Machine ID (UMID), MAC address, IMSI (International Mobile Subscriber Identity), APDID (Alipay Device ID) , TID。

**异常点定义**：如果一个帐户注册或登录同一个（一组）设备或一组公共设备，若这一个（一组）设备上有大量其他账户，那么此类帐户将是可疑的。

- **行为聚集性**

**异常点定义**：如果共享设备的账户行为是批量进行的（注册时间集中），那么这些账户是可疑的。

- **思路：连通子图**

针对恶意账户的设备和行为聚集性，直观的做法是查找连通子图：

  - 构建账户-设备二部图，这里的设备是广义的，包括手机号、IMEI、设备指纹等。
  - 将二部图转化为账户-账户之间关系图 ，并计算账户行为相似度作为权重。
  - 删除边，得到连通子图：相似度低于阈值的边删除，该阈值为超参，通过验证集进行调参。
  - 以连通子图大小作为风险Score。

连通子图虽然会存在一些问题，如无法检测到位于规模较小的连通图的恶意账户，以及IP关联的账户会存在噪声等情况，但其思想可以借鉴：

  - 连通子图大小，其实等价使用sum算子对连通的邻居进行计数。
  - 通过行为相似度限制连通性。
  - 将原始账户-设备图转化成账户-账户图，通过相似度来约束连通性。通过这转化能计算账户之间相似度，但会丢失信息。

3.  异构网络构建

- **拓扑图**

设d对应设备类型，时间窗为(0, T]（例如T为7天）。

M为边{(i, j)}的集合，若账户i在设备j上有行为（如注册、登录），则会形成边。

拓扑图 g = (V, E) 由N个节点V（账户和设备）及其之间关系E组成。邻接矩阵.

- **异构图结构**

根据不同类型的设备，抽取|D|个子图, 以及对应|D|个邻接矩阵.

每个节点特征抽取：

  - 账户行为将时间窗(0,T)等分成p段，统计账户在每段的行为次数作为特征（p维），例如7天每小时为一段，则p=7*24=168。
  - 设备类型one-hot编码：(|D|维)

一个异构连通子图的可视化：


<p align="center"><img width="436" alt="image" src="https://user-images.githubusercontent.com/46979228/172289684-5bac037d-7a97-4a24-aed7-d23a9c090e1c.png"></p>

- **目标**

给定(0, T]时间内的A和X， 以及(0, T-1]的真实标签{-1, 1}，学习一个可以在时间T上有较好区分度的函数f({A}, X)。


#### Summary Notes

## Representing Fine-Grained Co-Occurrences for Behavior-Based Fraud Detection in Online Payment Services

#### Behavioral Data Enhancement

Adopt the heterogeneous relation network, to represent the co-occurrences among transactional attributes effectively. 
- A network node (or say an entity) corresponds to an attribute value in transactions, and an edge corresponds to a heterogeneous association between different attribute values.

**Network representation learning (NRL)** effectively capture deep relationships. 
- By calculating the similarity between embedding vectors, more potential relationships could be inferred.

**Network Embedding**

The network embedding that preserves the network structure of native graph cannot directly help behavioral modeling for online payment fraud detection.
- It is intolerable to perform network embedding operation for every new transaction due to the response latency lead by large computing overhead.
- We are interested in the co-occurrence relationships among different behavioral entities rather than the relationship between a unique identifier and its entities.

**Customized Derivative Networks**

For B2C transactions, we define two different vertices, say u and v, that originally connect the same unique identifier as a vertex pair, and view it as an
edge e=(u,v).

<img src="https://github.com/zixi-liu/GNN-Fraud-Detection-Papers/blob/main/Img/FraudDetectionSys.png" alt="model" />

**Model Enhancement**
- Population-Level Models
  - Generate a derivative network where the vertices are transaction attributes and the edges with weights represent the co-occurrence frequency, taking no
account of transaction labels. We say such a derivative network is label-free.
- Individual-Level Models
  - Extract positive relationships generated from non-fraudulent transactions and negative relationships generated from fraudulent transactions. The positive relationship enhances the correlation between the agents involved, while the negative relationship weakens the correlation. We say such a derivative network is label-aware.

### Method

#### Graph Representation of Transaction Records & Network Embedding
- To transform networks from network structure to vector space, the commonly used models mainly include random walk, matrix factorization, and
deep neural networks.

#### Fraud Detection Models
- Fraud Detection in Population-Level Model: we need the features that can summarize a bunch of transactions. 
  - Embedding doesn't work well: d (dimension size of vector representation) x m (attributes).
  - Use the Cosine similarity (i.e. m(m-1)/2 similarities) to represent a transaction record. 
  - In the real online payment scenario, we divide training samples and testing samples in time order to avoid time-crossing problems.
- Fraud Detection in Individual-Level Models: information on normal transactions enhances the association of attribute vertices in the derivative network.
  - Use account_number as an agent. Detect anomalies by comparing with behavioral models when we assume that an agent’s behavioral pattern is stable.
  - **Single-Agent Behavioral Model:** Calculate the similarity of any two vector representations using the euclidean distance based on a size of d x m matrix. Introduce cohesivity to express the importance of a transaction in the behavioral model.
  - **Multi-Agent Behavioral Model:** Similar to the commonly-used agent, i.e., account number, some other attributes, e.g., merchant number and location number, can also act as the agents to build behavioral models. 

Given a transaction, its fraud score rated by its corresponding probability in the singleagent behavioral model determines whether the transaction
is fraud or not. If the transaction miss values in some attributes, we compute the average possibility of all transactions, which are related to existing attributes of the transaction.

- Population-level models compare the similarity between a transaction and the learned transactional patterns. 
- Individual-level models distinguish a transaction by contrasting the difference between its current and past patterns.

#### Evaluation


## Unveiling Fake Accounts at the Time of Registration - An Unsupervised Approach

Design UFA, an unsupervised method, to detect fake accounts at the time of registration. UFA can overcome limitations of existing fake account detection methods. Specifically, UFA consists of four components: 
- feature extraction
- unsupervised weight learning
- registration graph construction
- fake account detection

A measurement study on a real world registration dataset from WeChat show that, compared with benign accounts, fake accounts tend to cluster on **outlier registration patterns**, e.g., fake accounts are likely to use the same IPs, use the same phone numbers from the same areas, be active at midnight, or use outdated WeChat version and OS version.

### Unsupervised Weight Learning

<img src="https://github.com/zixi-liu/GNN-Fraud-Detection-Papers/blob/main/Img/fake-accounts-model.png" alt="model" />

**Feature Extraction**
- Extract features that reveal outlier registration patterns of fake accounts;

Registration Feature Bigraph

<img src="https://github.com/zixi-liu/GNN-Fraud-Detection-Papers/blob/main/Img/registration-feature-bigraph.png" alt="model" width = "400px" />

**Unsupervised Weight Learning**
- Construct a registration-feature bigraph to capture the relationship between registration accounts and features. Each node in
the bigraph represents either a registration account or a feature, and each edge between a registration node and a feature node indicates that the registration account has the feature.
- Design a statistical method to initialize the weight of each node in the bigraph. The weight of node quantifies the node’s anomaly.

- Statistical method relies on three concepts: 
   - feature frequency (the number of registration accounts who have this feature),
   - feature ratio (given a feature 𝑥 with prefix pre, the feature ratio ratio(𝑥) is defined as the fraction of its feature frequency among all features with the same prefix pre), 
   - mode feature under a feature prefix (given a feature prefix pre, the mode feature of pre is the feature 𝑥∗ with this prefix having the maximal feature ratio).
 
- Define the weight of a feature to quantify the feature anomaly:
   -  One natural choice is to relate the anomaly of the feature to its feature ratio. 
   -  Feature coupling define the weight for a feature by considering the feature ratio as well as the feature prefix’s ratio to make features with different prefixes comparable.
   -  If a feature is unique, i.e., it is used by a single registration account, we set its weight to be 0.5, which means that we consider all unique features to be neutral.

- Feature/registration weight update:
   -  Linearized belief propagation, to update each node weight in the registration-feature bigraph by considering the influence from its indirect neighbors. 

**Construct a Registration Graph**
- Directly capture the correlation between registration accounts. Specifically, we map the registrationfeature bigraph into a registration graph, where each node is a registration account and an edge is added between two registration accounts if their similarity is higher than a threshold. The similarity
between two registration accounts is defined as the sum of weights of features shared by the two accounts. In the constructed registration graph, fake accounts are likely to be densely connected, while benign accounts are likely to be sparsely connected.

**Fake Account Detection**
- Utilize a community detection algorithm to cluster the registration accounts into communities in the fake account detection component. We treat all accounts in a community as fake accounts if the community size is larger than a threshold.
   - First adopt a community detection method, e.g., Louvain method, to cluster the nodes into different communities (i.e., dense subgraphs). Second, we predict all registration accounts in the communities whose sizes are larger than a threshold to be fake accounts.
