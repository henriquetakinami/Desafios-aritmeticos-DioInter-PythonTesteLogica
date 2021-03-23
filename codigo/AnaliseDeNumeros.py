"""
Você deve fazer a leitura de 5 valores inteiros. Em seguida mostre quantos valores informados são pares, quantos valores informados são ímpares, quantos valores informados são positivos e quantos valores informados são negativos.
Entrada

Você receberá 5 valores inteiros.
Saída

Exiba a mensagem conforme o exemplo de saída abaixo, sendo uma mensagem por linha e não esquecendo o final de linha após cada uma.

"""

a,b,c,d,e = int(-5), int(0), int(-3), int(-4), int(12)

lista_vazia = []

lista_vazia.append(a), lista_vazia.append(b), lista_vazia.append(c), lista_vazia.append(d), lista_vazia.append(e)
par = 0
impar = 0
negativo = 0
positivo = 0
for n in lista_vazia:
    if n % 2 == 0:
        par+=1
    else:
        impar+=1

    if n < 0:
        negativo+=1
    elif n == 0:
        continue
    else:
        positivo+=1

print(str(par) + " valor(es) par(es)")
print(str(impar) + " valor(es) impar(es)")
print(str(positivo) + " valor(es) positivo(s)")
print(str(negativo) + " valor(es) negativo(s)")