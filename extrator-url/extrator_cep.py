endereco = "Rua dos Bobos, apartamento 1010101, Maceeiras, Rio de Novembro, RN, 45664-410"

import re

padrao = re.compile("[0-9]{5}[-]?[0-9]{3}")
busca = padrao.search(endereco)  # Match
if busca:
    cep = busca.group()
    print(cep)
