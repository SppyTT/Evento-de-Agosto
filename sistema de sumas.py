def main():

    num_1 = int(input("Introduzca el primer número que quiera sumar: "))

    num_2 = int(input("Introduzca el segundo número que quiera sumar:"))

    veces_a_sumar = int(input("Introduzca el número de veces que quiere sumar los dos números: "))

    if veces_a_sumar<0:
        print("El número de veces a sumar no puede ser negativo.")

    elif num_1<= 0 or num_2 <= 0 :
        print("¡Dije números naturales!")
    else:
        suma_de_los_dos_numeros= num_1 + num_2
        print(suma_de_los_dos_numeros * veces_a_sumar)

if __name__ == "__main__":

    main()