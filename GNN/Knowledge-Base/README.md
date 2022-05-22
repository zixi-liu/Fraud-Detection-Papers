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

