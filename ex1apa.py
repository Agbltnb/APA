#insertion sort 
#Ana Maria Pinto

import time
def insertion_sort(lista):
#sua complexidade é de n^2, logo no pior caso teremos
#quadrado de iterações


    start = time.time()
    for i in range(1, len(lista)):
        aux = lista[i]
        t = i
        while t > 0 and int(aux) < int(lista[t - 1]):
            lista[t] = lista[t - 1]
            t -= 1
        lista[t] = aux
    print("\n ordenação com insertion :" + str(lista))
    print("\n" + str(time.time()-start) + " segundo")
        

        
def selection_sort(lista):
#// serve para selecionar o menor valor do vetor e
#// e o vetor coloca na primeira posição, depois o 
#// segundo menor valor para a segunda posição
#// e assim em diante
                
    start = time.time()
    for i in range(0, len(lista)):
        imenor = i 
        t = i
        for t in range (i, len(lista)):
            if(int(lista[t]) < int(lista[imenor])):
                imenor = t
                                
    aux = lista[int(i)]
    lista[int(i)] = lista[imenor]
    lista[imenor] = aux
    print("\n a ordenação com selection:" + str(lista))
    print("\n" + str(time.time()-start) +"segundo")

 
try: #fazer testes para poder controlar os erros.

    filename = input("digite o nome do arquivo: ") 
    file = open(filename, 'r')
    lista = []   #se não fizer por esse parametro o programa não entende que é uma lista, mas sim que é uma variavel qualquer.
    lista = file.readlines()
    print(lista)
    print("tamanho = " + str(len(lista))) #verifica os elementos do vetor para fazer a ordenação
    insertion_sort(lista)
    selection_sort(lista)
     
finally:
    file.close()
