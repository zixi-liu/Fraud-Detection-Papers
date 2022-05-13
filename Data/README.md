## 大数据基础架构

**Google大数据的三篇论文（文件系统，计算框架和数据库系统）**
- [分布式文件系统GFS](https://static.googleusercontent.com/media/research.google.com/en//archive/gfs-sosp2003.pdf)
- [大数据分布式计算框架MapReduce](https://static.googleusercontent.com/media/research.google.com/en//archive/mapreduce-osdi04.pdf)
- [NoSQL数据库系统BigTable](https://static.googleusercontent.com/media/research.google.com/en//archive/bigtable-osdi06.pdf)

**批处理/大数据离线计算**

**大数据流计算**

采用批处理技术处理全量数据，采用流式计算处理实时新增数据。

<img width="400" alt="image" src="https://user-images.githubusercontent.com/46979228/168396407-226bf4b5-8309-498c-9402-4c1b51c03082.png">

移动计算程序到数据所在位置进行计算
1. 将待处理的大规模数据存储在服务器集群的所有服务器上，主要适用HDFS分布式文件存储系统，将文件分成很多块（block），以块为单位存储在集群服务器上。
2. 大数据引擎根据集群里不同服务器的计算能力，在每台服务器上启动若干分布式任务执行进程，这些进程会等待给它们分配执行任务。
3. 使用大数据计算框架支持的编程模型进行编程，比如Hadoop的MapReduce编程模型，或者Spark的RDD编程模型。应用程序编写好以后，将其打包，MapReduce和Spark都是JVM环境中运行，打包出来一个Java的JAR包。
4. 用Hadoop或者Spark的启动命令执行这个应用程序的JAR包，首先执行引擎会解析程序要处理的数据输入路径，根据输入数据量的大小，将数据分成若干片（Split），每一个数据片都分配给一个任务执行进程去处理。
5. 任务执行进程收到分配任务，检查自己是否有任务对应的程序包，如果没有就去下载程序包，下载以后通过反射的方式加载程序。
6. 加载程序后，任务执行进程根据分配的数据片的文件地址和数据在文件内的偏移量读取数据，并把数据输入给应用程序相应的方法去执行，从而实现在分布式服务器集群中移动计算程序。

**HDFS架构**

<img width="841" alt="image" src="https://user-images.githubusercontent.com/46979228/168401262-cd408a2d-e022-40d9-8d07-8030538cc825.png">

DataNode负责文件数据的存储和读写操作，HDFS将文件数据分割成若干块数据块（Block），每个DataNode存储一部分数据块。应用程序客户端（Client）可以对数据块并行访问。

NameNode负责整个分布式文件系统的元数据（MetaData）管理，也就是文件路径名，数据块的ID以及存储位置等信息。

NameNode高可用容错能力非常重要，采用主从热备的方式提供高可用服务。
- 部署两台NameNode服务器，通过ZooKeeper选举，主要是通过争夺znode锁资源，决定谁是主服务器。
