persona=int(input("ingrese su edad: " ))
if persona<=0:
    print("ingrese un numero entero, por favor")

if persona >= 18:
    print("es mayor de edad")

elif persona < 18:
    print("es menor de edad, no puedes ingresar ")

m1=int(input("ingrese un numero"))
m2=int(input("ingrese segundo numero"))
if m1 > m2:
    print(f"{m1} es mayor que {m2}")
else:
    print(f"{m2} es mayor que {m1}")


numero1 = float(input("ingrese primer numero "))
operacion = input("operacion (+,/,*,/):")
numero2 = float(input("ingrese segundo numero "))
if operacion=="+":
    resultado = numero1+numero2
    print(f"resultado : {resultado}")
elif operacion=="-":
    resultado = numero1-numero2
    print(f"resultado: {resultado}")
elif operacion=="*":
    resultado = numero1*numero2
    print(f"resultado: {resultado}")
elif operacion=="/":
    resultado = numero1/numero2
    print(f"resultado: {resultado}")
else:
    print("error: no se puede dividir por cero")







