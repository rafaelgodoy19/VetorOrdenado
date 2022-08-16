class VetorOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = self.capacidade*[0]

    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i])

    def insere(self, valor):

        for i in range(self.ultima_posicao + 1):
            if valor == self.valores[i]:
                return 
        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i] > valor:
                break
            if i == self.ultima_posicao:
                posicao = i + 1

        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x = x - 1
        
        self.valores[posicao] = valor
        self.ultima_posicao = self.ultima_posicao + 1

    def pesquisa(self, valor):
        for i in range(self.ultima_posicao + 1):
            if self.valores[i] == valor:
                return i
        return -1

    def excluir(self, valor):
        posicao = self.pesquisa(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
            self.ultima_posicao = self.ultima_posicao - 1

vetor = VetorOrdenado(8)
vetor.imprime()
print()

vetor.insere(4)
vetor.insere(2)
vetor.insere(2)
vetor.insere(5)
vetor.insere(6)
vetor.insere(7)
vetor.insere(4)
vetor.insere(1)
vetor.insere(2)
vetor.imprime()