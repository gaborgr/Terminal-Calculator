print(
    """
Bienvenido a la Calculadora de Gabo
          Version 1.0
 las operaciones son las siguientes

- Suma        (S)
- Resta       (R)
- Multiplicar (M)
- Dividir     (R)

"""
)

resultado = ""

while True:
    if not resultado:
        resultado = input("Ingresa el primer numero: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input("Selecciona la operacion que deseaas realizar (S,R,M,D) =>: ")
    if op.lower() == "salir":
        break
    n2 = input("Ingresa el segundo numero: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if op.lower() == "s":
        resultado += n2
    elif op.lower() == "r":
        resultado -= n2
    elif op.lower() == "m":
        resultado *= n2
    elif op.lower() == "d":
        resultado /= n2
    else:
        print("Seleccion incorrecta")
        break

    print(f"El resultado es {resultado}")
