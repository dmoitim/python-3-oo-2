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


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas


vingadores = Filme('vingadores: guerra infinita', 2018, 160)
vingadores.dar_like()
print(f"{vingadores.nome} ({vingadores.ano}) - Duração: {vingadores.duracao} - Likes: {vingadores.likes}")

vikings = Serie('vikings', 2013, 6)
vikings.dar_like()
vikings.dar_like()
print(f"{vikings.nome} ({vikings.ano}) - Temporadas: {vikings.temporadas} - Likes: {vikings.likes}")
