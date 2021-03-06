# hipoteca.py

# Alumna: Julieta Bloise

# Ejercicio 1.11:
# Corregí el código anterior de forma que el pago del último mes se ajuste a lo adeudado.

pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 1

while saldo > 0:
    if (mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin):
        print("Entro al if")
        saldo = saldo * (1+tasa/12) - pago_mensual - pago_extra
        total_pagado = total_pagado + pago_mensual + pago_extra
    else:
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual
    
    if (saldo < 0):
        total_pagado = total_pagado + saldo
        saldo = 0

    print(mes, round(total_pagado, 2), round(saldo, 2))
    mes = mes + 1
    
print('Total pagado', round(total_pagado, 2))
print('Meses: ', mes-1)