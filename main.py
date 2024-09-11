from Calificaciones_Num_Lit import Calificaciones

if __name__ == '__main__':
    operacion = Calificaciones()
    calificacion = operacion.ingresoCalificacion()
    print(f"La calificación literal es: {operacion.calificacionLiteral(calificacion)}")
