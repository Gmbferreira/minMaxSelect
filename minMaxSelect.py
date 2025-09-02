# -*- coding: utf-8 -*-

def minMaxSelect(arr, inicio, fim):
    if inicio == fim:
        return arr[inicio], arr[inicio]

    if fim == inicio + 1:
        if arr[inicio] < arr[fim]:
            return arr[inicio], arr[fim]
        else:
            return arr[fim], arr[inicio]

    meio = (inicio + fim) // 2

    min_esq, max_esq = minMaxSelect(arr, inicio, meio)
    min_dir, max_dir = minMaxSelect(arr, meio + 1, fim)

    menor_final = min_esq if min_esq < min_dir else min_dir
    maior_final = max_esq if max_esq > max_dir else max_dir

    return menor_final, maior_final

