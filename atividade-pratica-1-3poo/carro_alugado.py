class Carro_Alugado:
    def __init__(self, modelo: str = '', quantidade_dias: int =  0, kilometros_rodados: float = 0):
        self.modelo = modelo
        
        if quantidade_dias < 0:
            self.kilometros_rodados = 0
            return
        if kilometros_rodados
        self.quantidade_dias = quantidade_dias
        self.kilometros_rodados =  kilometros_rodados
        

    def forneca_valor_aluguel(self):
        valor_kilometro: float = self.kilometros_rodados * 0.8
        valor_dia: float = self.quantidade_dias * 120
        return valor_kilometro + valor_dia

