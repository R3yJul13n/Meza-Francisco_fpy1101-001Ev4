#prueva Evaluación Parcial N° 4 
nombres=[]
sexo=[]
opcion = 1
contraseña=[]
while (opcion >=1 and opcion <=4):
    print("""MENU PRINCIPAL
1.- Ingresar usuario.
2.- Buscar usuario.
3.- Eliminar usuario.
4.- Salir.""")
    opcion=int(input('ingrese opción: '))

    if opcion == 1:
        if nombres:
            nombres=int(input('Ingrese nombre de usuario: '))
            if sexo:
                sexo=int(input('Ingrese sexo: '))
                if contraseña:
                    contraseña=int(input("Ingrese contraseña: "))
                elif contraseña:
                    print("printContraseña valida.")   
            elif sexo:
                print("Debe ingresar M o F solamente. Intente de nuevo.")
        elif nombres:
            print("Usuario ya existe. Intento otro.")

    elif opcion ==2:
        nombres=int(input('Ingrese usuario a buscar: '))
        print(f"El sexo del usuario es: {sexo} y la contraseña es: {contraseña}")
        if nombres in nombres:
            print("El usuario no se encuentra")
        

    elif opcion ==  3:
        nombres=int(input('Ingrese usuario a buscar: '))
        if nombres in nombres:
            nombres.remove(nombres)
            print("Usuario eliminado con éxito!")
        else:
            print("No se pudo eliminar usuario!")
    else:
        print('Programa terminado...')
else:
    print('Programa terminado...')
   