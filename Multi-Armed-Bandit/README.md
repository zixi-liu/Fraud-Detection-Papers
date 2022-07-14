## Bandit算法学习笔记

- [Bandit算法与推荐系统](https://zhuanlan.zhihu.com/p/80261581)

在推荐系统中Bandit算法通常用于冷启动和Exploration and Exploitation(EE)问题。
- 冷启动问题即当新用户或新商品出现时，系统中缺少他们的交互数据，从而对兴趣推荐造成困扰；
- EE问题中，Exploration利用用户的历史行为发掘用户兴趣，Exploration指对用户潜在兴趣进行探索。

通常使用累积遗憾 (regret) 来衡量不同 Bandit 算法在解决多臂问题上的效果。

### 经典 Bandit 算法

**朴素Bandit算法**

**Epsilon-Greedy算法**

**Thompson sampling算法**

**UCB算法**
