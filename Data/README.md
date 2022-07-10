## Table of Contents

- Fraud Data Types 欺诈数据类型
- 


### 大数据基础架构

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

**保证可用性的策略**
- 冗余备份
- 失效转移
- 限流降级

**MapReduce编程模型**
- map主要输入是一对<key,value>值，经过map结算后输出一对<key,value>值，然后将相同key合并，形成<key,value集合>，再将<key,value集合>输入reduce，经过计算输出零个或多个<key,value>对。

举例-词频统计问题的Python实现

```
strl_list = str.replace('\n', '').lower().split(' ')
count_dict = {}
for str in str_list:
  if str in count_dict.keys():
    count_dict[str] = count_dict[str] + 1
    else:
      count_dict[str] = 1
```
MapReduce实现

```
public class WordCount{
  public class TokenizerMapper
    extends Mapper<Object, Text, Text, IntWritable>{
      
      private final static IntWritable one = new IntWritable(1);
      private Text word = new Text();
      
      public void map(Object key, Text value, Context context) throws IOException, InterruptedException{
        StringTokenizer itr = new StringTokenizer(value.toString());
        while (itr.hasMoreTokens()){
          word.set(itr.nextToken());
          context.write(word, one);
        }
      }
    }
}

public static class IntSumReducer
  extends Reducer<Text, IntWritable, Text, IntWritable>{
  private IntWritable result = new IntWritable();
  
  public void reduce(Text key, Iterable<IntWritable> values, Context Context) throws IOException, InterruptedException{
    int sum = 0;
    for (IntWritable val: values){
      sum += val.get();
    }
    result.set(sum);
    context.write(key, results);
  }
 } 
}
```

### Yarn资源调度框架

服务器集群资源调度管理和MapReduce执行过程耦合在一起，如果想在当前集群中运行其他计算任务，比如Spark或者Storm，就无法统一使用集群中的资源了。

- Resource Manager资源管理器
- Node Manager节点管理器（基本跟HDFS的DataNode进程一起出现）

### Hive

Map, Reduce, Shuffle

<img width="800" alt="image" src="https://user-images.githubusercontent.com/46979228/168404902-72a9dc89-f570-4f50-8957-d363ccb526e8.png">

Hive根据SQL语句生成函数的DAG，然后封装进MapReduce的map和reduce函数。

### Spark

Resilient Distributed Datasets (RDD)
- Spark分布式计算的数据分片、任务调度都以RDD为单位展开。每个RDD分片都会分配到一个执行进程去处理。
  - Spark SQL
  - Spark Streaming
  - MLlib
  - GraphX

### HBase

BigTable对应的NoSQL系统HBase。

HRegion是HBase负责数据存储的主要进程，应用程序对数据的读写操作都是通过和HRegion通信完成。

HRegionServer 是物理服务器，每个 HRegionServer 上可以启动多个 HRegion 实例。当一个 HRegion 中写入的数据太多，达到配置的阈值时，一个 HRegion 会分裂成两个 HRegion，并将 HRegion 在整个集群中进行迁移，以使 HRegionServer 的负载均衡。

HBase 的做法是按 Key 的区域进行分片，这个分片也就是 HRegion。应用程序通过 HMaster 查找分片，得到 HRegion 所在的服务器 HRegionServer，然后和该服务器通信，就得到了需要访问的数据。

<img width="897" alt="image" src="https://user-images.githubusercontent.com/46979228/168507922-10779f36-7131-4844-91fa-842daa0ceb4f.png">





