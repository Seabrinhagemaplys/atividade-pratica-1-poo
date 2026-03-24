class FazBolo:
    def __init__(self, massa: str, recheio: str, cobertura: str):
        self.massa = massa
        self.recheio = recheio
        self.cobertura = cobertura

    def assar(self, temperatura: str, tempo: int):
        if temperatura != "alto" and temperatura != "medio" and temperatura !="baixo":
            print("Entrada inválida! Esse forno é limitado")
            return
        
        if tempo < 0 or tempo > 200:
            print("Tempo inválido!!")   
            return 
        
        print(f"Você está querendo assar o bolo de {self.massa} com recheio de {self.recheio} e cobertura de {self.cobertura} no fogo {temperatura} por {tempo} minutos")
        
        match (temperatura):
            case "alto":
                if tempo > 10:
                    print("Cuidado para não queimar!")
                elif tempo < 10:
                    print("Cuidado, o bolo vai ficar cru e ruim!")
            case "médio":
                if tempo > 30:
                    print("Cuidado para não queimar!")
                elif tempo < 45:
                    print("Cuidado, o bolo vai ficar cru e ruim!")
            case "baixo":
                if tempo > 45:
                    print("Cuidado para não queimar!")
                elif tempo < 45:
                    print("Cuidado, o bolo vai ficar cru e ruim!")
