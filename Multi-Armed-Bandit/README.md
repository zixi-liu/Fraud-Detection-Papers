## Bandit算法学习笔记

MAB（multi-arm bandit）是强化学习(reinforcement learning)框架下的一个特例。
- [通俗解释Bandit算法](https://www.zhihu.com/question/53381093)
- [Bandit算法与推荐系统](https://zhuanlan.zhihu.com/p/80261581)
- [在线学习(MAB)与强化学习(RL)](https://zhuanlan.zhihu.com/p/52727881)

在推荐系统中Bandit算法通常用于冷启动和Exploration and Exploitation(EE)问题。
- 冷启动问题即当新用户或新商品出现时，系统中缺少他们的交互数据，从而对兴趣推荐造成困扰；
- EE问题中，Exploitation利用用户的历史行为发掘用户兴趣，Exploration指对用户潜在兴趣进行探索。

通常使用累积遗憾 (regret) 来衡量不同 Bandit 算法在解决多臂问题上的效果。对同样的多臂问题，用不同的bandit算法试验相同次数，看看谁的regret增长得慢。

### 经典 Bandit 算法

**朴素Bandit算法**
- 每个臂都有了均值之后，一直选均值最大那个臂。

**Epsilon-Greedy算法**
- 选一个(0,1)之间较小的数epsilon。每次以概率epsilon（产生一个[0,1]之间的随机数，比epsilon小）做一件事：所有臂中随机选一个。否则，选择截止当前，平均收益最大的那个臂。

**Thompson sampling算法**
- 假设每个臂是否产生收益，其背后有一个概率分布，产生收益的概率为p。估计出一个置信度较高的概率p的概率分布近似解决这个问题。

**UCB算法**
- Upper Confidence Bound(置信区间上界)
- <img width="150" alt="image" src="https://user-images.githubusercontent.com/46979228/185758059-54a834b3-de47-4d60-9335-5968eacc6b32.png">
- 加号前面是这个臂到目前的收益均值，后面的叫做bonus，本质上是均值的标准差，t是目前的试验次数，Tjt是这个臂被试次数。
- 均值越大，标准差越小，被选中的概率会越来越大，起到了exploit的作用；同时哪些被选次数较少的臂也会得到试验机会，起到了explore的作用。

### Multi-Armed Bandit 与 Payment Routing
