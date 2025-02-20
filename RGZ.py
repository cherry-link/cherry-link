import numpy as np
import matplotlib.pyplot as plt

PowerLeft = 1000 - int(input("Введите величину снижения мощности, МВт: "))
Consumers = np.array([70, 80, 100, 120, 130, 150, 170, 180])
while PowerLeft < np.sum(Consumers):
    Consumers = np.delete(Consumers, 0)
T = np.array(range(Consumers.size))
plt.bar(T, Consumers)
plt.ylabel('P, МВт')
print("Потребителей подключено: ", Consumers.size)
plt.show()