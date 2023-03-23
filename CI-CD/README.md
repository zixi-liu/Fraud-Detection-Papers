## CI / CD or Continuous Integration / Continuous Delivery

[The IDEAL & Practical CI / CD Pipeline - Concepts Overview](https://www.youtube.com/watch?v=OPwU3UWCxhw)
1. Source
 - Require X Reviewers
2. Build
 - Compile source and dependencies
 - Run unit tests
 - Check and enforce code coverage
3. Test Environment (Own DB)
 - Run integration tests
4. Production Environment (Own DB)
 - (1box) - DNS/AWS Lambda
   - Alarms (errors, latency, business metrics etc.)
   - Bake periods (anomaly detection or error counts + latency breaches)
   - Canary (cron job)


## AWS Core Services

Static Content
- S3 (simple, storage service) 存储在S3的object会备份在区域内的data centers。注重数据安全需要做cross-region replication。
  - S3 object由以下信息组成：key, value, version id, metadata, subresource, 11X9s, key management.
- Cloudfront, caching
- Route S3 domain hosting

**API Hosting**

Serverless Computing
- API Gateway + AWS Lambda -> restful endpoint

- AWS Load Balancer + EC2
- AWS Load Balancer + ECS (Elastic Container Store) + Docker

**Database**
- Amazon RDS
- Amazon Redshift
- Amazon DynamoDB
- Amazon ElasticCache
- Amazon Neptune

**Application Orchestration**
- Amazon SNS
- Amazon SQS
- AWS Step Function

**Analytics, Big Data, ML**
- Amazon QuickSight
- Amazon EMR
- Amazon Sagemaker

**Security**
- Amazon VPC (Virtual Private Cloud) - virtual firewall, subnets, gateways
- AWS Identity and Access Management

**Monitoring**
- Amazon CloudWatch
- AWS CloudTrail

## Nginx

- [深入浅出Nginx](https://zhuanlan.zhihu.com/p/34943332)

Nginx是一款轻量级的Web服务器、反向代理服务器，由于它的内存占用少，启动极快，高并发能力强，在互联网项目中广泛应用。

#### 反向代理服务器

- 正向代理“代理”的是客户端，而且客户端是知道目标的，而目标是不知道客户端是通过VPN访问的。
- 
