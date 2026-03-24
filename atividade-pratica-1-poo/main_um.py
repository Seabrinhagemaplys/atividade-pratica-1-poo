from bolo import Bolo

bolo1 = Bolo('Bolo de cenoura caseiro', 'cenoura', 'farinha', True)
bolo2 = Bolo('Bolo de chocolate industrial', 'chocolate', 'pão de ló', False)
bolo3 = Bolo(bolo1.nome, bolo1.recheio, bolo1.massa, (not bolo1.tem_cobertura))

print(f'bolo1: {bolo1.tem_cobertura}, bolo2: {bolo2.tem_cobertura}, bolo3: {bolo3.tem_cobertura}')
