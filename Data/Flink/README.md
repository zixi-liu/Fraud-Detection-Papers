## 流式计算


大数据流计算框架有Storm、Spark Streaming、Flink。

[Flink学习资源](https://github.com/pierre94/flink-notes)

### Spark Streaming

Spark Streaming将实时传输进来的数据按照时间进行分段，把一段时间传输进来的数据给合并在一起，当作一批数据，再去交给Spark处理。
- 如果时间段分的足够小，每一段的数据量就会比较小，Spark引擎处理速度快，就能够实现实时处理。

```
//指定分段时间间隔为1s。
val ssc = new StreamingContext(conf, Seconds(1));
```

### Flink

Flink会初始化一个流执行环境StreamExecutionEnvironment，然后利用这个执行环境构建数据流DataStream。

```

StreamExecutionEnvironment see = StreamExecutionEnvironment.getExecutionEnvironment();

DataStream<WikipediaEditEvent> edits = see.addSource(new WikipediaEditsSource());

```

如果要进行批处理计算，Flink 会初始化一个批处理执行环境 ExecutionEnvironment，然后利用这个环境构建数据集 DataSet。然后在 DataStream 或者 DataSet 上执行各种数据转换操作（transformation）。

Flink的架构和Hadoop或者Yarn看起来很像，JobManager是Flink集群的管理者，Flink程序提交给JobManager后，JobManager检查集群中所有TaskManager的资源利用状况，如果有空闲TaskSlot（任务槽），就将计算任务分配给它执行。

<img width="788" alt="image" src="https://user-images.githubusercontent.com/46979228/168446373-eb8f0ce0-283b-4628-b5a6-26e8e90a70c4.png">

**数据处理过程的基本模式**

- 数据输入 Source
- 数据处理 Transformation
- 数据输出 Sink

### 一、Flink概述

**流处理概念**

### 二、Flink DataStream API 实践原理

- DataStream API实践

