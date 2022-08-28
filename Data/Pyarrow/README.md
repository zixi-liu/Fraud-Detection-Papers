## Apache Arrow

- [FastNLP 开发日记](https://zhuanlan.zhihu.com/p/442390833)

### huggingface datasets
pyarrow是python封装的高层接口，其底层实现是Apache Arrow c++库实现的。其本身设计是为了能够处理大批量数据存储和处理，其底层存储是与语言无关的柱状内存格式。假设一个数据集有4个列，其在内存的存储位置如图1所示。pyarrow严格定义了ds的field的数据类型，创建时需要传入ds的schema，否则默认会检测数据列的数据类型。若是想进一步节省内存可以将数据类型定义到多少位，如int8,int16,int32等，而采用默认则为int64。
