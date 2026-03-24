from carro_alugado import Carro_Alugado

class Locadora:
    def __init__(self, nome_locadora: str):
        self.nome_locadora = nome_locadora

    def determine_valor_aluguel(self, carro_alugado: Carro_Alugado):
        return carro_alugado.forneca_valor_aluguel() 
