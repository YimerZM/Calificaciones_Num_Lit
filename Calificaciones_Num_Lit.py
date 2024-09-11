class Calificaciones:
    def ingresoCalificacion(self):
        calificacion = float(input("Ingrese la calificación numérica (0-100): "))
        return calificacion

    def calificacionLiteral(self, calificacion):
        if calificacion >= 90:
            return "A"
        elif calificacion >= 80:
            return "B"
        elif calificacion >= 70:
            return "C"
        elif calificacion >= 60:
            return "D"
        else:
            return "F"

if __name__ == '__main__':
    operacion = Calificaciones()
    calificacion = operacion.ingresoCalificacion()
    print(f"La calificación literal es: {operacion.calificacionLiteral(calificacion)}")
