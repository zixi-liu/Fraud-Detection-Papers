
## RNN

RNN shares features learned across different positions of the sequence.

**1.1 Architecture**

将网络的隐含层输出又作为自身的输入，展开后相当于堆叠多个共享隐含层参数的前馈神经网络。

![image](https://user-images.githubusercontent.com/46979228/182639747-b3fb1c9b-949b-4154-ba57-64a39039bc73.png)

当使用RNN处理一个序列输入时，需要讲RNN按输入时刻展开，然后将序列中的每个输入对应到网络不同时刻的输入上，并将当前时刻隐含层的输出作为下一时刻的输入。

![image](https://user-images.githubusercontent.com/46979228/182641087-068a70c7-717c-4cfc-9a01-1318911c7aa7.png)

${h_t} = tanh(W^{xh}x_t + b^{xh} + W^{hh}h_{t-1} + b^{hh})$

$y = Softmax(W^{hy}h_n + b^{hy})$
- t是输入序列的当前时刻，隐含层 ${h_t}$ 不但与当前时刻有关，也与上一时刻隐含层有关，层层递归。
- The recurrent neural network scans through the data from left to right. The parameters it uses for each time step are shared. 

Different types of RNN
- many-to-many
- many-to-one
- onw-to-many

Vanishing Gradient Problems
- Basic RNN model has many local influences, meaning that the output $y^{<3>}$ is mainly influenced by values close to $y^{<3>}$ and a value here is mainly influenced by inputs that are somewhat close. It's difficult for the output here to be strongly influenced by an input that was very early in the sequence.
  - Exploding gradient is easier to spot. Use gradient clipping (if gradient vectors gets over certain threshold, re-scale gradient vectors) for exploding gradient issues.
  - Gated Recurrent Unit (GRU): update gate ( ${\gamma_u}$ between 0 and 1, decides when to update the memory cell) solves the vanishing gradient problem.
  - Equation: $c^{t} = {\gamma_u} * \tilde{c}^t + (1 - {\gamma_u}) * c^{t-1} $
  
## LSTM

![image](https://user-images.githubusercontent.com/46979228/182665493-1787c40e-6d40-4c5a-960a-023dda984b8c.png)

$\sigma$ 表示sigmoid函数，输出在0-1，作为加权求和的系数。由于旧状态与新状态的贡献需要独立的系数分别控制，因此引入门控机制。

## Bidirectional RNN

