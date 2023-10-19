"https://replit.com/join/wvynrzdoue-fernandaportil3"
"""
Pre diagnostico de Enfermedades Respiratorias
"""
#datos paciente
temperatura = float(input("Cuál es tu temperatura?(En Celsius):"))
dias = float(input("Cantidad de días enfermo:"))
sintomas = input("Cuáles son los síntomas?:")

#fiebre
if temperatura <= 36.5:
  print("No tiene fiebre")
elif temperatura < 36.5 > 38:
  print("Fiebre baja")
elif temperatura >= 38:
  print("Fiebre Alta")

#Enfermedad cronica
if dias >= 7 and sintomas == "tos":
  print("Enfermedad Crónica")

#Infeccion respiratoria
if temperatura < 36 < 36.6 and sintomas == "tos":
  print("Infeccion respiratoria leve")
elif temperatura > 36.6 < 38 and sintomas == "tos" or "dolor de garganta":
  print("Infeccion respiratoria media")
elif temperatura > 38 and sintomas == "tos" or "dificultad para respirar":
  print("Infeccion respiratoria grave")
  
