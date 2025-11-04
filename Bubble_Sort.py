import time

def bubble_sort(lista):
    start = time.perf_counter()  # início da medição de tempo
    n = len(lista)
    comparacoes = 0
    trocas = 0

    for i in range(n):
        houve_troca = False
        for j in range(0, n - i - 1):
            comparacoes += 1
            
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocas += 1
                houve_troca = True
        
        if not houve_troca:  # otimização: para cedo se já estiver ordenado
            break

    end = time.perf_counter()  # fim da medição
    tempo_ms = (end - start) * 1000.0
    return comparacoes, trocas, tempo_ms

def converter_entrada(texto):
    return list(map(int, texto.replace(",", " ").split()))

# --- Execução ---
entrada = input("Cole os números (ex: 1,2,3,1,23,4): ")
lista = converter_entrada(entrada)

comparacoes, trocas, tempo_ms = bubble_sort(lista)

print("Lista ordenada:", lista)
print(f"Comparações: {comparacoes}")
print(f"Trocas: {trocas}")
print(f"Tempo (ms): {tempo_ms:.3f}")
