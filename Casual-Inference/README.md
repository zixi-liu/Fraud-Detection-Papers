## 因果推断 Casual Inference

**Resources:** 
- [Casual Inference Course, Brady Neal](https://www.bradyneal.com/causal-inference-course)
- [因果推断原理、框架和工具学习资源合集](https://zhuanlan.zhihu.com/p/463459303)

### 1. 因果推断的基本问题及假设

- Average Treatment Effects (ATE)

ATE is not equal to associational difference due to confounding.

Causal structure of X confounding the effect of T on Y:

<img width="200" alt="image" src="https://user-images.githubusercontent.com/46979228/177358622-b8965a66-8d2d-4efa-b1df-37d2562ef488.png">

- Ignorability & Exchangeability

  - **Ignorability:** ignoring how people ended up selecting the treatment they selected and just assuming they were randomly assigned their treatment;
  - **Exchangeability:** the treatment groups are the same in all relevant aspects other than the treatment;

假设potential outcome Y(t=1),Y(t=0)和treatment独立。这个假设使我们能够将ATE简化为associational diﬀerence。

Causal structure when the treatment assignment mechanism is ignorable:

<img width="200" alt="image" src="https://user-images.githubusercontent.com/46979228/177359898-fc83740b-67c3-4c0a-9d16-a57328aa3570.png">

- Conditional Exchangeability and Unconfoundedness

  - Although the treatment and potential outcomes may be unconditionally associated (due to confounding), within levels of X, they are not associated. In other words, there is no confounding within levels of X because controlling for X has made the treatment groups comparable.

- Positivity/Overlap and Extrapolation
  - Positivity is the condition that all subgroups of the data with diﬀerent covariates have some probability of receiving any value of treatment.
  - **The Positivity-Unconfoundedness Tradeoff:** 尽管condition on更多的covariate可能会有更高的机率满足unconfoundedness，但同样会有更大的机率违反Positivity。 随着我们增加covariate的数量，每个subgroup越来越小，整个subgroup得到同样treatment的可能性越来越高。
  - **Extrapolation:** Violations of the positivity assumption can actually lead to demanding too much from models and getting very bad behavior in return.

- No interference, Consistency, and SUTVA
  - No interference指的是每个个体的potential outcome只和当前这个个体所接受的treatment有关，和其他个体的treatment无关。
  - Consistency一致性指的是，如果观察到的treatment T=t，观察的结果Y 实际上是T=t的potential outcome--Y(t)。

**Identification-Estimation Flowchart**

The process of moving from a target causal estimand to a corresponding estimate, through identification and estimation.

<img width="500" alt="image" src="https://user-images.githubusercontent.com/46979228/177364391-781025e7-4a40-4dd7-99ff-f923adf29741.png">

- **Causal estimand** refer to any estimand that contains a *potential outcome* in it. 
- **Statistical estimand** denote the complement: any estimand that does not contain a *potential outcome*.

We often use model-assisted estimators (e.g. linear regression etc.) in place of the conditional expectations E[Y | T=t, X=x].

### 2. 因果图与关联图

**贝叶斯网络**

贝叶斯网络（拓扑结构是有向无环图模型）是模拟因果关系的不确定性处理模型。

联合概率分布可以通过chain rule写成如下形式：

<img width="300" alt="image" src="https://user-images.githubusercontent.com/46979228/177662302-860a2d3e-7526-4aee-8262-72351f48e584.png">

但是如果直接对上面公式建模的话，参数数量会爆炸，所以我们只model local dependencies， 即P(x4|x3, x2, x1)写成P(x4|x3)。

<img width="251" alt="image" src="https://user-images.githubusercontent.com/46979228/177662505-c27e6c6b-6b7d-4844-bbc5-31334ad12974.png">

**Local Markov Assumption：** Given its parents in the DAG, a node - is independent of all its non-descendants.

**因的定义：**
- 如果我们把Y的所有直接原因ﬁx，那么改变Y的任何其他原因都不会引起Y的任何变化。DAG中，假设所有的父节点都是他们子节点的原因。

**基本结构**

- Chain链式
- Fork叉子
- Immoralities对撞

<img width="434" alt="image" src="https://user-images.githubusercontent.com/46979228/177792068-668b7aeb-c86d-4c38-bb2c-26581aac9ef4.png">

**链&叉子结构**

- 相关性：关联流(associate flow)是对称的，因果流是非对称的，只能沿着有向边流动。
- 独立性：如果condition on X2，X1与X3的相关性会被阻断变得独立。

**对撞结构**

- 相关性：如果condition on X2，X1与X3从独立变得相关。

**D-分离**

D-Separation是一种用来判断变量是否条件独立的图形化方法。

**因果流与关联流**

关联流沿着unblock path流动，因果流沿着有向边流动。

关联分为因果关联(causal association)与非因果关联(i.e. confounding association)。

### 3. 因果模型

**Do算子与干预分布**

do算子表示干预操作。Conditioning条件与Intervening干预的区别：

<img width="426" alt="image" src="https://user-images.githubusercontent.com/46979228/177797696-1290b094-b044-4596-a857-ed64f54fa9ee.png">




















