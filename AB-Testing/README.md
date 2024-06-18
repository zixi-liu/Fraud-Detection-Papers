## A/B Testing

- [[**Lyft Engineering 2017**] Interactions in fraud experiments: A case study in multivariable testing](https://eng.lyft.com/interactions-in-fraud-experiments-a-case-study-in-multivariable-testing-e0525b11751)
  - auth decreases fraud exposure, but increases passenger churn
  - user churn increase with increased auth frequency
- [[**Feedzai 2023**] On the Importance of Application-Grounded Experimental Design for Evaluating Explainable Machine Learning Methods](https://arxiv.org/pdf/2206.13503)
- [[**Feedzai 2024**] On the Importance of Application-Grounded Experimental Design for Evaluating Explainable ML Methods](https://ojs.aaai.org/index.php/AAAI/article/view/30082/31906)
  - use performance metrics that reflect operational goals such as Percent Dollar Regret (PDR)




## Platform-wise
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


