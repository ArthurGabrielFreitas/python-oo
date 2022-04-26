import re

class TelefonesBr:
    def __init__(self, telefone):
        if self.valida_telefone(telefone):
            self.numero = telefone
            print("Tudo certo!")
        else:
            raise ValueError("Número de telefone inválido!")

    def valida_telefone(self, telefone):
        padrao = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
        resposta = re.search(padrao, telefone)
        if resposta:
            return True
        else:
            return False