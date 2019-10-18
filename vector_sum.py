import matplotlib.pyplot as plt
import numpy as np

origin = [0, 0]
vector1 = [-2, 1]
vector2= [3, 4]

arrow1 = np.array(vector1) #cria os vetores
arrow2 = np.array(vector2)
vectorsum = arrow1 + arrow2 

xvalues = [arrow1[0], arrow2[0], vectorsum[0], origin[0]]
yvalues = [arrow1[1], arrow2[1], vectorsum[1], origin[1]]

ax = plt.axes() #cria o plano

#criação das setas no plano
ax.arrow(0, 0, arrow1[0], arrow1[1], color='g', length_includes_head=True, head_width=0.2, head_length=0.2)
ax.arrow(arrow1[0], arrow1[1], arrow2[0], arrow2[1], color='g', length_includes_head=True, head_width=0.2, head_length=0.2)
ax.arrow(0, 0, vectorsum[0], vectorsum[1], color='b', length_includes_head=True, head_width=0.2, head_length=0.2)

ax.set_yticks(yvalues)
ax.set_xticks(xvalues)

#seta os valores do foco do plano
ax.set(xlim=(min(xvalues), max(xvalues)), ylim=(min(yvalues), max(yvalues)))

ax.set_axisbelow(True) #deixa a grade do plano ao fundo
ax.set_aspect('equal', adjustable='box') #ajusta a grade do plano
ax.grid() #mostra a grade do plano

plt.show()