## Model Evaluation 风控模型评估常用指标

[**模型评估指标基础**](https://zhuanlan.zhihu.com/p/353384266)

[**模型评估指标进阶**](https://zhuanlan.zhihu.com/p/355335193)

ROC、K-S 曲线、Lift 曲线、PR 曲线

<img width="461" alt="image" src="https://user-images.githubusercontent.com/46979228/178168402-ed92010c-5f43-42e6-b4af-dd62df75694b.png">


**模型可解释性综述**
- [[Tencent] 机器学习模型可解释性](https://zhuanlan.zhihu.com/p/92655819)

### Lift Analysis

Lift衡量的是与不利用模型相比，模型的预测能力 “变好” 了多少。

<img width="297" alt="image" src="https://user-images.githubusercontent.com/46979228/178166372-d621a19e-0d70-4739-9eac-fca99057a55c.png">

- 在不使用模型的情况下，我们用先验概率估计正例的比例，即上式分母部分，以此作为正例的命中率；
- 利用模型后，不需要从整个样本中来挑选正例，只需要从预测为正例的样本子集中挑选正例计算命中率，后者除以前者即可得提升值Lift。

举一个Churn Model的例子：

lift = ( predicted churn rate / average churn rate )
- 假设用户可以取消订阅(Churn = 1)或维持订阅(Churn = 0)，将预测用户Churn的分数(0-1)分十分位：0.0-0.1，0.1-0.2，...，0.9-1.0。
- 计算每一组的true churn rate， 并除以每组客户的人数。

### KS曲线（Kolmogorov-Smirnov Curve）

KS = max(TPR - FPR) 

KS曲线横轴为不同的分类阈值，纵轴为真正率（TPr）和假正率（FPr）的变化曲线。KS值越大表示模型的区分能力越强。

### Precision-Recall (P-R曲线）

P-R曲线刻画查准率和查全率（召回率）之间的关系，查准率指的是在所有预测为正例的数据中，真正例所占的比例，查全率是指预测为真正例的数据占所有正例数据的比例。更常用的是平衡点或者是F1值。

Precision
- 预测为正样本的样本中实际有多少正样本；

Recall
- 描述实际正样本中有多少被预测为正样本；

### ROC曲线

不同分类阈值情况下真正率（TPr）和假正率（FPr）的变化曲线。

当正负样本分布发生变化的时候，ROC曲线的形状能够基本保持不变，而PR曲线的形状会发生较剧烈的变化。

为了使得ROC曲线之间能更好的进行比较，通常采用AUC，即ROC曲线下的面积来衡量一个分类算法的性能。

### Cumulative Gains Chart

横坐标代表样本的百分比，假设有10000个样本，0.1代表1000个，1代表10000个样本。

纵坐标代表横轴所代表的那么多样本中，判断正确的比率。

baseline表示如果我们不用模型，那我们对每一个人的打分都是一样的，正率在所有样本空间都是一样的，连接起来就成为一条直线。

曲线表示采用模型进行预测。y值的分子代表模型预测且预测为正例的人数，分母是整个群体正例人数。

### SHAP

一个特征的shapley value是该特征在所有的特征序列中的平均边际贡献。也可以用Shap值识别特征交叉。

- [[SHAP] A Unified Approach to Interpreting Model Predictions](https://proceedings.neurips.cc/paper/2017/file/8a20a8621978632d76c43dfd28b67767-Paper.pdf)
- [One Feature Attribution Method to (Supposedly) Rule Them All: Shapley Values](https://towardsdatascience.com/one-feature-attribution-method-to-supposedly-rule-them-all-shapley-values-f3e04534983d)
