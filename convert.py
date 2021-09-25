#!/usr/bin/env python3
# Eva Luna Alvarez Calderon 2do Semestre Practica 4
# Espero sirva
print("Hola! Soy una calculadora de bases!")
print("Espero que te diviertas convirtiendo. ")


print("\n")


def cambio_base(numerito, base):
    # converter va a guardar los residuos que vayan quedando.
    converter = ''
    # mientras decimal / base no sea igual a  el ciclo descrito abajo se ejecutara.
    while numerito // base != 0:
        # converter es igual numerito entre la base a la que se quiere convertir el numerito.
        # se concatena el residuo guardado en converter para dar el resultado correcto
        converter = str(numerito % base) + converter
        # numerito va a ser igual a el numerito a convertir entre la base en la que se quiera convertir
        numerito = numerito // base
    # el valor que tenga numerito al final se concatenara con lo que haya en converter para dar el resultado.
    return str(numerito) + converter

# Dato curioso si por ejemplo fueras a convertir 5 a binario, la suma de los cocientes mas la suma de los residuos da como resultado el numero a convertir
# mind blown


numero = int(input("Introduce el numero a convertir: "))
base = int(input("Introduce la base: "))
print("El Resultado es el siguiente: ")
print(cambio_base(numero, base))
print("\n")
print("Gracias por convertir con Pyxerter")
print("Por LordVlads77")
print("PD: Tu sabes quien soy")
