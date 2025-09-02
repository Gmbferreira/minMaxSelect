from minMaxSelect import minMaxSelect
import random
import time
import math
import numpy as np

def measure_complexity(func_instrumented):
   
    print("Iniciando a medição de complexidade...")
    
    input_sizes = [100, 200, 400, 800, 1600, 3200, 6400]
    operation_counts = []

    print(f"{'Tamanho (n)':<15}{'Comparações':<15}{'Tempo (s)':<15}")
    print("-" * 45)

    for n in input_sizes:
        random_list = [random.randint(0, n * 10) for _ in range(n)]
        
        start_time = time.time()
        
        *_, count = func_instrumented(random_list, 0, len(random_list) - 1)
        
        end_time = time.time()
        
        operation_counts.append(count)
        elapsed_time = end_time - start_time
        print(f"{n:<15}{count:<15}{elapsed_time:<15.6f}")

    complexities = {
        "O(log n)": [],
        "O(n)": [],
        "O(n log n)": [],
        "O(n^2)": [],
    }

    for i in range(len(input_sizes)):
        n = input_sizes[i]
        count = operation_counts[i]
        if n > 1:
            complexities["O(log n)"].append(count / math.log(n))
            complexities["O(n log n)"].append(count / (n * math.log(n)))
        complexities["O(n)"].append(count / n)
        complexities["O(n^2)"].append(count / (n**2))

    print("\nAnálise da estabilidade da razão (contagem/função(n)):")
    best_fit = None
    min_std_dev = float('inf')

    for name, ratios in complexities.items():
        if not ratios: continue
        std_dev = np.std(ratios)
        print(f"- {name}: Desvio Padrão = {std_dev:.4f}")
        if std_dev < min_std_dev:
            min_std_dev = std_dev
            best_fit = name
    
    print("\nA complexidade que melhor se ajusta aos dados (menor desvio padrão) é a mais provável.")
    return best_fit

if __name__ == "__main__":
    print("--- Demonstração do Algoritmo MaxMin Select ---")
    lista_numeros = [10, 5, 25, 3, 47, 1, 98, 32, 12, 8]
    print(f"Lista original: {lista_numeros}")

    if lista_numeros:
        menor, maior = minMaxSelect(lista_numeros, 0, len(lista_numeros) - 1)
        print(f"Menor elemento: {menor}")
        print(f"Maior elemento: {maior}\n")
    else:
        print("A lista está vazia.\n")
        
    print("--- Análise de Complexidade Assintótica ---")
    complexidade_estimada = measure_complexity(minMaxSelect)
    
    print(f"\nComplexidade estimada do algoritmo: {complexidade_estimada}")