import matplotlib.pyplot as plt #alias

def generate_pie_chart(): #funcion que genera un piechart
    labels = ['A', 'B', 'C'] #etiquetas para los datos
    values = [200, 34, 120] #valores para el grafico

    fig, ax = plt.subplots() #obtener figuras y coordenas desde matlib
    ax.pie(values, labels=labels)#se le envian los valores y los labels
    plt.savefig('pie.png')#genere la grafica y lo guarde en un archivo / show() lo muestra y termina el programa
    plt.close()

    #este es un  modulo el cual va a ser importado y ejecutado desde main.py