
## 目录

- [《支付方法论》阅读笔记](#支付方法论-阅读笔记)
- [《产业互联网与在线支付》](#产业互联网-在线支付)
- [《社会工程》阅读笔记](#社会工程-阅读笔记)
- [《货币未来 - 从金本位到区块链》阅读笔记](#货币未来-阅读笔记)
- [《蚂蚁金服》阅读笔记](#蚂蚁金服-阅读笔记)
- [Overview of Payment Technology 支付技术总结](#Overview-of-Payment-Technology-支付技术总结)
- [Payments Transaction Routing](#Payments-Transaction-Routing)
- [Payments Orchestration](#Payments-Orchestration)
- [Payment KPIs](#Payment-KPIs)
- [EMV 3DS](#EMV-3DS)
- [Credit Card Payment Processing Rules and Laws](#Credit-Card-Payment-Processing-Rules-and-Laws)
- [How to Create a Fraud Prevention Unit](#How-to-Create-a-Fraud-Prevention-Unit)
- [Account Takeover](#Account-Takeover)
- [Financial Impacts of Cybercrime](#Financial-Impacts-of-Cybercrime)
- [BNPL Overview](#BNPL-Overview)
- [Crypto Fraud](#Crypto-Fraud)
- [[O'Reilly] Practical Fraud Prevention](#[O'Reilly]-Practical-Fraud-Prevention)
- [Subscription - 8 most important KPIs for subscription business models]

## Industry Applications 业界案例

**Anti-Abuse AI Team @Linkedin**

[Using deep learning to detect abusive sequences of member activity](https://engineering.linkedin.com/blog/2021/using-deep-learning-to-detect-abusive-sequences-of-member-activi)


[Abstract] The Anti-Abuse AI Team at LinkedIn creates, deploys, and maintains models that detect and prevent many types of abuse, including the creation of fake accounts, member profile scraping, automated spam, and account takeovers. Bad actors use automation to scale their attempted abuse. There are many unique challenges associated with using machine learning to stop abuse on a large professional network including maximizing signal, keeping up with adversarial attackers, and covering many heterogeneous attack surfaces. In addition, traditional machine learning models require hand-engineered features that are often specific to a particular type of abuse and attack surface. To address these challenges, we have productionalized a deep learning model that operates directly on raw sequences of member activity, allowing us to scalably leverage more of the available signal hidden in the data and stop adversarial attacks more effectively. Our first production use case of this model was the detection of logged-in accounts scraping member profile data. We will present results demonstrating the promise of this modeling approach and discuss how it helps to solve many of the unique challenges in the anti-abuse domain.

**Payment Anallytics @Netflix**

- [Payment Analytics at Netflix](https://www.youtube.com/watch?v=xCwW1OENCOY)
  - Minimize involuntary churn
  - Optimize payment routing
  - Minimize False positives/negatives
  - Building tools for exploration of data
 
Business Processes
 - acquisition
 - renewals
 - after acquisition and renewals
 - retail gift
 - processor services
 - anomaly detection
 - offline and online processing analytics
 - issuer analytics
 

## Payments and Fraud Prevention 支付与反欺诈


### 支付方法论 阅读笔记

1、支付的基本概念

支付是货币债权转移过程。

支付的三个基本过程：交易、清分、和结算。

交易是支付的前提和基础，清分是数据的准备阶段，结算是支付的完结。

- 交易的重要性：拓展交易场景
  - 确保支付指令的生成、确认与传输。包括交易主体的合法性和身份确认、支付方式确认、支付通道的计算与决策、支付能力查证、交易结果的存储与返回信息归类等等。
- 清分(Clearing)：算出债权人与债务人各自应收应付，并没有发生实际交割。
- 结算(Settlement)：资产交割。

*“支付是交易的终点，是货币流动的起点。”*

支付演进概述
- 货币的实物商品本位阶段
  - 直到世界经济发展，黄金储备严重不足，美元贬值，布雷顿森林体系解体，进入货币第二阶段。
- 信用货币阶段

现代支付体系
- 支付服务组织：支付工具和支付系统的提供者
  - 中央银行，银行业金融机构，支付清算组织等。
- 支付系统：实现资金、债券、债务信息的清算，完成资金的转移。
  - 大额实时支付系统(High Value Payment System, HVPS)
  - 小额批量支付系统(Bulk Electronic Payment System, BEPS)相比大额实时支付具有一定延时性。
  - 网上支付跨行清算系统(Internet Banking Payment System, IBPS)网银系统。
  - 境内外币支付系统(Foreign Currency Payment System, FCPS)
- 支付工具
  - API, SDK, 移动端，二维码，电话语音支付，POS支付等。
- 支付体系监管

支付基础名词
- T+1：工作日+1
- D+1：自然日+1
- 全额结算(Gross Settlement)
- 净额结算(Net Settlement)
- 日切：上一个工作日结束的时间点。
- 头寸：款项(Statement of Financial Position)
- 轧头寸：预测头寸的宽松还是紧缺。
- 借记
- 拒绝交易(Charge Back)
- 冲正：交易在终端置为成功，但是发送到主机的账务交易包没有得到响应，即终端交易超时。终端向主机端请求取消交易流水。
- 卡基支付vs账基支付

2. 支付通道

支付通道要求 
- 支付方式：卡基&账基
- 支付品牌：商业银行，地区银行等
- BIN：一个支付通道往往会由于没有处理权限或未及时更新等，不能覆盖全部的BIN。
- 内外卡通道：国际支付通道
- 应付款能力：支付能力包括交易类型(消费、预授权、代扣、代付等)，产品特性(免CVV等)，交易币种等。
- 支付通道能力
  - 额度、限额、结算时效、风险拒付率、费率、安全性等。

支付通道结构
- 支付方式
- 支付品牌
- 支付通道
  - 物理通道：物理链路不可拆分
  - 逻辑通道：按接入渠道、商户、不同品牌、价格等因素拆分。
- 支付产品

支付通道分类
- 快捷支付与非快捷支付
  - 无磁有密类：直接支付。无签约。可能会验证有效期、CVV。
  - 快捷支付：现签约再支付。 

<img src="https://user-images.githubusercontent.com/46979228/185811807-5834751a-253a-4820-8227-0d85fe2c7100.png" alt="Unsupervised embedding" width = "400px"/>

3. 跨境支付（Cross-border Payment）

跨境支付是不同交易币种、不同结算币种、不同跨国监管主体资金转移、不同国界支付网络（如SWIFT、卡组织等）的连接。

- 交易发起阶段(Initiate Relationship)：（客户、汇出行、汇率转换机构）资金处理、费用处理、验证客户信息KYC、AML反洗钱信息提交、与汇率转换机构换汇等。
- 资金转移阶段(Transfer Money)：（当地清分网络、SWIFT、代理行）当地清分网络进行资金费用计算，SWIFT提供国际间资金处理报文传输网络等。
- 资金交付阶段(Deliver Funds)：（汇入行、收款人、汇率转换机构）
- 资金交付后阶段(Act Post Payment)：（银行、汇率转换机构、政府监管机构）

<img src="https://user-images.githubusercontent.com/46979228/188317677-84cafd83-932e-4993-a5f9-0b63b1174f11.png" alt="Unsupervised embedding" width = "800px"/>

**跨境支付背景**：
- 账户端应用场景（跨境电商）
- 备付金集中存管：第三方支付机构交易产生的客户备付金统一存至指定账户，央行监管，支付机构不得挪用、占用客户备付金。
- 直连与断直连

跨境支付场景
- 境外线下支付（基于交易）
- 跨境转账汇款（基于人口跨国转移流动）
- 跨境线上支付（基于交易）

跨境支付注意事项
- 跨币种资金转移与流动
  - DCC(Dynamic Currency Conversion)将当地货币实时转换为持卡人的记账货币 or EDC(Electronic Data Capture)支付时仅知道本地货币价格。
  - 跨地区的资金转移与流动

跨境支付方式与特性
- 电汇
- 时效
- 金额限制
- SWIFT系统：提供标准化、安全可靠合规的报文传送和通信服务。每个成员拥有一个SWIFT Code。

4. 路由系统

5. 重试服务

提高支付成功率
- 提升通道质量，进行系统监控并针对问题通道自行熔断，队列处理控制并发量，事中路由保证交易可用，根据日切时间进行自动对账增加处理时间，提升通道限额等；
  - 通道限额vs发卡行限额

重试服务流程
- 路由计算最优通道，交易失败后调用重试服务，匹配重试规则；


6. BIN服务

7. 清结算

7.3 计费服务
- 计费对象分为商户和支付通道。
  - 用支付产品来定义手续费。
  - 计费维度：币种、地区、国家、卡组织、卡类型、账户类型、支付方式、交易方式、风险模型(3DS)、支付通道、到账时效、支付产品等。
  - 计费规则类型：交易类型，单笔/批量，计费类型(阶梯手续费等)，手续费。
  
### 产业互联网 在线支付  

3.3 第三方支付模式

- Payment Gateway
  - 银行金融网络系统和Internet直接的接口，是银行操作将交易数据转换为金融机构内部数据的一组服务器设备；电商平台可对接多家银行专网系统，第三方支付解密电商平台用户传来的通信协议，并按照银行专网通信协议标准，将数据重新打包处理；银行完成转账后，将信息传给支付平台，支付平台将结果通知交易平台；第三方平台并不参与资金的支付和清算；
  - 买方资金可直接进入卖方账户，无需再第三方资金沉淀；实际资金是通过第三方备付金账户系统完成资金流转；
  
3.4 银行网关支付模式

3.5 信用支付模式

##### 在线支付系统构建基础

直联银行支付系统 VS 对接第三方支付渠道

平台产品与服务
- 标准品vs非标品
- 定价范围
- 交易频次
  - 采购频次高，则对支付便捷性要求高；
  


### 社会工程 阅读笔记

2 信息收集

信息收集工具
- BasKet
- Dradis

### 货币未来 阅读笔记

1. 货币

投资与货币的3点不同：
- 投资产生回报
- 货币携带的风险系数最低
- 投资的流动性不如货币

某种商品能够在自由市场上成为货币的关键性质，是它的适销性（以微小的价格损失出售该商品的便利性）。
- 价值尺度（便于分割组合）
- 空间尺度（便携性）
- 时间尺度（未来的保值能力）

生产新货币单位的难度决定了货币的硬度：
- 增加供给难度很高的货币称为硬通货；
- 增加供给难度不那么高的称为软通货；
- 理解货币硬度（存量-增量比越高，时间上的适销性越好）：
  - 存量
  - 增量

4. 政府货币

俗称“法定货币”(Fiat Money)。在金本位下，货币就是黄金，政府只是承担铸造标准重量单位的黄金或者印刷由黄金背书的纸币的责任。

**只有能兑换为具备适销性的货币形式，政府货币才能获得自身的适销性。所有的中央银行仍然会储备资产来支撑国家的货币价值。没有黄金储备的国家则会储备其他由黄金储备的国家的法定货币。->并不是政府赋予了黄金货币地位，而是只有通过持有黄金，政府才能让它发行的货币获得认可。**

一战前，政府实行金本位制。战后脱离金本位制，进入货币国家主义[哈耶克],即货币的价值，供给和利率由各国政府中央计划。真正的国际货币体系应该是全世界使用统一货币，货币在区域之间的流动是所有个体行为的结果。

布雷顿森林体系下，美国是全球货币体系的中心，成为其他国家中央银行的储备货币。其他国家央行将储备的黄金运到美国保存。建立国际货币基金组织(IMF)，实现汇率和金融的稳定。

5. 货币和时间偏好

降低时间偏好，人类可以执行长时间尺度的任务。

**通货膨胀**: 增加货币并不会增加使用该货币的社会的财富。


8. 数字货币

比特币
- 比特币发明之前的支付方式
  - 现金支付
  - 中介支付（第三方放大了交易的安全缺陷，交易成本及诈骗风险）
- 比特币通过充分的验证，免除对第三方的依赖。（建立在100%的验证和0%的信任之上）


### 蚂蚁金服 阅读笔记

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


### Payments Orchestration
Payments orchestration 支付编排
- an abstraction layer that met the four following conditions: one API, connectivity to providers that acquire cards and provide local payment methods, end-user routing and management configurable tools, and real-time ledgers.
- 支付编排在软件上链接不同的支付服务提供商PSP,收单机构和银行.


**Architecture Diagram**
- API (Account Verification, Authorization, Capture, Lifecycle Notifications, Partial Refunds, Redirects, Reporting API)
- Application (BIN file, FX Tracker tracks currency rate at time of settlement, payment method presentation, PCI Level 1 Certified Token Vault, Transaction Manager)
- Attribute (Idempotency that prevent double spending, currency support)
- Endpoint (3DS provider-standalone connection, PSP)
- Endpoint-PayMethod (Paypal, Klarna, U.S.ACH etc.)
- Feature (Algorithmic routing, integration to account updater programs, dynamic routing, endpoint timeouts, installment payments, merchant initiated transactions, partial captures - The ability to submit the same transaction for clearing multiple times for customizable amounts, PSP declinen codes)
- Instance 
- Reporting (A/B Testing, Routing report etc.)
- Service (iOS/Android SDK, Blocklist, Canonical Message Converter, Logger, Message Decision Handler, Payments Data Warehouse, Transaction Router, Retry Manager includes 3DS soft declines, Payment Method Catalog, Network Token Requestor, MID Manager)

**Unified Payment Interface (UPI)**



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

### EMV 3DS

- [3DS2 (3D Secure 2.0) - Everything You Need to Know [2021 Update]](https://www.emerchantpay.com/insights/3ds2/)
- [Visa's 3DS](https://www.visa.co.uk/dam/VCOM/regional/ve/unitedkingdom/PDF/visa-preparing-for-psd2-sca-publication-version-1-1-05-12-18-002-final.pdf)

3D Secure 2.0 is an authentication protocol that aims to reduce fraud and enhance security in online card payments.
- perform strong (two-factor) authentication. It aims to reduce fraud and enhance security in online card payments. 
- an enhanced version of the old 3DS protocol and introduced a more frictionless payment flow across different devices. 
- 3DS stands for Three-Domain Secure. 
- Visa created the authentication protocol in 1999, to help merchants and issuing banks authenticate cardholders’ identity when shopping online.

The three domains are 
- the acquirer domain (the merchant and the bank to which the money is paid), 
- the issuer domain (the bank that issued the cardholder’s card) and 
- the interoperability domain (the infrastructure used by the card scheme to enforce 3DS protocol, i.e. the Internet, the Merchant Plugin, and Access Control Server (ACS)).

The cardholder enters their card details at checkout. At this point, the merchant’s 3D Secure service provider sends an authentication request with rich data to the issuer. This data includes a varying amount of cardholder and device information upon regional or market law restrictions, such as device ID, MAC address, geo-location, previous transactions and more.

Then, the issuer’s 3D Secure service provider assesses the transaction risk. If the transaction is determined as high-risk, the transaction goes through a challenge. In other words, it prompts the cardholder to verify their identity using biometrics, and/or two-factor authentication, i.e. a one-time password, a fingerprint etc. If the transaction is deemed as low-risk, no further action is required on the cardholder’s end. The issuer sends the authentication result to the merchant, who in turn submits the transaction for authorisation with a flag indicating the authentication result.

**Benefits of 3DS**
- Enhanced user experience across devices and in-app
- Rich data exchange means more secure payments
- Reduced risk of fraud
- Chargeback Liability shift of 3D Secure

### Credit Card Payment Processing Rules and Laws

**PCI Data Security Standard**
- a global data security standard required of all businesses, regardless of size, that accept credit cards. PCI DSS and the Payment Application Data Security Standard (PA-DSS) are rules designed to reduce the incidence of credit card fraud.
- PA-DSS mandates that all point-of-sale (POS) equipment and terminals meet the PCI DSS standards. That means that if you have a POS system, the lion’s share of your PCI compliance is already handled by your POS hardware.
- [Payment Processing Laws](https://www.business.com/articles/payment-processing-laws/)

**Four Levels of PCI Compliance**

PCI Level 1
- applies to businesses that process more than 6 million credit card transactions annually.
  - Annual report on compliance (ROC) by a Qualified Security Assessor (QSA) or internal auditor (external or internal trained individuals certified to review payment transaction systems and assess and validate compliance)
  - Quarterly network scan by an Approved Scanning Vendor (ASV), a company with commercial software that analyzes and performs certified vulnerability scans on business systems and networks
  - Attestation of Compliance form

PCI Level 2
- applies to businesses that process 1 million to 6 million credit card transactions annually.
  - Annual self-assessment questionnaire
  - Quarter network scan by an ASV
  - Attestation of Compliance form 
 
PCI Level 3
- applies to businesses that process 20,000 to 1 million credit card transactions annually.
  - Annual self-assessment questionnaire
  - Quarter network scan by an ASV
  - Attestation of Compliance form

PCI Level 4
- applies to businesses that process up to 20,000 e-commerce payments or up to 1 million payments via other channels.
  - Annual self-assessment questionnaire recommended, but not required
  - Quarter network scan by an ASV, if applicable
  - Compliance validation requirements set up by merchant bank

**Card Association Network**
- set and manage the interchange rates, the purchase percentage and the per-transaction amount that you pay for the ability to accept each type of card.

**National Automated Clearinghouse Association**
- governs ACH transactions and the network they use. ACH transactions include direct deposits and direct payments from bank and credit union accounts.

**IRS Mandate**
- Section 6050W, also called the IRS mandate, which requires merchant services providers to specifically report their clients’ annual gross transactions processed with a credit or debit card or third-party network to the IRS.

**Nacha**
- any business that accepts ACH payments must abide by these rules.
- A new Nacha Supplementing Data Security Rule, which went into effect in June 2021, requires businesses that process 2 million or more ACH transactions annually to encrypt payment information on their computer systems while at rest (not being transmitted to a financial institution). Businesses with fewer than 2 million ACH transactions per year are not subject to the new rule but are encouraged to comply anyway. 

**Visa Chargeback Rules**
- Pre-Dispute
- Dispute
- Dispute Response (Representment)
- Pre-Arbitration
- Final Decision

Visa Chargeback Categories
- Fraud
- Authorization
- Processing Error
- Consumer Dispute

Rules for Responding to Visa Disputes
- draw from many different sources for evidence, whatever documents you provide must directly address the reason code attached to the dispute case.
- provide a rebuttal letter, which explains the reason for the dispute. You may also be required to include documents like a Chargeback Adjustment Reversal Request, a Chargeback Debit Advice Letter, depending on the circumstances.
- Merchants must respond within 30 days of “day one” for each phase. In Visa’s case, day one is the day after each phase is initiated.

Visa Chargeback Thresholds
- Visa chargeback rules limit the number of disputes a merchant can receive.

**Visa Dispute Monitoring Program (VDMP) & Visa Fraud Monitoring Program (VFMP)**
### How to Create a Fraud Prevention Unit

**Types of Online Fraud**
- New Account Fraud
- Synthetic Profiles
- Account Takeover (ATO)
- Mobile Fraud (track fraud by channel)
- First Party Fraud
- Merchant Fraud
- Transaction Laudering

**Regulation**
- General Data Protection Regulation (GDPR)
- Payment Services Directive (PSD2)
  - Strong Customer Authentication (SCA) for account-based payments and card-based payments (something you know i.e. password/pin, somthing you have i.e. token, phone, somthing you are i.e. biometric identifier)
- Transaction Risk Analysis (TRA)

**Fraud Managements**
- strategic, financial, operational, compliance, reputational fraud.

**Frameworks for Fighting Fraud**
- When to fight: proactiive vs. reactive
- How to fight: prevention, detection, measurement, analytics, investment and communication.

**Measuring the Scale of Fraud**
- Fraud loss chargebacks
- Chargeback representment win rate
- Fraud exposure (fraud prevented + fraud loss)
- Fraud exposure rate (fraud orders/total orders)
- Fraud loss chargeback rate
- Fraud loss rate

**Operational KPIs**
- Authorization rate (by bin and card scheme)
- Time to review (manual rebiew time - non-review time)
- Manual review rate
- Decline rate 
- False positive rate (TP/TP+FN)
  - customer reorder
  - manual review
  - auto-accept

**KPI for Fraud Analysts**
- Chargeback released (Leakage rate)
- Approval Rate
- Manual review time

**Benchmarking**
- Fraud by average ticket value
- Most typical fraud by type
- Fraud management challenges
- Detection tools and techniques
- Chargeback win rates

**Reducing PSD2/SCA Friction**
- Two-factor authentication (password + verification via SMS code)
- SCA through 3DS2
  - additional data is gathered during each transaction; customer behaviours and device ID, transaction history etc.
- TRA exemption


### Account Takeover



### Financial Impacts of Cybercrime

Two areas of cybercrime that are difficult to measure are IP theft and loss of opportunity.

Stolen IP and confidential business information, online fraud, financial manipulation of publicly traded companies, and the cost of securing networks after hacking are some of the most devastating effects to companies right now.

How much it costs to set up the automated attack—including the credentials, automation tools, and botnets—versus the estimated return. These attacks can
provide a solid ROI for cybercriminals even when the value per transaction is low.

**ROI = Value of attack * Change of Success / Cost - Initial Investment (100%)**

**Common Types of Attack**
- Low-cost credential stuffing attacks
- Get credentials
- Automate login
- Simulate relevant geography (proxy services)
- Defeat defenses

**How to Detect Automated Attacks**
- Examine application traffic patterns
- Check your login success ratios
- Look for diurnal patterns
- Check for attacker retooling

### BNPL Overview

Millennials and Gen Z spend 44% and 72% more on orders if BNPL is available as an option.

**Types of BNPL Fraud**
- Identity theft and social engineering scams
- Account Takeover (ATO)
- Friendly fraud

"As fraudsters can easily circumvent rules-based fraud management systems, all they
need to do is act as normal as possible over a period of time (sometimes weeks or even
months). They achieve this by browsing shops online, adding/removing small items to
checkout, making small purchases similar to the ones the real account holder will make.
They will even engage customer relations to make a connection with the merchant. Later
in the process, high-value goods will be purchased and even card details changed to
make payments. This is part of a Trojan Horse Scheme and is essentially a form of social
engineering."

**How to Beat BNPL Fraud**
- Behavioral biometrics, patterns of behaviors, device information obtained through digital fingerprinting are all analysed automatically
and in real time.

**5 BNPL Business Models**
- Integrated shopping apps (Afterpay, Klarna)
- Card-linked installment offerings
- Off-card financing solutions (Affirm)
- Virtual rent-to-own models
- vertical-focused larger-ticket plays

### Crypto Fraud

Terminologies
- Crypto: digital assets which exist today and operate on blockchain technology.
- Central Bank Digital Currencies (CBDCs): a digital form of fiat issued by governments.



*Robust fraud prevention solutions are built mainly by researchers who can explain the fraud from the perspectives of the attacker and the victim.*


### [O'Reilly] Practical Fraud Prevention

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


## Subscription - 8 most important KPIs for subscription business models

#### 1. Monthly recurring revenue (MRR)

- MRR = no. of customers x monthly rate

#### 2. Annual recurring revenue (ARR)

- ARR = (monthly rate x 12) / no. of customers

#### 3. Average revenue per user (ARPU)

- ARPU = MRR / no. of customers

#### 4. Customer lifetime value (CLV)

- CLV = Average Transaction Size x Number of Transactions x Retention Period

#### 5. Customer acquisition cost (CAC)

#### 6. Churn rate

- Churn rate = subscription cancellations/total customers

#### 8. Lead velocity rate (LVR)

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
