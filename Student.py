class Student:

	def __init__(self, nombre, n1, n2):
		self.__nombre = nombre
		if n1 >=1 and n1<=5:
			self.__n1 = n1
		else:
			raise ValueError("Nota Incorrecta")

		self.__n2 = n2
	 	
	def setNombre(self, nombre):
		self.__nombre = nombre

	def setN1(self, nota):
		if nota >=1 and nota<=5:
			self.__n1 = nota
		else:
			raise ValueError("Nota Incorrecta")

	def setN2(self, nota):
		if nota >=1 and nota<=5:
			self.__n2 = nota
		else:
			self.__n2 = 0

	def getNombre(self):
		return self.__nombre

	def getN2(self):
		return self.__n2

	def getN1(self):
		return self.__n1

	def calcularPromedio(self):
		if self.__n1 == 0 :
			return "La nota 1 no esta asignada"
		if self.__n2 == 0 :
			return "La nota 2 no esta asignada"

		return (self.__n1 + self.__n2) / 2

e1 = Student("jose",-4, 0)
try:
    e1.setN1(0)
except ValueError as er:
	print(er)	

print("Holaaaaaaaaa")

