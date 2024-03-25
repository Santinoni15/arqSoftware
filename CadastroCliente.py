class CadastroCliente:
    def __init__(self):
        self.clientes_cadastrados = []

    def cadastrar_cliente(self, cliente):
        self.clientes_cadastrados.append(cliente)

        if len(self.clientes_cadastrados) > 0: #conferir se esta realmente cadastrando.
            return "Cadastrado com sucesso"
