# importar numpy
#
# variável linhas
# variável colunas
#
# classe Estado
# função recompensa
#
# classe RL
# função qLearning
# função posicaoLivres
#
# classe Jogo
# função renderizar



import numpy as np

linhas = 3
colunas = 3


class Estado:
    def __init__(self, tabela):
        self.table = tabela

    def recompensa(self):
        for i in range(linhas):
            if sum(self.table[i, :]) == 3:
                return 1

            elif sum(self.table[i, :]) == -3:
                return -1

        for i in range(colunas):
            if sum(self.table[i, :]) == 3:
                return 1

            elif sum(self.table[i, :]) == -3:
                return -1

        diagonal = sum(self.table[i, i] for i in range(colunas))
        diagonal_reverse = sum(self.table[i, colunas - i - 1] for i in range(colunas))

        diagonalValor = max(abs(diagonal), abs(diagonal_reverse))

        if diagonalValor == 3:
            if diagonal == 3:
                return 1

            if diagonal_reverse == 3:
                return 1

            return -1

        return 0


class RL:
    def __init__(self, tabela):
        self.tabela = tabela
        self.tmp = None

    def qLearning(self):
        livres = self.posicaoLivres()

        if len(livres) == 0:
            exit("Fim de jogo")

        self.tmp = self.tabela

        p = livres[0]
        for _ in livres:
            self.tmp[_] = 1
            estado = Estado(self.tmp)
            R = estado.recompensa()
            if R == 1:
                return self.tmp
            elif R == -1:
                self.tmp = self.tabela
                continue
            else:
                self.tmp = self.tabela
                continue

        return self.tabela[p]

    def posicaoLivres(self):
        posicoes = []
        for i in range(linhas):
            for j in range(colunas):
                if self.tabela[i, j] == 0:
                    posicoes.append((i, j))
        return posicoes


class Jogo:
    def __init__(self, tabela):
        self.tabela = tabela

    def renderizar(self):
        for i in range(linhas):
            print('-' * 12)
            out = '|'
            for j in range(colunas):
                if self.tabela[i, j] == 1:
                    s = 'X'
                elif self.tabela[i, j] == -1:
                    s = 'O'
                else:
                    s = ' '
                out += s + ' | '
            print(out)
        print('-' * 12)


tabela = [
    [0, 0, 1],
    [1, -1, 1],
    [-1, 0, 0]
]

matriz = np.array(tabela)

rl = RL(matriz)
matriz = rl.qLearning()

jogo = Jogo(matriz)
jogo.renderizar()
