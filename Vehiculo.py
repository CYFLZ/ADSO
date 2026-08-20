class Vehiculo: 

    def __init__(self,marca, modelo,color,valor, ref, placa, propietario):
        self.marca  = marca
        self.modelo = modelo
        self.color  = color
        self.valor  = valor
        self.ref    = ref
        self.placa  = placa
        self.propietario  = propietario # objeto de tipo persona

    def calcularImpuesto(self):
        return self.valor * 0.02
         