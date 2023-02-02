

#Aqui llevaremos acabo el primer proyecto con python
#tenemos que hacer unos inputs para un calculo del imc 
#la formula del IMC es =  Peso / estatura2   -> Peso sobre estatura al cuadrado

#Que datos vamos a pedir? 

#El programa no puede permitir que ningún dato quede vacío, además de asegurarse de que en los campos de edad, peso y estatura el usuario introduzca una cifra. Todo esto antes de proceder con el cálculo del IMC siguiendo la fórmula:


nombre = input("Escribe tu nombre: ")
apellidoDad = input("Escribe tu apellido paterno: ")
apellidoMom = input("Escribe tu apellido materno: ")
edad = int(input("Escribe tu edad: "))
peso = int(input("Escribe tu peso: "))
estatura = float(input("Escribe tu estatura: "))



#ejemplo de concateacion donde juntamos todos los datos recabados
print("Hola, " + nombre + " " + apellidoDad + " " + apellidoMom + "." + " tienes"+ " " + str(edad) + " años" + "," + " tu peso es " + str(peso) + " kg " + "y tu estatura es de " + str(estatura) + "mts")

if (edad < 18):
    print("Usted es menor de edad")
else:
    print("Usted es mayor de edad")

#Asignamos la variable de imc
imc = peso / estatura**2

print("Tu IMC es de: " + str(imc))
