"""

Desafio

Neste desafio sua tarefa será ler vários números e em seguida dizer quantas vezes cada número aparece, ou seja, deve-se escrever cada um dos valores distintos que aparecem na entrada por ordem crescente de valor.
Entrada

A primeira linha de entrada contem um único inteiro N, que indica a quantidade de valores que serão lidos para X (1 ≤ N ≤ 2000) logo em seguida. Com certeza cada número não aparecerá mais do que 20 vezes na entrada de dados.
Saída

Imprima a saída de acordo com o exemplo fornecido abaixo, indicando quantas vezes cada um deles aparece na entrada por ordem crescente de valor.


"""
import collections

ent = [7, 8, 10, 8, 260, 4, 10, 10]

dict = {}
for n in ent:
    if n not in dict.keys():
        dict[n] = 0
        dict[n] =+ 1
    else:
        dict[n] = dict[n] + 1

ord = collections.OrderedDict(sorted(dict.items()))

for k, v in ord.items():
    print(str(k) + " aparece " + str(v) + " vez(es)")


