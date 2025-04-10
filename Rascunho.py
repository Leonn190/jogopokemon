
tabuleiro = [
    [2, 2, 1],
    [2, 2, 2],
    [2, 3, 3],
    [2, 3, 3]
]

def calcula_pontuacao_por_coluna(tabuleiro):
    linhas = len(tabuleiro)
    colunas = len(tabuleiro[0])
    possiveis = [0,0,0,0,0,0,0]
    pontuaçao = [0] * colunas

    for j in range(colunas):
        for i in range(linhas):
            possiveis[tabuleiro[i][j]] += 1

        pontuaçao[j] = 0
        for i in range(len(possiveis)):
            pontuaçao[j] += possiveis[i] * i * possiveis[i]
        possiveis = [0,0,0,0,0,0,0]
    return (pontuaçao)

print (calcula_pontuacao_por_coluna(tabuleiro))