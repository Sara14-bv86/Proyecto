Este es mi proyecto del curso.

*leer un archivo
*Imprimir el contenido

Autor: Sarai Bata Ventura


# Instalar colorama 
pip install colorama

# Colorama 
import colorama
from colorama import Fore, Style

def leer_datos_archivo(archivo_csv):

   # Verificar si el IMC está fuera de rango (> 30)
    if paciente['IMC'] > 30:
        imc_str = Fore.RED + Style.BRIGHT + f"{paciente['IMC']:.2f}" + Style.RESET_ALL
    else:
        imc_str = f"{paciente['IMC']:.2f}"
    
   # Verificar si existe alguna otra alerta de salud
    
    diabetes_str = Fore.RED + Style.BRIGHT+ paciente['Diabetes'] + Style.RESET_ALL if paciente['Diabetes'] == 'Si' else paciente['Diabetes']
    hipertension_str = Fore.RED + Style.BRIGHT+ paciente['Hipertensión'] + Style.RESET_ALL if paciente['Hipertensión'] == 'Si' else paciente['Hipertensión']
    depresion_str = Fore.RED + Style.BRIGHT+ paciente['Depresión'] + Style.RESET_ALL if paciente['Depresión'] == 'Si' else paciente['Depresión']
    trastorno_sueno_str = Fore.RED + Style.BRIGHT + paciente['Trastorno del sueño'] + Style.RESET_ALL if paciente['Trastorno del sueño'] == 'Si' else paciente['Trastorno del sueño']
    trastorno_alimentacion_str = Fore.RED+ Style.BRIGHT + paciente['Trastorno de la alimentación'] + Style.RESET_ALL if paciente['Trastorno de la alimentación'] == 'Si' else   
    paciente['Trastorno de la alimentación']
    
    print(f"{'Paciente':>24} :  {paciente['ID']:>3}")
    print(f"{'Sexo':>24} :   {paciente['Sexo']}")
    print(f"{'Edad':>24} :  {paciente['Edad']}")
    print(f"{'Peso':>24} :  {paciente['Peso']}")
    print(f"{'Estatura':>24} : {paciente['Estatura']}")
    print(f"{'IMC':>24} : {imc_str}")
    print(f"{'Diabetes':>24} :  {diabetes_str}")
    print(f"{'Hipertensión':>24} :  {hipertension_str}")
    print(f"{'Depresión':>24} :  {depresion_str}")
    print(f"{'Trastorno del sueño':>24} :  {trastorno_sueno_str}")
    print(f"{'Trastorno de la alimentación':>24} :  {trastorno_alimentacion_str}")
    print(45 * chr(0x2015))
    
# Busca pacientes por sus IDs y muestra la información
def buscar_pacientes(pacientes, ids_buscados):

 # Checamos si el id está en la lista de los solicitados
    
    for id_buscado in ids_buscados:
        encontrado = False
        for paciente in pacientes:
            if paciente['ID'] == id_buscado:
                mostrar_informacion_paciente(paciente)
                encontrado = True
                break
        if not encontrado:
            print(Fore.RED+ Style.BRIGHT + f"No se encontró ningún paciente con ID: {id_buscado}")
            print(45 * chr(0x2015))

# Solicita los IDs de los pacientes 
def obtener_datos_entrada():

# Solicita los IDs de los pacientes y los convierte a enteros
    ids_input = input("ID. pacientes (separados por coma): ").split(',')
    # Convertir a enteros, manejando posibles errores de entrada
    IDs = []
    for id_str in ids_input:
        try:
            IDs.append(int(id_str.strip()))  # Convertir cada ID a entero, eliminando espacios en blanco
        except ValueError:
            print(Fore.RED + Style.BRIGHT+ f"Error: '{id_str}' no es un ID válido. Se omitirá.")
    # Regresar una lista ordenada y sin repeticiones
    return sorted(set(IDs))

# Nombre del archivo CSV
archivo_csv = 'personal_data.csv'

# Leer los datos del archivo
pacientes = leer_datos_archivo(archivo_csv)

# Mostrar encabezado del sistema
print(45 * chr(0x2015))

print("                   Sistema XYZ                    ")

print(45 * chr(0x2015))

# Obtener los IDs de los pacientes
ids_buscados = obtener_datos_entrada()

# Mostrar línea de separación
print(45 * chr(0x2015))

# Buscar y mostrar información de los pacientes
buscar_pacientes(pacientes, ids_buscados)

    
    