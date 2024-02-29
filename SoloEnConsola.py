import re

entrada_usuario = input("Ingrese una cadena: ")

expresion_regular_1 = re.compile(r'^(c(u(a(y)?)?)?)?$', re.IGNORECASE)

if expresion_regular_1.match(entrada_usuario):
    print(f'{entrada_usuario} - Primera Expresion Valida')
else:
    print(f'{entrada_usuario} - Primera Expresion no valida')

expresion_regular_2 = re.compile(r'^C(uay)*$', re.IGNORECASE)

if expresion_regular_2.match(entrada_usuario):
    print(f'{entrada_usuario} - Segunda Expresion Valida')
else:
    print(f'{entrada_usuario} - Segunda Expresion no valida')

expresion_regular_3 = re.compile(r'^C(?=.*u)(?=.*a)(?=.*y)(?!.*(.).*\1)[uay]+$', re.IGNORECASE)

if expresion_regular_3.match(entrada_usuario):
    print(f'{entrada_usuario} - Tercera Expresion Valida')
else:
    print(f'{entrada_usuario} - Tercera Expresion no valida')
