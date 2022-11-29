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
