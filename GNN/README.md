# GNN-Based Fraud Detection Papers


| Year  | Title | Company | Paper | Code  |
| :---: | :---: | :---: | :---: | :---: |
| 2021  | **Unveiling Fake Accounts at the Time of Registration: An Unsupervised Approach** | Tencent | [[KDD2021]](https://dl.acm.org/doi/pdf/10.1145/3447548.3467094) | Code |

## Unveiling Fake Accounts at the Time of Registration: An Unsupervised Approach

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

**Unsupervised Weight Learning**
- Construct a registration-feature bigraph to capture the relationship between registration accounts and features. Each node in
the bigraph represents either a registration account or a feature, and each edge between a registration node and a feature node indicates that the registration account has the feature.
- Design a statistical method to initialize the weight of each node in the bigraph. The weight of node quantifies the node’s anomaly.

**Construct a Registration Graph**
- Directly capture the correlation between registration accounts. Specifically, we map the registrationfeature bigraph into a registration graph, where each node is a registration account and an edge is added between two registration accounts if their similarity is higher than a threshold. The similarity
between two registration accounts is defined as the sum of weights of features shared by the two accounts. In the constructed registration graph, fake accounts are likely to be densely connected, while benign accounts are likely to be sparsely connected.

**Fake Account Detection**
- Utilize a community detection algorithm to cluster the registration accounts into communities in the fake account detection component. We treat all accounts in a community as fake accounts if the community size is larger than a threshold.
