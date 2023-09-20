class VerificadorDeMascotas:
    def __init__(self, mascotas):
        self.mascotas = mascotas

    def contar_mascotas_con_mismo_nombre(self):
        resultado = {}
        
        for nombre, cantidad in self.mascotas.items():
            if nombre in resultado:
                resultado[nombre] += cantidad
            else:
                resultado[nombre] = cantidad
        
        return resultado

mascotas = {
    "William": 5,
    "Floyd": 2,
    "William": 6,
    "Juan": 10,
    "Pedro": 5,
    "Carlos": 3
}

contador = VerificadorDeMascotas(mascotas)

# Contar las mascotas con el mismo nombre
resultado = contador.contar_mascotas_con_mismo_nombre()

# Mostrar el resultado
print("resultado:", resultado)
