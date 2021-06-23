import matplotlib.pyplot as plt

x1=[2,5,6,14]
y1=[11,22,33,44]

x2=[2,5,6,15]
y2=[4,12,18,45]

x3=list(range(6))
y3=list(map(lambda x : x**2+2*x-1, x3))

#plot para lineal
plt.plot(x1,y1, 'o-', color="blue", linewidth=3, label='linea 1' )
plt.plot(x2,y2, 'o-', color="red", linewidth=3, label='linea 2' )
plt.plot(x3,y3, 'o-', color="green", linewidth=3, label='linea 3' )
plt.title('Dos graficas juntas')
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.grid()
plt.show()

#bar para grafica de barras
plt.bar(x1,y1, color="blue", linewidth=3, label='linea 1' )
plt.bar(x2,y2, color="red", linewidth=3, label='linea 2' )
plt.title('Dos graficas juntas')
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.grid()
plt.show()
#Histogramas
Datos=[20,22,21,20,23,25,28,40,22,23,22,15,16,18,18,19,21,22,24,4,12,17,17,22,30]
Rangobin=[0,10,20,30,40,]

plt hist(Datos, Rangobin, histtype='bar', rwidth=0.8 ,color="purple")
plt.title('Histograma')
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.grid()
plt.show()