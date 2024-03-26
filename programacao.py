
def calcular_soma_e_media(lista):
    soma = sum(lista)
    media = soma / len(lista)
    return soma, media


def substituir_palavra(lista, palavra_antiga, palavra_nova):
    for i in range(len(lista)):
        if lista[i] == palavra_antiga:
            lista[i] = palavra_nova
    return lista


def gerar_triangulo(num_linhas):
    for i in range(1, num_linhas + 1):
        print('*' * i)


if __name__ == "__main__":
    lista_numeros = [1, 2, 3, 4]
    soma, media = calcular_soma_e_media(lista_numeros)
    print("Soma:", soma)
    print("Média:", media)

    lista_palavras = ["banana", "morango", "limão"]
    palavra_antiga = "banana"
    palavra_nova = "maçã"
    nova_lista = substituir_palavra(lista_palavras, palavra_antiga, palavra_nova)
    print("Lista alterada:", nova_lista)

    num_linhas = 4
    gerar_triangulo(num_linhas)
    
