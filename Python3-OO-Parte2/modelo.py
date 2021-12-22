class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    def __str__(self):
        return f'{self.nome} - {self.ano} - Like(s): {self.likes}'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self.nome_classe()} {self.nome}: - {self.ano} - Duração: {self.duracao} - Like(s): {self.likes}'

    @staticmethod
    def nome_classe():
        return "Filme"


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self.nome_classe()}: {self.nome} - {self.ano} - Temporadas: {self.temporadas} - Like(s): {self.likes}'

    @staticmethod
    def nome_classe():
        return "Série"


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome.title()
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)

    @property
    def listagem(self):
        return self._programas


homem_aranha = Filme("Homem-aranha: Sem volta para casa", 2021, 148)
homem_aranha.dar_like()
homem_aranha.dar_like()
homem_aranha.dar_like()
homem_aranha.dar_like()

big_bang = Serie("The Big Bang Theory", 2007, 12)
big_bang.dar_like()

super_bad = Filme("Superbad - é hoje", 2007, 113)
super_bad.dar_like()
super_bad.dar_like()

hora_avetura = Serie("Hora de aventura", 2010, 10)
hora_avetura.dar_like()
hora_avetura.dar_like()
hora_avetura.dar_like()

filmes_e_series = [homem_aranha, big_bang, super_bad, hora_avetura]

playlist_fim_de_semana = Playlist("Fim de semana", filmes_e_series)

print(f"Quantidade de programas na Playlist {playlist_fim_de_semana.nome}: {len(playlist_fim_de_semana)}\n")

for programa in playlist_fim_de_semana:
    print(programa)

print(f"Super Bad está na lista? {super_bad in playlist_fim_de_semana}")
