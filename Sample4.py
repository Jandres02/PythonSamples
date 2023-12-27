class A():
    pass

class atlantico(A):
	def capital(self):
		print("La capital del Atlantico es Barranquilla.")

	def population(self):
		print("La poblacion en Atlantico es de 2.536 millones de personas.")


class cundinamarca(atlantico):
	def capital(self):
		print("La capital de Cundinamarca es Bogotá.")

	def population(self):
		print("La población en Cundinamarca es de 2.919 milones de personas.")

busqueda = cundinamarca()
busqueda.capital()
busqueda.population()
