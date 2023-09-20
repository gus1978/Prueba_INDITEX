def saludar(nombre):
    
    "Esta funcion saluda a la persona con el nombre proporcionado."
    mensaje = "Hola, " + nombre + "!"
    return mensaje

saludo = saludar("Juan")

print(saludo)