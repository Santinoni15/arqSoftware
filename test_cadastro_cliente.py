def test_cliente_cadastrado();
    cliente = Cliente()
    cadastro_cliente = CadastroCliente()
    resposta = cadastro_cliente.cadastrar_cliente(cliente)
    assert "Cadastrado com sucesso" == resposta