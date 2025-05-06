def calcula_multa(excedente):
    multa = excedente * MULTA_KG
    return multa


MULTA_KG = 4.0
QUILOS_PERMITIDOS = 100

peso_pescado = float(input("Informe o peso: "))
# calcula peso
if peso_pescado > QUILOS_PERMITIDOS:
    excedente = peso_pescado - QUILOS_PERMITIDOS
    vl_multa = calcula_multa(excedente)
    print(f' O valor da multa é {vl_multa}')
else:
    print(f'Sem multa a pagar')