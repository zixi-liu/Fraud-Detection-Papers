
## Payments and Fraud Prevention 

*Robust fraud prevention solutions are built mainly by researchers who can explain the fraud from the perspectives of the attacker and the victim.*


### [O'Reilly] Practical Fraud Prevention

**前言**

一点Fraud的发展历史：早期的信用卡欺诈形式主要是磁条侧录盗刷(Card Skimming)或者收银员窃取信用卡号和密码。但随着Card Chip和PIN的技术发展，card-not-present fraud逐渐成为主流。

![image](https://user-images.githubusercontent.com/46979228/182518512-e6c7c2b9-c54a-45b8-ae7c-8b05724bbede.png)

Why event-based historical data?

- Point-in-time analysis (e.g., being able to train a predictive system using only data that was available at the time of the fraud attack, long before the financial loss became evident)

**一、欺诈分析 Fraud Analytics**

1. Fraud Traits

*You don’t care about what (the IP, address, email, etc.). You care about who.*

Impersonation Techniques
- Fraudsters pretend to be someone else,
  - Device ID and behavioral info are harder to spoof unless the attack is carried out with malware used to skim the info from live visitors.
  - Emails & Phone numbers: fraudster steal account or use disposable SIM cards that match whereever victim lives.
  - Physical Orders: order and then change adddress or click-and-collect option pose challenges. 
  - Address verification service (AVS) spoofing.
- Fraudsters pretend to be completely fresh,
- [Friendly Fraudster] using own identity and plan to file a fraudulent chargeback.



=======================================================================================================
### Merchant Risk Council (MRC) 2022 Global Payments and Fraud Survey Report 

**Executive Summary**

E-commerce fraud

1. [Business Impacts of Fraud] What effect is fraud having on merchant businesses?

- MRC merchants in our survey report *fraud rates* by revenue that are 5 to 8 times lower, *order rejection rates* that are 50 to 60 percent
lower, and *shares of accepted orders* that are fraudulent that are 5 times lower, when compared to non-members.
  - 重点关注在fraud rate, order reject rate, 和shares of accepted order。
  - Reduce Manual Order Review: European merchants and SMBs are significantly more likely to lean in this direction, given that the share
of orders manually screened and the share of screened orders that were subsequently declined due to suspicion of fraud, both decreased across all region and size segments.
- [Payment Regulation System] EU’s Payment Services Directive, specifically involving the implementation of Strong Customer Authentication (known as PSD2 / SCA) and for the implementation of EMV® 3DS.

2. [Range of Fraud Attacks] What types of fraud attacks are merchants experiencing?

- Phishing网络钓鱼/pharming, card testing, identity theft, and first-party misuse remain the most prevalent fraud attacks, each affecting impact around one-third of merchants, globally.
  - First-Party Misuse (chargeback fraud): disputed transactions are the result of cardholders aiming to obtain free goods, confusion about transaction descriptors, or card issuers incorrectly processing general cardholder disputes as fraud (likely due, in part, to incentives issuers have to resolve disputes quickly). For example, Attempt to obtain free goods or services, Transaction or descriptor confusion, Family fraud, Attempt to return goods outside of merchant’s return period, Buyer’s remorse, Quality of goods not as expected.
  - A list of common fraud types:
  - ![image](https://user-images.githubusercontent.com/46979228/182512070-84ae4472-1c4b-42ea-b62e-52fe89276115.png)

- Globally, on average, merchants believe 16% of fraudulent disputes should be attributed to **first-party misuse** (or “friendly fraud”).
- The challenges of identifying and responding to emerging fraud attacks, updating fraud risk models, and effectively managing fraud while expanding into new sales channels have become markedly more difficult for merchants to overcome.

3. [Fraud Prevention Strategies] What strategic and tactical approaches are merchants using to prevent and manage fraud?

- Merchants report using an average of four fraud detection tools and services, in total. 
  - Payment card,
  - Identity verification services,
  - 3D-Secure,
  - Two-factor phone authentication
- Other commonly used tools, such as list management tools (e.g., negative lists / blacklists, positive lists / whitelists), geographic indicators (e.g.,
maps, geo location for country, IP location, etc.), company-specific fraud scoring models, and order velocity monitoring to significantly enhance their ability to detect and thwart incoming fraud attacks.
  - A list of commonly used fraud prevention tools:
  - ![image](https://user-images.githubusercontent.com/46979228/182514217-6eca02d6-e619-48d3-98b0-ed06949aceea.png)


E-commerce payments

4. [Payment Acceptance and Partners] What practices and partners are merchants using to accept eCommerce payments? 

- Most eCommerce merchants accept payments via **digital wallets, direct debit transfers, traditional cards and mCommerce mobile apps (such as PayPal mobile or Amazon one-click)**. Beyond these primary methods, cash is accepted by 45% of merchants, while gift cards and vouchers, third-party payments, and buy-now-pay-later (BNPL) payments are each accepted by around 3 in 10. The vast majority (nearly 9 in 10) encourage customers to pay via preferred methods, mainly to minimize risk of payment fraud, maximizing conversion rates, expediting availability of funds and minimizing processing costs.
- Third-party payments, cryptocurrency, buy now pay later (BNPL), digital wallet, and mobile payments are the fastest growing payment methods.
- Merchants leverage multiple payment processors and acquiring banks to support omnichannel payments. Maximizing flexibility, geographic coverage, uptime,
and authorizations represent merchants’ main motivations for utilizing multiple acquirers.
  - On average, merchants leverage four payment processor connections and three different acquiring banks to support omnichannel payment.

5. [Payment Management] How are merchants optimizing payment processes and platforms?

- Merchants are experimenting with a diverse range of novel retail approaches, such as buy now pay later (or BNPL) and buy online pickup in store (BOPIS), as well as new customer experiences to facilitate payments, like AI chatbots and face-to-pay technologies.
- On average, merchants use 2 to 3 different approaches or techniques to optimize payment authorization. EMV® 3DS (3D Secure 2 usage to improve issuer
approval rate), intelligent payment routing, machine learning (fine-tune fraud management) and automated retries are most common.
  - Sizable shares also leverage account updaters (Reducing failed transactions), tokenization (Real-time card-onfile updates), and dynamic currency conversion.
  - Majority Use Tokenization To Enhance Security, Customer Trust and Authorization Rates: tokenization means the encryption of customer
card numbers, either in the merchant’s own internal databases, or via the merchant’s card network / card issuer / wallet provider payment partners. The most common motivation for employing tokenization is to improve payment security and reduce risk – i.e., protecting customer privacy and reducing the risk of data breaches (robust compliance with Payment Card Industry (PCI) Data Security Standards (DSS) and payment regulations).
- MRC members are more likely to have a sophisticated approach to payment management, with most using tokenization, employing authorization-boosting techniques, and monitoring a larger and wider range of payment KPIs.
  - Payment success rate, revenue, and cost of payments represent the top three KPIs tracked by merchants, globally, followed by authorization, authentication and loss rates.
  - A list of KPIs monitored:
  - ![image](https://user-images.githubusercontent.com/46979228/182515782-f607ac04-46e0-4567-ae3b-7f5071449e0f.png)


### Payments Terminology

**CIT vs MIT**
- CIT (Customer Initiated Transactions)
- MIT (Merchant Initiated Transactions)

**Payment Gateways (pass the Payment Transaction onto the relevant place)**

For Cards, the Payment Gateway passes the transaction onto an Authorisation Platform.

- Adyen
- Paymentech
- Chase Orbital
- Worldpay

**Payment Provider (someone who PROVIDES a Payment Services and helps settle transactions after authorization)**
- Paypal (APM)
- Boku (APM)
  - KakaoPay
  - DCB (Direct Carrier Billing) 

**3DS**
- 3DS Retries are NOT classed as retries.

### Payments Newsletter

- [How does VISA work?](https://blog.bytebytego.com/p/ep15-what-happens-when-you-swipe)


### 团伙挖掘关系类型

- 硬件设备关系
- 互联网关系物理地址
- 社交关系数据
- 通讯录数据
- 地址关系数据
- 资金往来关系
- LBS地址位置数据（GeoHash）
- 文本、图片等内容关系
  - 标题、昵称相似性计算



### 黑产攻击

游戏黑灰产识别与溯源取证

**账号层**
- 批量注册
- 撞库风险
  - 黑产人员利用个人信息数据，主要是账号、密钥对其他网站平台实施批量登陆，通过已知平台破译未知平台，盗取支付账户，或通过电商盗刷账户。
- ATO盗号风险

**流量层**
- 流量攻击、游戏爬虫等。

**设备层**
- 虚拟设备、模拟器、群控软件等。

**业务层**
- 游戏脚本、游戏漏洞挖掘等。
