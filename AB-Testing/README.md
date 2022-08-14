## A/B Testing

随机对照试验 RCT
- 在线上流量中取出一小部分用户（较低风险），完全随机地分给原策略A和新策略B（排除干扰），再结合一定的统计方法，得到两种策略对比效果的准确估计。

**字节跳动A/B测试实验平台**

<img width="971" alt="image" src="https://user-images.githubusercontent.com/46979228/184524694-3a3019d0-5f6b-421a-b9b6-01e4a71b6492.png">

**统计原理与技术实现**

分流，流量复用与隔离
- 哈希保证层内流量互斥，层间流露正交，流量轮转，Time Window轮转

统计分析
- 假设检验
- Seed finder, Diff in Diff, CUPED (Controlled-experiment using pre-experiment data)

### Econometrics：计量经济学
