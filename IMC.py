#Aqui llevaremos acabo el primer proyecto con python
#tenemos que hacer unos inputs para un calculo del imc 
#la formula del IMC es =  Peso / estatura2   -> Peso sobre estatura al cuadrado

#Que datos vamos a pedir? 

#El programa no puede permitir que ningún dato quede vacío, además de asegurarse de que en los campos de edad, peso y estatura el usuario introduzca una cifra. Todo esto antes de proceder con el cálculo del IMC siguiendo la fórmula:


nombre = input("Escribe tu nombre: ")
edad = int(input("Escribre tu edad: "))
peso = int(input("Escribe tu peso: "))
estatura = float(input("Escribe tu estatura: "))

#ejemplo de concateacion
print(nombre + " tu edad es " + str(edad) + "años")

