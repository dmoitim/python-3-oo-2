class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def imprimir(self):
        pass


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def imprimir(self):
        print(
            f"{self._nome} ({self.ano}) - Duração: {self.duracao} min. - Likes: {self._likes}")


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def imprimir(self):
        print(
            f"{self._nome} ({self.ano}) - Temporadas: {self.temporadas} - Likes: {self._likes}")


vingadores = Filme('vingadores: guerra infinita', 2018, 160)
vingadores.dar_like()

vikings = Serie('vikings', 2013, 6)
vikings.dar_like()
vikings.dar_like()

filmes_e_series = [vingadores, vikings]

for programa in filmes_e_series:
    # detalhes = programa.duracao if (
    #    hasattr(programa, 'duracao')) else programa.temporadas
    #print(f"{programa.nome} ({programa.ano}) - {detalhes} - Likes: {programa.likes}")
    programa.imprimir()
