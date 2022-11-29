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
