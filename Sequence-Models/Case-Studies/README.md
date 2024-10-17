
## Linkedin - Using Deep Learning to Detect Abusive Sequences of Member Activity

[Using Deep Learning to Detect Abusive Sequences of Member Activity on LinkedIn](https://exchange.scale.com/public/videos/using-deep-learning-to-detect-abusive-sequences-of-member-activity-on-linkedin)

**Challenges in Anti-Abuse**

- Many Surfaces (across a diverse set of product surfaces)
- Maximizing signal (need to maximally leverage available signal in the data)
  - Sequence modeling leverages subtle patterns in the ordering and timing of user requests
- Adversarial (attacks are quick to adapt and evolve)
- Pool labels
- Unbalanced data
- Need to take action quickly

**Scaping** 
- scraping refers to the use of bots or other tools to copy data from Linkedin in automated fashion
  - Erosion of member trust
  - Wasted resources

**Activity Sequence Data**
- 1) Normalize request paths
- 2) Map to integers based upon frequency

![image](https://github.com/user-attachments/assets/0e3d54c7-1421-4159-8be4-66e9ff0f47bf)

- Use the LSTM model

**Training Labels**
- Created using unsupervised outlier detection (isolation forest)
- Can be augmented with labels from other sources

**Activity Sequence Embeddings**
- Clustering
- Outlier Detection

## Airbnb - What we're doing to prevent fake listing scams

[What we're doing to prevent fake listing scams](https://news.airbnb.com/what-were-doing-to-prevent-fake-listing-scams/)

Case Study
- First, the fraudster needs to bypass our defenses and upload photos of either someone else’s listing or of a listing that does not actually exist.
- Next, if they manage to slip through, the scammer then has to convince you to communicate with them off of the Airbnb website or app. They do this by giving you their personal contact information in order to lure you into paying them directly and taking off with your money.
- Finally, they still need to actually convince you to send them money directly, instead of receiving payment as usual through our secure payment system on Airbnb. Scammers may say they need you to wire or transfer them money directly due to a problem with the platform or send you to a fake Airbnb payment site.

Solutions to combat fraud
- **Leveraging machine learning technology:** Our technology evaluates each listing against hundreds of risk signals such as host reputation, template messaging, duplicate photos and other discrepancies — using data learnings from millions of listings. When we predict a high likelihood that a listing is fake, we automatically block it from appearing on Airbnb or, in other cases, delay the listing from going live while we conduct additional reviews.
- **Keeping personal contact info off of the site:** In listing descriptions, house rules, and messages between guests and hosts, our system automatically screens out phone numbers, email addresses, and other personal information until a reservation has been booked. We also detect text within listing images to prevent fraudsters from slipping contact details in them.
- **Safeguarding your payment.** We do not release your money to your host until after check-in. This gives both parties time to make sure that everything is as expected. This security measure forces fraudsters to have to convince you to transact off of Airbnb in order to accomplish their scam.
- **User flagging capabilities.** Users can now flag suspicious listings on their mobile devices. These flags are fed directly into our risk model to reevaluate whether a listing should be automatically removed or manually reviewed.

## Alipay

### Modeling Users’ Behavior Sequences with Hierarchical Explainable Network for Cross-domain Fraud Detection

[Modeling Users’ Behavior Sequences with Hierarchical Explainable Network for Cross-domain Fraud Detection](https://arxiv.org/pdf/2201.01004)

[Sequence As Genes: An User Behavior Modeling Framework for Fraud Transaction Detection in E-commerce](https://dl.acm.org/doi/pdf/10.1145/3580305.3599905)

## Fake News Detection

[虚假新闻检测概述](https://blog.csdn.net/m0_51474171/article/details/126708654)
