## Fraud Data Types

**反欺诈业务背景**

C端欺诈风险：
- 账号安全。
- 交易场景中，套现交易和虚假交易。
- 支付环节盗号风险。
- 信贷场景中，恶意申请信贷产品并逾期。

互联网平台侧主要通过三种方式应对欺诈：
- 黑白名单
- 规则策略
- ML模型

平台数据主要包含三类型数据：
- 交易相关属性 (transaction related)
  - Time: Date and time of the transaction
  - Type: The kind of transaction issued. A real payment (e.g. ecommerce) or a virtual transaction (3D-secure ACS).
  - Authentication: The kind of authentication experienced by the card holder: Chip-based PIN check, signature, 3D-secure.
  - Entry Mode:  The interaction modality between the card and the terminal: e.g. contactless, magentic stripe, manual entry.
  - Amount: The transacted monetary value in Euro.
- 信用卡持有人相关属性 (card holder/card related)
  - Profile: Several attributes describing the card holder such as his country of residence, age or gender.
  - Card: Several attributes describing the credit card such as the credit limit, card type or expiration date.
- 商户相关属性 (merchant related)
  - Profile: Two attributes describing the terminal: The merchant category code assigned to the terminal (e.g. shoe store, ATM, etc.) and the country the terminal is registered in (e.g. Belgium, Germany, etc.)
