from cpf_cnpj import Documento
from telefones_br import TelefonesBr
from cadastro import Cadastro
from acesso_cep import BuscaEndereco

# Documento.cria_documento(documento) recebe uma sequência de números e retorna um objeto CPF ou CNPJ.
cpf = Documento.cria_documento(66666666666)  # 11 dígitos
cnpj = Documento.cria_documento("11111111111111")  # 14 dígitos

print(f"São documentos válidos: {cpf} (CPF) e {cnpj} (CNPJ).\n")

# TelefonesBr recebe um número de telefone, que deve ter o DDD, pode ter 8 ou 9 números no corpo
# e pode ou não ter três dígitos de identificação do país.
telefone1 = TelefonesBr("22222222222")
telefone2 = TelefonesBr("8888888888888")

print(f"São telefones válidos: {telefone1} e {telefone2}.\n")

# Cadastro simula um cadastro com a data e hora atual para fazer testes.
cadastro = Cadastro()

print(f'O cadastro foi realizado em {cadastro}.\n'
      f'O dia é {cadastro.dia_cadastro()} e o mês é {cadastro.mes_cadastro()}.\n'
      f'O cadastro deve ser atualizado em {cadastro.data_atualizar_cadastro()}.\n')

# BuscaEndereco recebe os dígitos de um CEP e realiza a consulta em uma API para verificar se é válido.
cep = BuscaEndereco(78945612)
uf, cidade, bairro = cep.acessa_via_cep()

print(f"É um CEP válido: {cep}.\n"
      f"Endereço: {cidade}, {uf} - {bairro}.\n")
