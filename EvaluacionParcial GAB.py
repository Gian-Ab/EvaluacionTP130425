# Objetivo: Evaluacion Parcial
# Nombre : Añasco Bendezu Giancarlos
# Fecha: 13/04/25

print("IE MI PAIS - Recolecta 5to Año")
while(True):
    menu=int(input("""
****** MENU DE OPCIONES ******
                   
1. AUTENTICARSE
2. REGISTRAR DONACIONES
3. CALCULADORA
4. REPORTE TOTAL
5. SALIR DEL PROGRAMA
                   
Ingrese una opcion: """))
    
    if(menu ==1):
        while (True):
            contraseña=71383436
            
            usuario=str(input("Ingrese su usuario (Apellido Paterno): "))
            contraseñaIngre=int(input("Ingrese Contraseña: "))
            if (contraseñaIngre==contraseña):
                break
            else:
                print("ERROR la contraseña no es valida")
            
    while(True):
        menu=int(input("""
****** MENU DE OPCIONES ******
                   
2. REGISTRAR DONACIONES
3. CALCULADORA
4. REPORTE TOTAL
5. SALIR DEL PROGRAMA

Ingrese una opcion: """))
        if(menu ==2):
            seccion=str(input("Ingrese su sección A/B/C/D: ")).upper()
            while(True):
                if seccion in ("A", "B", "C", "D"):
                    break
                else:
                    print("ERROR Ingrese una seccion valida A/B/C/D")
            
            varACU1 = 0 
            varACU2 = 0  
            varACU3 = 0  
            varACU4 = 0  
            varACU5 = 0  
            varACU6 = 0  
            varACU7 = 0  
            varACU8 = 0  

            n = int(input("Ingrese el numero de alumnos: "))
            if n > 0:
                i = 0
                while i < n:
                    print(f"\nAlumno {i+1}:")
                    
                    ApellidoAlum = input("Ingrese apellido paterno del alumno: ")
                    
                    while True:
                        DniAlum = int(input("Ingrese el DNI del alumno: "))
                        if 9999999< DniAlum < 99999999:
                            break
                        print("ERROR: El número de DNI no es válido")
                    
                    while True:
                        GeneroAlum = input("Ingrese el sexo del alumno M/F: ").upper()
                        if GeneroAlum in ["M", "F"]:
                            break
                        print("ERROR: género inválido, ingrese solo M ó F")
                    
                    while True:
                        respuesta = input("¿El alumno usa lentes? SI/NO: ").upper()
                        if respuesta in ("SI", "NO"):
                            UsoLentes = (respuesta == "SI")
                            break
                        print("ERROR: Ingresa solo SI o NO")
                    
                    while True:
                        edadAlum = int(input("Ingresar edad del alumno: "))
                        if 13 <= edadAlum <= 18:
                            menorEdad = int(edadAlum < 18)
                            mayorEdad = int(edadAlum == 18)
                            break
                        print("ERROR: La edad no es correcta (solo entre 13 y 18)")
                    
                    while True:
                        MontoAlumn = float(input("Ingresa el monto de tu donación: "))
                        if MontoAlumn > 0:
                            print("GRACIAS por tu donación de:", MontoAlumn)
                            break
                        print("ERROR: Ingrese un monto positivo")
                                        
                        break
                    
                    varACU1 = varACU1 +(GeneroAlum == "M")
                    varACU2 = varACU2 +(GeneroAlum == "F")
                    varACU3 = varACU3 +(GeneroAlum == "M" and UsoLentes)
                    varACU4 = varACU4 +(GeneroAlum == "F" and UsoLentes)
                    varACU5 = varACU5 +(not UsoLentes)
                    varACU6 = varACU6 +menorEdad
                    varACU7 = varACU7 + mayorEdad
                    varACU8 = varACU8 + MontoAlumn

                    i += 1
            else:
                    print("ERROR Ingrese solo numeros positivos")
        
        elif(menu ==3):
            while(True):
                menu=int(input("""
****** MENU DE OPCIONES ******
1. SUMA DE DOS NUMEROS       
2. RESTA DE DOS NUMEROS
3. MULTIPLICACION DE DOS NUMEROS
4. DIVICION DE DOS NUMEROS
5. MODULO DE DOS NUMEROS
6. SALIR AL MENU PRINCIPAL                               
                  
Ingrese una opcion: """))
                if (menu ==1):
                    while True:
                        a=float(input("Ingrese numero 1: "))
                        if (a>0):
                         break
                        print ("Digite un numero positivo")
                    while True:
                        b=int(input("Ingrese numero 2: "))
                        if (b>0):
                         break
                        print ("Digite un numero positivo")
                    suma=a+b
                    print("La suma es: ",suma)
                elif (menu ==2):
                    while True:
                        a=float(input("Ingrese numero 1: "))
                        if (a>0):
                         break
                        print ("Digite un numero positivo")
                    while True:
                        b=float(input("Ingrese numero 2: "))
                        if (b>0):
                         break
                        print ("Digite un numero positivo")
                    resta=a-b
                    print("La resta es: ",resta)
                elif (menu ==3):
                    while True:
                        a=float(input("Ingrese numero 1: "))
                        if (a>0):
                         break
                        print ("Digite un numero positivo")
                    while True:
                        b=float(input("Ingrese numero 2: "))
                        if (b>0):
                         break
                        print ("Digite un numero positivo")
                    multiplicacion=a*b
                    print("La multiplicacion es: ",multiplicacion)
                elif (menu ==4):
                    while True:
                        a=float(input("Ingrese numero 1: "))
                        b=float(input("Ingrese numero 2: "))
                        if b!=0:
                            divicion=a/b
                            print("La divicion es: ", divicion)
                            break
                        else:
                            print("ERROR no se puede dividor entre cero")
                            
                elif (menu ==5):
                    while True:
                        a=float(input("Ingrese numero 1: "))
                        if (a>0):
                         break
                        print ("Digite un numero positivo")
                    while True:
                        b=float(input("Ingrese numero 2: "))
                        if (b>0):
                         break
                        print ("Digite un numero positivo")
                    modulo=a%b
                    print("El modulo (MOD) es: ",modulo)

                elif (menu ==6):
                    break
                else:
                    print("Opción no válida, intente de nuevo.")
                
                

        elif(menu ==4):
            print("****** REPORTE TOTAL ******")
            print("La cantidad de alumnos masculinos ingresados es: ", varACU1 )
            print("La cantidad de alumnas femeninas ingresadas es: ", varACU2)
            print("La cantidad de alumnos con lentes son: ", varACU4)
            print("La cantidad de alumnas con lentes son: ", varACU3)
            print("La cantidad de alumnas y alumnos SIN lentes son: ", varACU5)
            print("La cantidad de alumnos menores de edad son: ", varACU6)
            print("La cantidad de alumnos mayores de edad son: ", varACU7)
            print("La seccion ingresada fue: ", seccion)
            print("El monto total recaudado es: ", varACU8)
            print("El monto total recaudado - refrigerio del experto (s/50) es: ", varACU8-50)
            print("El monto neto total recaudado es: ", varACU8-50)

        elif(menu ==5):
            print("Esta saliendo de TECNICAS DE PROGRAMACION :P :()")
            break
        
        else:
            print("Opción no válida, intente de nuevo.")



            

                    

    









