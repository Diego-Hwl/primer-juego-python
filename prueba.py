
def mostrar_estado(e):
    print(f"\n[ ENERGÍA ACTUAL: {'■' * e}{'□' * (5-e)} ({e}/5) ]")

def caminar(e):
    if e > 0:
        print(">> Caminas por el bosque...")
        return e - 1
    return e

def descansar(e):
    if e < 5:
        print(">> Descansas un rato y recuperas fuerzas.")
        return e + 1
    print(">> Ya estás totalmente descansado.")
    return e


energia = 3

while energia > 0:
    mostrar_estado(energia)
    accion = input("¿Qué quieres hacer? (caminar/descansar/salir): ").lower()
    
    if accion == "caminar":
        energia = caminar(energia)
    elif accion == "descansar":
        energia = descansar(energia)
    elif accion == "salir":
        print("Saliendo del juego...")
        break 
    else:
        print("Comando no válido.")

print("\n--- JUEGO TERMINADO ---")