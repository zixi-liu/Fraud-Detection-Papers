## Casual Inference

**Resources:** 
- [Casual Inference Course, Brady Neal](https://www.bradyneal.com/causal-inference-course)
- [因果推断原理、框架和工具学习资源合集](https://zhuanlan.zhihu.com/p/463459303)

#### 1. 因果推断的基本问题及假设

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

  - Although the treatment and potential outcomes may be unconditionally associated (due to confounding), within levels of -, they are not associated. In other words, there is no confounding within levels of X because controlling for X has made the treatment groups comparable.
