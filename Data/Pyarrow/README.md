## Apache Arrow

- [FastNLP 开发日记](https://zhuanlan.zhihu.com/p/442390833)

### huggingface datasets
pyarrow是python封装的高层接口，其底层实现是Apache Arrow c++库实现的。其本身设计是为了能够处理大批量数据存储和处理，其底层存储是与语言无关的柱状内存格式。假设一个数据集有4个列，其在内存的存储位置如图1所示。pyarrow严格定义了ds的field的数据类型，创建时需要传入ds的schema，否则默认会检测数据列的数据类型。若是想进一步节省内存可以将数据类型定义到多少位，如int8,int16,int32等，而采用默认则为int64。

pyarrow支持与numpy，pandas，python objects等数据类型的转化，pyarrow的table使用方式与pandas的DataFrame有异曲同工之妙，则两者相互转化非常容易。pyarrow还提供了zero-copy的机制，使得你取数据时候不会增加内存，底层实现是返回指向数据的指针，操作的数据对象是同一份数据。

pyarrow的csv读文件速度会比python提供的csv会更快，更有趣的是pyarrow提供了memory_map方法来读取数据。memory_map主要针对大数据集读取，其原理是将数据存储的硬盘地址映射到内存中，不直接加载整个数据集，当使用数据集时再根据映射地址将硬盘数据直接加载到内存中；所带来的好处是减少地址映射的开销，加载使用数据时候速度会更快，避免数据集太大内存放不下的问题，可以批量加载数据集。
