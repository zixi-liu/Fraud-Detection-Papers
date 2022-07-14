## All You Need for CICD Testing

- [API Test](#api-test)
- [Smoke Test](#smoke-test)
- [Perf Test](#perf-test)
- [Stress Test](#perf-test)
- [Load Test](#perf-test)
- Regression Test


### **API Test**

API实现两个或多个独立系统或模块间的通信和数据交换能力。

API测试关注在系统架构的业务逻辑层。

API测试覆盖
- 检查API是不是根据输入数据返回期望的结果
- 验证API是不是不返回结果或者返回异常结果
- 验证API是不是正确出发其他event或者正确调用了其他API
- 验证API是不是正确更新了数据等等

API测试能发现什么bug
- 无法正确处理错误的深入条件
- 缺少或重复功能
- 可靠性问题
- 安全问题
- 多线程问题
- 性能问题
- 相应数据结构不规范问题
- 有效参数值不能正确处理

API测试工具
- SoapUI
- JMeter
- PostMan

### **Smoke Test**

It is a set of tests run on each new build of a product to verify that the build is testable before the build is released into the hands of the test team.

测试强调程序的主要功能进行的验证，而不会对具体功能进行更深入的测试。在CI中每一个Build都自动的去执行主流程的测试，确保其是一个基本可用的版本。


### **Perf Test**

- Stress Test 
- Load Test

<img width="691" alt="image" src="https://user-images.githubusercontent.com/46979228/178886349-83ed84b1-4887-409f-9261-af6e670cedcc.png">


<img width="691" alt="image" src="https://user-images.githubusercontent.com/46979228/178888234-c96a1531-5dca-416a-8385-5b644949eb59.png">

- [Load Testing vs Stress testing](https://www.soapui.org/learn/load-testing/load-testing-vs-stress-testing-vs-performance-testing/)


