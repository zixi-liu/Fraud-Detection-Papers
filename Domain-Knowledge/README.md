
## 目录

- [《支付方法论》阅读笔记](#《支付方法论》阅读笔记)

## Industry Applications 业界案例

**Anti-Abuse AI Team @Linkedin**

[Using deep learning to detect abusive sequences of member activity](https://engineering.linkedin.com/blog/2021/using-deep-learning-to-detect-abusive-sequences-of-member-activi)


[Abstract] The Anti-Abuse AI Team at LinkedIn creates, deploys, and maintains models that detect and prevent many types of abuse, including the creation of fake accounts, member profile scraping, automated spam, and account takeovers. Bad actors use automation to scale their attempted abuse. There are many unique challenges associated with using machine learning to stop abuse on a large professional network including maximizing signal, keeping up with adversarial attackers, and covering many heterogeneous attack surfaces. In addition, traditional machine learning models require hand-engineered features that are often specific to a particular type of abuse and attack surface. To address these challenges, we have productionalized a deep learning model that operates directly on raw sequences of member activity, allowing us to scalably leverage more of the available signal hidden in the data and stop adversarial attacks more effectively. Our first production use case of this model was the detection of logged-in accounts scraping member profile data. We will present results demonstrating the promise of this modeling approach and discuss how it helps to solve many of the unique challenges in the anti-abuse domain.

## Payments and Fraud Prevention 支付与反欺诈


### 《支付方法论》阅读笔记

1、支付的基本概念

1.1 支付的三个基本过程：交易、清分、和结算。
- 交易的重要性：拓展交易场景
  - 确保支付指令的生成、确认与传输。包括交易主体的合法性和身份确认、支付方式确认、支付通道的计算与决策、支付能力查证、交易结果的存储与返回信息归类等等。
- 清分(Clearing)：算出债权人与债务人各自应收应付，并没有发生实际交割。
- 结算(Settlement)：资产交割。

*“支付是交易的终点，是货币流动的起点。”*


### Overview of Payment Technology 支付技术总结

Magnetic Stripe Card 磁条卡
- Static data programmed onto card at issuance. 
  - Data contains Primary Account Number (PAN), Expiry Date, and Usage Controls.
  
Smart Cards
- Card with Integrated Circuit (ICC)
  - Contains secret keys and PINs, cryptographic use for proof of use, and can talk to outside world.
- EMV card (card with embedded microchips) transaction flow
  - Select application -> read card data -> terminal decision -> card decision [online authorization] -> complete [issuer scripting]

Contactless Payments
- EMV card with antenna
  - Faster transactions <500ms

Mobile Payments 
- Near-field Communication (NFC)
  - Tokenization.
  - Card date can be used to make "in-app" purchases.

Peer-to-Peer Payments 
- Money transfered directly from one account to another.
  - Using networks such as Paypal or Venmo.
  - Using direct bank-to-bank method like Zelle.
  
Alternative Payments 
- QR codes or 2D barcodes

### Payments Transaction Routing

*Implementing the right local payment method is a real lever for conversion.*

Payment routing is a payment processing feature for businesses working with multiple payment providers. It allows sending each transaction to the optimal payment gateway based on selected parameters.

**Why Card Decline Happens?**

A card decline occurs when the card is unable to be processed, which can happen at several points in the transaction process. Card declines happen for different reasons and many of these reasons are preventable by using services like Account Updater to keep card information up to date. 

**Popular Online Payment Methods**
- Credit/Debit Cards
- ACH Payments (Automated Clearing House): the electronic funds transfer in batches, considered the most secure mode of the online and automated recurring payment, processed in two to three working days.
  - Direct Deposits: The ACH Direct Deposits can be made using Paychecks, Government Benefits, Tax Refunds, Interest Payments, and others.
  - Direct Payments: Paying a bill online, sending money from one bank account to another, sending payments via PayPal, Stripe, Braintree, and other social payment apps, and more are the prime examples of ACH Payments.
- Digital Wallets: Digital wallets do not require a bank account with a physical branch. They enable wider financial inclusion. Digital Wallets can also process digital or cryptocurrencies. Some of the payment services providers also serve as payment aggregators and offer merchant’s accounts.
- Mobile Payments: Mobile Wallet service allows its users to store digital cash on their phones. Some of the leading examples of mobile payments are Apple Pay, Samsung Pay, Ali Pay, Google Pay, Amazon Pay, and some others.
- Wire Transfers: Most costly, unsafe, undisputable, but faster and instant way to make recurring payments when they are international. With the rise of digital wallets and mobile payments, wire transfer is not as effective and efficient as it was considered earlier.

**Payment Gateway**
- An interface between the merchant's website and acquirer. Card and transaction details are collected and stored on the secure surface of payment gateway. Once the payment confirmed by card schemes, payment gateway sends transaction back to merchant's website.
  - Authorization
  - Settlement
  - Security (Protocols, Signatures, PCI DSS, Multi-factor Authorization, Tokenizations)
  - Bin-based Routing
  
**Static Routing**
- Manually configured system that is pre-defined for the customers. 

**Dynamic Routing**
- Select the best route based on multiple parameters, such as card issuer/type/brand, auth mode (CVV/3DS), geolocation, store, currency, amount, date & time, metadata, and other payment routing data.
 
[Awesome Talk on Payment Transaction Routing at LinkedIn](https://www.youtube.com/watch?v=afs6CnU6qtk)

Payments Transaction Routing Flow
- Intent to order
- Intent to order confirmed
- Orders Approved

Member -> Order -> Payment Service Provider (Payment Gateway, Payment Processors, Acquirers) -> Payment Networks -> Issuers

**Approval Rate = Orders Approved / Intent to order confirmed**

### Payment KPIs

**Must-Have KPIs include:**
- Authorization rate: allows merchants to see the performance of card payments (that require a real-time approval from the card issuer) and whether payments are proceeding successfully. 
- Conversion rate: percentage of unique visitors that are able to pay and complete their purchase. 
- Fraud rate: monitors fraudulent transactions.
- Chargeback rate: chargebacks happen for multiple reasons (including fraud) when a customer contacts their card issuer to request a refund.
- Total cost per transaction: many merchants find they need to assess the cost of accepting payment.

**Advanced KPIs include:**

Advanced authorization rates: 
- Authorization rate by country (location of buyer and/or of merchant)
- Authorization rate per PSP
- Authorization rate per issuer and/or acquirer
- Authorization rate across other dimensions such as the device used by the consumer, whether there has been a retry via another acquirer, whether another form of payment is used after an initial decline, etc.
- Authorization rate per authentication method (3D Secure version 1, 3D Secure version 2, non-authenticated transaction, by-pass authentication, eligible to exemptions)
- Abandonment rate / drop-off rate with 3D Secure

Decline rate per issuer and by reason code
- [WorldPay - Payment Transaction Response Codes](http://support.worldpay.com/support/CNP-API/content/paytransrespcodes.htm)
- [WorldPay - 3DS Authentication Result Codes](http://support.worldpay.com/support/CNP-API/content/3dsauthrescodes.htm)

Capture rate: (percentage of authorized transactions that are captured) enables merchants to identify if all authorized transactions are eventually sent for settlement. An authorization can be captured or cancelled for several reasons, such as fraud or product shortage.

False positive rate: an important KPI that tracks genuine transactions made by a real client, but which is declined due to suspicion of fraud. 

**Emerging KPIs include:**
- Incremental sales via A/B testing: the ability of payment to generate incremental sales is typically hard to measure.
- Token management: more and more merchants are enabling omnichannel use cases, and leverage the tokenization of customer’s payment data. It enables merchants to follow spending per sales channel and set up strategies to drive a customer from one channel to another.

**How to use KPIs to optimize payment?**
- authorization rate
  - Improvement of authorization rates through BIN analysis can be a very useful tool. It allows merchants to identify with which issuer they encounter difficulties and directly engage with them (or via their PSP / acquirer) to discuss areas of improvement. 
- fraud rate
- cost of payment acceptance
  - For instance, some merchants implemented a surcharging policy (in countries where it is allowed) or ‘promoted’ alternative payment methods in specific
countries.

*Robust fraud prevention solutions are built mainly by researchers who can explain the fraud from the perspectives of the attacker and the victim.*


### [O'Reilly] Practical Fraud Prevention 📖

**前言**

一点Fraud的发展历史：早期的信用卡欺诈形式主要是磁条侧录盗刷(Card Skimming)或者收银员窃取信用卡号和密码。但随着Card Chip和PIN的技术发展，card-not-present fraud逐渐成为主流。

![image](https://user-images.githubusercontent.com/46979228/182518512-e6c7c2b9-c54a-45b8-ae7c-8b05724bbede.png)

Why event-based historical data?

- **Point-in-time analysis** (e.g., being able to train a predictive system using only data that was available at the time of the fraud attack, long before the financial loss became evident)

## 一、欺诈分析 Fraud Analytics

### 1. Fraudster Traits 黑产的一些特点 🥷

Impersonation Techniques 黑产伪装手段
- Fraudsters pretend to be someone else,
  - Device ID and behavioral info are harder to spoof unless the attack is carried out with malware used to skim the info from live visitors.
  - Emails & Phone numbers: fraudster steal account or use disposable SIM cards that match whereever victim lives.
  - Physical Orders: order and then change adddress or click-and-collect option pose challenges. 
  - Address verification service (AVS) spoofing.
- Fraudsters pretend to be completely fresh,
- [Friendly Fraudster] using own identity and plan to file a fraudulent chargeback.


Deception Techniques 常见的欺诈手段
- IP masking
- Social Engineering: the fraudster becomes a puppeteer (i.e., puppet master, not the headless chrome node, although some fraudsters do favor it). The victim—being the puppet—waltzes through the checkout process with their own email, IP, device, and so on. 
- Fraud Ring

Volatility 黑产攻击的波动性
- Rules must be adjusted for different times of the year, 
- Machine learning systems must be able to scale quickly as necessary, 
- Manual review teams must be prepared and ramped up for busy times of the year.
- Volatility is very difficult to prepare for from the machine learning/artificial intelligence perspective. It's important to carry out continual assessments during volatile times in order to make changes as necessary on the fly.

Card and Account Testing 信用卡测试
- Fraudsters attempt small purchases on an unsuspecting merchant’s site to see if the stolen card was approved.
- When businesses experience a large number of authorizations and a high authorization decline rate, this may be an indicator that fraudsters have successfully submitted orders.

Abuse Versus Fraud 羊毛党🐏vs欺诈风险
- Promo abuse 
- Account creation
- Content abuse, or review abuse
- Click fraud

Money Laundering and Compliance Violations 洗钱行为
- Turn cryptocurrency into other forms of currency.

### 4. Fraud Prevention Evaluation and Investment

Types of Fraud Prevention Solutions
- Rules Engines
- Machine Learning
  - “adapt quickly to big new fraud tricks”
- Hybrid Systems
- Data Enrichment Tools
  - BioCatch started by collecting behavioral biometric data such as mouse motion, typing patterns, and the way one holds and operates a mobile device. When you control someone else’s device remotely over the internet, your hand–eye coordination gets awkward and delayed due to latency; given sufficiently sensitive behavioral analytics, it can be immediately detected.
- Privacy-enhancing Technology 

Measuring Loss and Impact
- Number of fraud chargebacks received - it’s crucial to stay well below the chargeback thresholds set by the card companies, with a comfortable margin of error.
- False positives
- Benchmarking against industry averages

Important Metrics
- Fraud rate, or the number of attacks you’re seeing as a percentage of overall transactions or activities. Break this down into types of attack.
- The number of fraudulent attempts you stop, both as a percentage of the total number of attacks and in dollar value.
- The exposure dollar amount versus the actual losses.
- Chargeback rate
- Successful chargeback dispute rate
- Manual review rate
- Percentage of manually reviewed cases that are approved
- The average speed of manual review.
- Account-level abuses such as coupon abuse, wire fraud losses, peer-to-peer (P2P) fraud losses, fake reviews, and more that harm the business’s bottom line and/or reputation.


### 5. Machine Learning and Fraud Model

Advantages ML模型的优势
- Scale, Subtlety, Diversity, Adaptability, Load variance, Pattern recognition

Challenges ML模型的挑战
- Relative Paucity of Data
- Delayed Feedback and Overfitting 
  - Might lead to false positives
- The Labeled Data Difficulty
- Intelligent Adversary
- Explainability, Ethics, and Bias

Dynamic Policies and the Merits of Story-Based Models
- It takes policy considerations, often backed with a set of policy rules, to set the threshold.
  - When a business tries to expand into a new region or audience, or when sales are spiking during the holidays, you may want to penetrate the market and accept more fraud.
  - On the positive side, dynamic business can yield control groups.
- Story-based models

Some Best Practices 
- Labeling 黑产标注
  - Fraudsters change their behavior frequently, and friendly fraud causes terrible noise.
  - For example, imagine a classifier aiming to predict fraud but trained on a mix of ATO and account-opening fraud; the results would be far from optimal.
- Featuring 特征工程
  - Sanity-check the features, predict significant codependencies, and uncover complex features (such as IP types) that can represent significant informational gain for the model.


Popular Machine Learning Approaches
- Accuracy Versus Explainability and Predictability
- Precision refers to how often the transactions you reject are in fact true positives; that is, they really are fraud. 
- Recall is telling you how much of the fraud attacking your business your team manages to catch.

## II. Ecommerce Fraud Analytics 电商欺诈分析 🛍️

### 6. Stolen Credit Card Fraud 信用卡欺诈

**Defining Stolen Credit Card Fraud**
- An attacker already has the compromised credentials (credit card number, expiration date, name on card, CVV) and they are attempting to purchase goods or sign up to a service in order to monetize those stolen details.

**Email Analysis**
- Aged email: an email created by a fraudster, often including a username to match a specific victim’s identity, which is then left alone to “age” for a period of time before the attack.
- Spoofed/hacked email: the true email of the victim that has been hacked/breached by the fraudster.
- Email mismatch: Fraudsters may use their own email or a disposable email address for the purpose of an attack.

**Modus Operandi 作案手法 👿**

Fraudsters need to prepare:
- A clean device that has no cookies to tie it to previous attacks, nor any fraud-related software/apps/plug-ins installed.
- Device settings to match the profile of the cardholder.
- An IP provider + geolocation to match the victim’s alleged lifestyle.
- Browsing and behavioral patterns tailored to match the victim’s alleged lifestyle (this includes time zone, language, browser history, referral URL, and browsing speed)

During checkout the fraudster will provide:
- Cardholder name and billing/shipping address.
- Contact email. Fraudsters would go for a recently generated email (or a spoofed email of another victim), preferably one with a handle name similar to the cardholder’s name.
- Contact phone. Fraudsters would provide bogus info and/or Voice over IP (VoIP)/disposable/public phone numbers that would match the geography of the cardholder.

**Identification 欺诈识别**

IP fraud identification - what should qualify as suspicious IP behavior？

**Everything about IP**
- IP Address
  - Protocols at the Internet layer provide for delivery beyond the local network segment (LAN).
  - The world is switching from 32-bit binary IPv4 addresses to a new 128-bit address system known as IPv6.
  - A logical addressing scheme is maintained by the IP protocol at the Internet layer. The logical address is called the IP address. 
  - Another Internet layer protocol called Address Resolution Protocol (ARP) assembles a table that maps IP addresses to physical addresses. This ARP table is the link between the IP address and the physical address burned into the network adapter card.
- Internet Protocol
  - The Internet Protocol (IP) provides a hierarchical, hardware-independent addressing system and offers the services necessary for delivering data on a complex, routed network. Each network adapter on a TCP/IP network has a unique IP address.
  - Computers with multiple network adapters are also common. A computer that is acting as a router or a proxy server, for instance, must have more than one network adapter and, therefore, has more than one IP address. 
  - IP addresses on the network are organized so that you can tell the location of the host.

**IP masking**

Mismatched IP
- Geolocation/profiling mismatches between the IP connection and the cardholder’s alleged location/profile。
- If we find this IP in a context that does not match the expected activity of this organization, we should suspect that it is being used as a proxy. 
- [互联网黑产剖析——代理和匿名](https://zhuanlan.zhihu.com/p/41544284)

Repeat offender IP
- Significant evidence of the IP being linked to previous attacks.
- IPs are often aggregated in a way that means they represent many users (home connections can be recycled by the ISP, mobile IPs are aggregated to a cell tower level, network address translation [NAT] routers will translate many employees of a corporation into a single IP, etc.).

Nonunique IP
- Significant evidence of attempts to cover the tracks of IPs by using public IPs.
- Looking for the Tor regular expression on the reverse DNS of the IP is worthwhile. 

Masked IP
- Significant evidence of attempts to cover the tracks of IPs by using proxies or VPNs of all sorts.
- Traceroute check allow effectively follow the geographic and IP routes of a packet of data.

Digital mapping services
- Digital mapping services, which translate IPs into geography and Whois/ASN (autonomous system number) data (i.e., registration data).
- A grain of salt: [[Apple’s 2021 Private Relay release]](https://support.apple.com/en-il/HT212614) vs [Maxmind - Data Updates for Apple iCloud Private Relay](https://blog.maxmind.com/2021/09/data-updates-for-apple-icloud-private-relay/)

Mitigation
- Query more than one service for Whois/ASN data. Cross-reference different services against each other, plus do reverse DNS. Along these lines, it’s worth learning about the gethostbyaddr function, for instance, in the DNS/Reverse DNS Lookups section of PHP 5 Unleashed by John Coggeshall (SAMS). 
- Consider metrics such as country/language breakdown, operating system breakdown, number of devices, weekend/night activity, and so on.
- Some examples:
  - Using IP Geolocation to Identify Legitimate Hotel IPs
  - Using IP Traffic Trends to Identify Fake-Hotel IPs
  - Using Hierarchy in Variable Design
  - Using Hierarchy in IP Typology Variable Design
  - If dealing with a fraud ring, consider reversing this hierarchy in an attempt to hunt down all the proxies.
  
### 7. Address Manipulation and Mules 地址欺诈

**Porch Piracy “门廊海盗”**
- Reshippers：Cross-border reshipping or freight forwarding services easily become target;
- AVS Manipulation: AVS system only checks the numbers of an address, not the words.

**Shipping Mules**
- If the fraudster can buy stolen card information for a number of cards, all connected to the same geographic area, and they can find a mule who lives in the right area, they can place plenty of fraudulent purchases that look legitimate, have them all sent to the mule, and then have the mule send them on to wherever is convenient for the fraudster. 

**Adding an Address to the Card**
- Targets the customer support representatives of the credit card’s issuer and persuades them to add their (the fraudster’s) own shipping address to the credit card on file. 

**Triangulation**
- The fraudster collects real payments as "businesses" from their own customers (and in the process, gains their payment information for future fraud) and uses stolen information to place the order with the merchant.

**Identification and Mitigation**



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
