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
- Offloading - trading memory capacity for bandwidth (Offload CPU tensors not used in computation from GPU to CPU)
- Model Implementation 
  - Tensor, Pipeline Parallelism
  - Data parallel, distributed Optimizer
  - Automatic Mixed Precision
  - BERT, GPT, T5, Vision Transformer
  - Achieve high utilization and scaling to thousands of GPUs
  - Working towards Trillion models

![image](https://user-images.githubusercontent.com/46979228/227277392-241833c9-1c20-428b-a36c-5218b301b7a0.png)
