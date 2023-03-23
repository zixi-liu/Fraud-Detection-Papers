## Overview

Very large deep neural networks (DNNs), whether applied to natural language processing (e.g., GPT-3), computer vision (e.g., huge Vision Transformers), or speech AI (e.g., Wave2Vec 2) have certain properties that set them apart from their smaller counterparts. As DNNs become larger and are trained on progressively larger datasets, they can adapt to new tasks with just a handful of training examples, accelerating the route toward general artificial intelligence. Training models that contain tens to hundreds of billions of parameters on vast datasets isn’t trivial and requires a unique combination of AI, high performance computing (HPC), and systems knowledge. We'll demonstrate how to train the largest of neural networks and deploy them to production.
In this workshop, you’ll learn how to:

- Train neural networks across multiple servers
- Use techniques such as activation checkpointing, gradient accumulation, and various forms of model parallelism to overcome the challenges associated with large-model memory footprint
- Capture and understand training performance characteristics to optimize model architecture
Deploy very large multi-GPU models to production using NVIDIA Triton™ Inference Server


<img width="1125" alt="image" src="https://user-images.githubusercontent.com/46979228/227267515-43fb934b-2e8b-4c78-8253-9f6433af3c7e.png">

## Challenges

- Cost of labels limits the utility of supervised deep learning models
- The Scaling Laws - loss decreasing with training data size increasing
- Few Shot Learning
  - learning from far fewer examples - larger models make increasingly efficient use of in-context information


**Model Tuning & Prompt Tuning**
- Prompt tuning is where you essentially have the model learn some 'virtual tokens' - basically an embedding that gets prepended to your prompt. So the model learns, given some examples, what a good prompt looks like (although the prompt isn't something human readable - thus 'virtual prompt')
  - [The Power of Scale for Parameter-Efficient Prompt Tuning](https://arxiv.org/pdf/2104.08691.pdf)

**Towards General Intelligence**
- Does not need labelled data
- Single generic model can do more than one tasks
- More generalized: in addition to language also learns higher level concepts, styles, etc.
- Computationally Expensive (~500 Billion parameters)

**Execution Time**
- Scale of compute

## Algorithms

**Transformer**
- Common fault tolerance mechanism, in the large model training
  - Model checkpointing is a standard practice these days, to restart training from those checkpoints in case of HW failures during training.
- Data Parallel = same model, different slices of data each batch, Model Parallel = same data, different slices of model

## Systems

- NVIDIA DGX Superpod Solution
- Automatic Mixed Precision
- Activation Checkpoints 
  - Trading compute for memory
- Gradient Accumulation
  - Gradient accumulation increases the effective batch size. Increasing the batch size is a very common trick to speed up training since GPUs are massively parallel and can process more data points at once with a larger batch.
- Offloading - trading memory capacity for bandwidth (Offload CPU tensors not used in computation from GPU to CPU)
- Model Implementation 
  - Tensor, Pipeline Parallelism
  - Data parallel, distributed Optimizer
  - Automatic Mixed Precision
  - BERT, GPT, T5, Vision Transformer
  - Achieve high utilization and scaling to thousands of GPUs
  - Working towards Trillion models

![image](https://user-images.githubusercontent.com/46979228/227277392-241833c9-1c20-428b-a36c-5218b301b7a0.png)

## Data Parallelism vs. Model Parallelism

- [深度学习并行训练算法: DDP, TP, PP, ZeRO](https://zhuanlan.zhihu.com/p/581677880)
- [Distributed Parallel Training: Data Parallelism and Model Parallelism](https://towardsdatascience.com/distributed-parallel-training-data-parallelism-and-model-parallelism-ec2d234e3214)
- [GPU/CPU集群下做到Data/Model Parallelism的区别](https://www.zhihu.com/question/31999064)
  - Tensor parallelism would just break up the matrix operations used in forward/back propagation.
  - In practice, tensor parallelism used only when NVLink is available (in Ampere generation of GPUs, this is limited to the GPUs within a single node).

#### 并行计算解决的问题
- 1） 通过并行化来做性能加速
- 2） 解决单机内存无法hold的huge model size

#### 并行计算的优化方案

- 将计算与通信开销overlap以后，提高计算资源的utilization rate；
- 神经网络的拓扑结构进行优化，在不明显损失精度的情况下，减少并行计算的同步过程所需要传输的数据量；
- 在不明显损失精度的情况下，改善计算资源的utilization rate；

CPU vs. GPU
- 同样面积的芯片，CPU放置更多的多级缓存和指令并行的控制部件；GPU则更多运算单元；
- GPU往往拥有更大带宽的Memory，所谓的显存，因此在大吞吐量的应用中会有很好的性能；

1) 相较于CPU而言，GPU更强大的“naive"浮点算术能力，但在GPU集群上，因为计算与通信的gap导致的性能degradation会更显著。

2) GPU的访存特点也使得GPU计算平台上能hold的有效模型尺寸通常来说是远小于CPU平台上的（以比较主流的Nvidia  Tesla K40M为例，显存12GiB），这也使得GPU平台上在处理比较大的模型的时候，会比CPU平台更早地遇到模型尺寸的瓶颈，需要考虑model parallelism。


## Inference

Model Selection
- Not all models respond in the same way to knowledge distillation, pruning and quantization.

<img width="1269" alt="image" src="https://user-images.githubusercontent.com/46979228/227357113-e26bb0fd-cf24-49d9-ad16-b9be7226baff.png">

#### Quantization

- Small precision but still maintain accuracy;
  - Without calibration, you could incur a pretty steep accuracy loss. FP16 tends to maintain accuracy well but a lot more caution is needed for going down to 8 bits.
- Bandwidth reduction;

<img width="1399" alt="image" src="https://user-images.githubusercontent.com/46979228/227357821-a8954075-c177-4205-a6e1-f7d5c4d9d68d.png">

#### Model Optimization

- Pruning

#### Sparsity Support

#### Knowledge Distillation

- Compress a large model or teach a smaller model; i.e. DistillBERT etc.

### Inference of Huge Models

- Maximize utilization of GPUs;
- Maximize throughput, minimize latency;

### Production Deployment





