#Fernanda Portillo Ortiz

puntuacion = input("Escribe tu calificacion del examen:")
asignaciones = input("escribe tus asignaciones completadas:")
participacion = input("Participaste en clase (Si/No):")

if puntuacion > 80 and asignaciones > 5 and participacion == "si":
  print("Tienes calificacion aprobatoria")

elif puntuacion > 70 and participacion == "si": 
  print("Apruebas")

else:
  print("no apruebas")
