### GNN 原理解析

[**学习资源**](https://www.zhihu.com/topic/21216055/hot)

[**配套代码**](https://github.com/FighterLYL/GraphNeuralNetwork)

1.1 图的基本定义
- 有向图和无向图
- 非加权图和加权图
- 连通图与非连通图
- 二部图
- 邻居和度
  - 一个图所有节点的度数之和为总边数两倍。
  - 有向图中，同时定义出度（outdegree）和入度（indegree）
- 子图与路径 subgraph & path
  - 路径长度：路径中边的数目
  - 顶点距离：两个顶点之间最短路径的长度
  - k阶邻居
  - k阶子图 k-subgraph：所有距离为k的点以内（包括距离为k）的点和边组合成的子图；

1.2 图的存储与遍历
- 邻接矩阵与关联矩阵 Adjacency Matrix & Incidence Matrix
  - 用系数矩阵的格式来存储邻接矩阵，可以将邻接矩阵的空间复杂度控制在O(m)。
- 图的遍历
  - DFS 深度优先搜索
  - BFS 广度优先搜索
 
 1.3 图数据的应用场景
 - 同构图 Homogeneous Graph
   - 图中的节点类型和关系类型都仅有一种；
 - 异构图 Heterogeneous Graph
   - 图中的节点类型或关系类型多于一种；
 - 属性图 Property Graph
   - Label & property;
   - 如节点类型为“用户”，属性是节点或关系的附加描述信息，如“姓名”、“注册时间”等等。
   - 电子购物的业务场景中，通过用户-商品的二部图描述。
 - 非显式图 Graph Constructed from Non-relational Data
 
 1.4 图数据深度学习
 - 谱图理论(Spectral Graph Theory)
 - GNN 
 - 图数据相关任务的分类
   - 节点层面的任务：包括分类任务和回归任务。工业界在线社交网络中用户标签的分类、恶意账户检测等。
   - 边层面的任务：边的分类指对边的性质进行预测；边预测指给定的两个节点之间是否会构成边。工业界通过边预测实现社交网络推荐。
   - 图层面的任务：从图的整体结构出发，主要应用在自然科学领域。

4 图嵌入 Graph Embedding

## 社区发现 Community Detection Algorithms

- 图分割、图聚类、节点表达、广义社区发现

**定义**：同一社区内的节点与节点之间关系紧密，社区与社区之间的关系稀疏。

**社区算法的种类**
- 凝聚法(Agglomerative Methods): 从强到弱将边一条一条添加到仅包含节点的图中。
- 分裂法(Divisive Methods)：从弱到强一条一条地去除子图中的边。

### 基本算法

**[Girvan Newman Algorithm (GN算法, 2003)](https://arxiv.org/pdf/cond-mat/0308217.pdf)**

- 在一个网络之中，经过社区内部的边的最短路径相对较少，而经过社区之间的边的最短路径的数目则相对较多。GN算法基于betweenness进行社区分割。

**[Walktrap Algorithm (随机游走算法, 2005)](https://www-complexnetworks.lip6.fr/~latapy/Publis/communities.pdf)**

- 社区为相对稠密的子图，因此在图中进行随机游走时较容易陷入trap社区中。随机游走过程中，网络图中每个节点表明一种状态，不同状态之间存在，表示t时刻从状态i转移到状态j的概率。

**[Label Propagation Algorithm (标签传播算法, 2002)](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.14.3864&rep=rep1&type=pdf)**

- 类似的数据应该具备相同的标签。LPA用已标记节点的标签信息去预测未标记节点的标签信息。

**Speaker-listener Label Propagation Algorithm (SLPA)**

- 当一个节点观察到有非常多一样的标签时，很有可能这个节点属于这个社区，而且在传播过程中也很有可能将这个标签传播给别的节点。

### 进阶算法

GN算法、随即游走算法和LPA算法都没有一个明确的量化指标衡量算法对社区划分的好坏。当图中有一些异常的节点或者特殊的节点时，将不断产生震荡，导致算法难以收敛。

**[Louvain Algorithm](https://arxiv.org/pdf/0803.0476.pdf)**

- 基于Modularity模块度。模块度Q的定义可以简单理解为社区内部所有边权重和减去与社区相连的边权重和。

**[Leiden Algorithm](https://www.nature.com/articles/s41598-019-41695-z.pdf)**

- 基于Louvain算法，将节点移动改为节点的本地移动。Louvain算法对于本社区内的每一个顶点都尝试和其他所有社区进行模块度计算，而Leidian算法只针对不稳定点和它直接相连的社区进行模块度计算。

 **社团划分结果评估指标：Q、ARI、NMI**
 
 - 模块度Q(Modularity)
 - 兰德指数ARI(Adjusted Rand Index)
 - 标准化互信息NMI(Normalized Mutual Information)


**相关资料**
[社区发现的经典方法](https://www.zhihu.com/question/29042018)


### 图的拉普拉斯矩阵


1. 拉普拉斯矩阵

- 邻接矩阵A
- 度矩阵D
- 拉普拉斯矩阵L = D - A
<img width="400" alt="image" src="https://user-images.githubusercontent.com/46979228/177009507-0445afa9-a852-4bb2-bffe-8ea3f3bda307.png">

给定了图拉普拉斯矩阵,可以得到图中任意节点的经过拉普拉斯矩阵聚合后的结果：LX = (D - A)X

<img width="451" alt="image" src="https://user-images.githubusercontent.com/46979228/179116244-c6f8b07b-1f82-438d-b5a1-9d6398adf527.png">

图信号X经过拉普拉斯矩阵L的二次型是图任意两条边上信号之差的平方和。图中任意的一条边，都可以表示成(xi - xj)^2的形式，在图信号处理中，将XLX看做为图信号的总变差, 其物理含义为图上各边上信号差值的平方和，刻画了整体信号的平滑度。

2. 加权聚合

如果将归一化的拉普拉斯矩阵作用在图上，即：

<img width="284" alt="image" src="https://user-images.githubusercontent.com/46979228/179116548-df707334-c210-4ef9-829c-1967d7f91017.png">

对节点的一阶邻居信息的加权聚合，权重与节点的度成反比。

3. 拉普拉斯矩阵特征分解

拉普拉斯矩阵L是一个实对称矩阵，由于实对称矩阵可以被正交对角化：

<img width="318" alt="image" src="https://user-images.githubusercontent.com/46979228/179117130-b6cad0e4-50dd-468e-a0f3-a31db5b5793c.png">

特征值反映了特征向量的平滑度，值越小代表对应的特征向量变化越平缓，取值差异不明显；


### 图卷积神经网络

**Spectral CNN**

Spectral CNN的计算依赖于拉普拉斯矩阵分解，导致卷积核不是局部化的，可以理解为一个节点的信息聚合不是来自于其邻居，而是所有节点；

**ChebyNet**

**GCN**

<img width="294" alt="image" src="https://user-images.githubusercontent.com/46979228/179118124-79997e23-4d15-49d4-848d-374ecae0ac95.png">











