# GNN-Based Fraud Detection Papers


| Year  | Title | Company | Paper | Code  |
| :---: | :---: | :---: | :---: | :---: |
| 2021  | **Unveiling Fake Accounts at the Time of Registration: An Unsupervised Approach** | Tencent | [[KDD2021]](https://dl.acm.org/doi/pdf/10.1145/3447548.3467094) | Code |

## Unveiling Fake Accounts at the Time of Registration: An Unsupervised Approach

Design UFA, an unsupervised method, to detect fake accounts at the time of registration. UFA can overcome limitations of existing fake account detection methods. Specifically, UFA consists of four components: 
- feature extraction;
- unsupervised weight learning; 
- registration graph construction; 
- fake account detection;

A measurement study on a real world registration dataset from WeChat show that, compared with benign accounts, fake accounts tend to cluster on **outlier registration patterns**, e.g., fake accounts are likely to use the same IPs, use the same phone numbers from the same areas, be active at midnight, or use outdated WeChat version and OS version.

### Unsupervised Weight Learning

<img src="https://github.com/zixi-liu/GNN-Fraud-Detection-Papers/blob/main/Img/fake-accounts-model.png" alt="model" />

i. Construct a registration feature bigraph to capture the relationship between registration accounts and features. 
- represent each account and each feature as a node 
- add an edge between an account and a feature if the account has the feature

ii. Design a statistical method to initialize the weight of each feature node, the weight of each registration account node based on the weights of feature
nodes.
