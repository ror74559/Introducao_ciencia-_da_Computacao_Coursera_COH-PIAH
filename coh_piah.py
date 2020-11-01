import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
     '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
     soma = 0
     for i in range(len(as_a)):
        soma += abs(as_a[i] - as_b[i])
     similaridade = soma / 6
     return similaridade
    

def calcula_assinatura(texto):

    sentencas = separa_sentencas(texto)
    frases = []
    for i in range(len(sentencas)):
        aux = separa_frases(sentencas[i])
        for j in range(len(aux)):
            frases.append(aux[j])
        aux = []

    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
   
    lista_palavras = []

    for l in range(len(frases)):
        aux = separa_palavras(frases[l])
        for m in range(len(aux)):
            lista_palavras.append(aux[m])
    n_palavras = len(lista_palavras)

    soma_tam_palavras = 0

    for i in range(len(lista_palavras)):
        soma_tam_palavras += len(lista_palavras[i])

    numero_palavras_diferentes = n_palavras_diferentes(lista_palavras)

    soma_caracter_sentenca = 0

    for i in range(len(sentencas)):
        soma_caracter_sentenca += len(sentencas[i])

    soma_caracter_frase = 0

    for i in range(len(frases)):
        soma_caracter_frase += len(frases[i])

    tamanho_medio_palavra = (soma_tam_palavras)/(n_palavras) #retorno

    tam_medio_frase = (soma_caracter_frase)/(len(frases)) #retorno

    type_token = numero_palavras_diferentes/n_palavras #retorno

    razao_hapax_legomana = n_palavras_unicas(lista_palavras)/n_palavras # retorno

    tam_med_sentenca = soma_caracter_sentenca/len(sentencas) #retorno

    complexidade_sentenca = len(frases)/len(sentencas) #retorno



    return [tamanho_medio_palavra,type_token,razao_hapax_legomana,tam_med_sentenca,complexidade_sentenca,tam_medio_frase]
    


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    assinaturas = []

    for texto in textos:
        assinaturas.append(calcula_assinatura(texto))

    compara_similaridade = []

    for assinatura in assinaturas:
        compara_similaridade.append(compara_assinatura(assinatura,ass_cp))

    return compara_similaridade.index(min(compara_similaridade)) + 1


def main():
    assinatura_base = le_assinatura()
    print(assinatura_base)
    textos = le_textos()
    final = avalia_textos(textos,assinatura_base)
    print ("O autor do texto " ,final, " está infectado com COH-PIAH")
    
main()
