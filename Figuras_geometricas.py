import math # Importamos math para poder operar con ciertos términos

# Definición de la clase Círculo
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio**2

    def perimetro(self):
        return 2 * math.pi * self.radio

# Definición de la clase Rectángulo
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

# Definición de la clase Cuadrado 
class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado**2

    def perimetro(self):
        return 4 * self.lado

# Definición de la clase Triángulo Rectángulo
class TrianguloRectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return 0.5 * self.base * self.altura

    def perimetro(self):
        return self.base + self.altura + self.hipotenusa()

    def hipotenusa(self):
        return math.sqrt(self.base**2 + self.altura**2)

    def tipo_triangulo(self):
        if self.base == self.altura:
            return "Triángulo Equilátero"
        elif self.base == self.altura or self.base**2 + self.altura**2 == self.hipotenusa()**2:
            return "Triángulo Isósceles"
        else:
            return "Triángulo Escaleno"

# Ejemplo de uso
circulo = Circulo(5) # Su radio es en cm
rectangulo = Rectangulo(4, 6) # Sus valores corresponden a su base y su altura respectivamente
cuadrado = Cuadrado(4) # Corresponde a un lado del cuadrado
triangulo = TrianguloRectangulo(3, 4) # Corresponde a la base y la altura

print("Área del círculo:", circulo.area())
print("Perímetro del círculo:", circulo.perimetro())

print("Área del rectángulo:", rectangulo.area())
print("Perímetro del rectángulo:", rectangulo.perimetro())

print("Área del cuadrado:", cuadrado.area())
print("Perímetro del cuadrado:", cuadrado.perimetro())

print("Área del triángulo rectángulo:", triangulo.area())
print("Perímetro del triángulo rectángulo:", triangulo.perimetro())
print("Hipotenusa del triángulo rectángulo:", triangulo.hipotenusa())
print("Tipo de triángulo:", triangulo.tipo_triangulo())
triangulo.tipo_triangulo()
