from cliente import Cliente
from cadastro_cliente import CadastroCliente


def test_cliente_cadastrado():
    cliente = Cliente('Ana', 20, 'anajuliasantinoni15@gmal.com')
    cadastro_cliente = CadastroCliente()
    resposta = cadastro_cliente.cadastrar_cliente(cliente)
    assert "Cadastrado com sucesso" == resposta


def test_menor_de_idade():
    cliente = Cliente('Ana', 17, 'anajuliasantinoni15@gmal.com')
    cadastro_cliente = CadastroCliente()
    resposta = cadastro_cliente.cadastrar_cliente(cliente)
    assert "Cliente menor de idade" == resposta


def test_email_valido():
    cliente = Cliente('Ana', 18, 'teste erro')
    cadastro_cliente = CadastroCliente()
    resposta = cadastro_cliente.cadastrar_cliente(cliente)
    assert "Email invalido" == resposta
