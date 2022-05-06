# Graph-Based Fraud Detection Papers

#### Table of Content

- [[Online Payment Services] Representing Fine-Grained Co-Occurrences for Behavior-Based Fraud Detection in Online Payment Services, 2022](#Representing-Fine-Grained-Co-Occurrences-for-Behavior-Based-Fraud-Detection-in-Online-Payment-Services)
- [[UFA] Unveiling Fake Accounts at the Time of Registration: An Unsupervised Approach, 2021](#unveiling-fake-accounts-at-the-time-of-registration---an-unsupervised-approach)


| Year  | Title | Entity | Paper | Code  |
| :---: | :---: | :---: | :---: | :---: |
| 2022  | **Representing Fine-Grained Co-Occurrences for Behavior-Based Fraud Detection in Online Payment Services** | IEEE | [[IEEE2022]](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9085905) | Code |
| 2021  | **Unveiling Fake Accounts at the Time of Registration: An Unsupervised Approach** | Tencent | [[KDD2021]](https://dl.acm.org/doi/pdf/10.1145/3447548.3467094) | Code |

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
