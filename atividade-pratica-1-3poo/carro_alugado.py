class Carro_Alugado:
    def __init__(self, modelo: str, quantidade_dias: int, kilometros_rodados: float):
        self.modelo = '' 
        self.quantidade_dias = 0
        self.kilometros_rodados = 0
        
        if quantidade_dias < 0 or not isinstance(quantidade_dias, int):
            return
        if kilometros_rodados < 0 or not isinstance(kilometros_rodados, int):
            return


        self.kilometros_rodados =  kilometros_rodados
        self.quantidade_dias =quantidade_dias
        self.modelo = modelo
        

    def forneca_valor_aluguel(self):
        valor_kilometro: float = self.kilometros_rodados * 0.8
        valor_dia: float = self.quantidade_dias * 120
        return valor_kilometro + valor_dia
