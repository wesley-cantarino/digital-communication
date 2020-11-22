import math
import numpy as np 
import matplotlib.pyplot as plt

mensagem = 'Hello Word'
EbN0dB_MIN = 2
EbN0dB_MAX = 5

EbN0dB = np.arange(EbN0dB_MIN, EbN0dB_MAX, 1)
M = 2
m = np.arange(0, M)
constellation = (2*m + 1)/2 - M/2;
d = 2/np.sqrt((M**2 - 1)/3)
constellation = constellation * d
Ex = sum(constellation**2)/M

###############################
#Hello World
data_ASCII = bin(int.from_bytes(mensagem.encode(), 'big'))
data_str = str(data_ASCII)[2:]
data_list = [int(x) for x in data_str[0:]]
#print("Vetor dados:")
#print(data_list)

r_ = ''
r_ = r_.join(map(str, data_list))
data_re = r_
n = int(data_re, 2)
data_ = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
print("Mensagem em texto a ser enviada é \n \'", data_, "\'")

##############################

data = data_list
#print("Data: ", data)
n_bit = len(data)
signal = constellation[data]

#plt.title("2-PAM")
#plt.plot(signal)
#plt.show()

EbN0 = 10**(EbN0dB/10)
signal_Filter = data_list


N0 = 1/EbN0
sigma = np.sqrt(N0/2)

for j in range(len(EbN0dB)):
  awgn = np.random.normal(0, sigma[j], n_bit)
  signal_ = signal + awgn
  #plt.title("Sinal + AWGN")
  #plt.plot(signal_)
  #plt.show()

  print("Frase recebida para EbNo = ", EbN0dB[j], "dB foi:")
  for k in range(n_bit):
    if signal_[k] > 0:
      signal_Filter[k] = 1
    else:
      signal_Filter[k] = 0

  #print(signal_Filter)
  r_ = ''
  r_ = r_.join(map(str, signal_Filter))
  data_re = r_
  n = int(data_re, 2)
  data_ = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
  print("\'", data_, "\'")
  print("-------------------------------------")


 