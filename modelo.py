class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()


class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()


vingadores = Filme('vingadores: guerra infinita', 2018, 160)
vingadores.dar_like()
print(f"{vingadores.nome} ({vingadores.ano}) - Duração: {vingadores.duracao} - Likes: {vingadores.likes}")

vikings = Serie('vikings', 2013, 6)
vikings.dar_like()
vikings.dar_like()
print(f"{vikings.nome} ({vikings.ano}) - Temporadas: {vikings.temporadas} - Likes: {vikings.likes}")
