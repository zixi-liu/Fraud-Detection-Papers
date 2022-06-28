## DynamoDB

### 1. 基本概念

**getItem, query and scan**

这三个操作都是查询操作，效率分别是：getItem > query > scan.

- getItem是根据primary key进行插叙，可以理解为通过primary key在hashMap上查询。
- scan是全表扫描。
- query是最常见的查询方式。

**分区键：partition key**

**排序键：sort key**
