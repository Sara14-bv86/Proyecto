# Proyecto_SBV_Micromonosporaceae_families

# Importación de bibliotecas 

import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns

# Lectura de acrchivo y creación de dataframe

Micro_fam = pd.read_csv ('Actinobacterias.csv', sep ='\t')

Micro_fam

# Análisis exploratorio general

# Agrupación de los datos por familas y tipos de BGC

#Generación de ocurrencias de cada tipo de BGC por género

occurrences = Micro_fam.groupby(["#Genus", "BGC type"]).size().reset_index(name="Occurrences")

# Guardar en un nuevo archivo CSV
occurrences.to_csv('BGC_por_género.csv', index=False)

print("Los datos han sido guardados en BGC_por_género.csv")

occurrences

# Construccion de la grafica de calor para visulaizar los BGC por familia para identificar los géneros de interés y su potencial bisintético
pivot = occurrences.pivot(index="BGC type", columns="#Genus", values="Occurrences")
plt.figure(figsize=(8, 10))
sns.heatmap(pivot, cmap="coolwarm")

# Guardar la gráfica en un archivo PDF
plt.savefig("actinobacterias_heatmap.pdf", format="pdf", bbox_inches="tight")
print("La gráfica se ha guardado en actinobacterias_heatmap.pdf")
plt.show()

# Construcción de gráfica y filtración de datos para la obtención de BGC por cada género 
Salinispora = occurrences.loc[occurrences["#Genus"] == "Salinispora"]
plt.figure(figsize=(18, 5))
sns.scatterplot(Salinispora, x="BGC type", y="Occurrences")
plt.xticks(rotation="vertical")
plt.show()

pip install colorama

# Código para análisis particular para el usuario

# Para probar este código con NCBI accession se sugiere revisar el documento Actinobacterias.csv para obyener ejemplos de NCBI accession number 

# Colorama 

import colorama
from colorama import Fore, Style

# Colores para los BGC types
bgc_colors = {
    'ni-siderophore': Fore.RED + Style.BRIGHT ,
    'lanthipeptide-class-i': Fore.YELLOW + Style.BRIGHT,
    'lanthipeptide-class-ii': Fore.YELLOW + Style.BRIGHT,
    'lassopeptide': Fore.YELLOW + Style.BRIGHT,
    'nrps': Fore.GREEN + Style.BRIGHT,
    'terpene': Fore.MAGENTA + Style.BRIGHT,
    't1pks': Fore.BLUE + Style.BRIGHT,
    't2pks': Fore.BLUE + Style.BRIGHT,
    't3pks': Fore.BLUE + Style.BRIGHT,
    'betalactone': Fore.CYAN + Style.BRIGHT,
    
}
def datos():
    return pd.read_csv('Actinobacterias.csv', sep='\t')

def mostrar_tabla_bgc(df, columna, valor):
    # Mostrar una tabla con la información filtrada por tipo de BGC o número de acceso NCBI
    filtered_df = df[df[columna] == valor]

    if columna == 'NCBI accession':
        print(80 * chr(0x2015))
        print("                 Número de referencia NCBI")
        print(80 * chr(0x2015))
        
        for _, row in filtered_df.iterrows():
            # Obtener el color del tipo de BGC si existe en el diccionario
            bgc_type = row['BGC type']
            color = bgc_colors.get(bgc_type, Fore.RESET)  # Usa Fore.RESET si el tipo no está en bgc_colors

            # Imprimir cada campo con el color aplicable al tipo de BGC
            print(f"{'Género:':<20} {row['#Genus']}")
            print(f"{'Especie:':<20} {row['Species']}")
            print(f"{'Cepa:':<20} {row['Strain']}")
            print(f"{'Tipo de BGC:':<20} {color}{bgc_type}{Style.RESET_ALL}")
            print(f"{'Similitud con clúster conocido:':<20} {row['Most similar known cluster']}")
            print(f"{'Similitud en %:':<20} {row['Similarity in %']}")
            print(f"{'MIBIG_BGC_ID:':<20} {row['MIBiG BGC-ID']}")
            print(80 * chr(0x2015))

    elif columna == 'BGC type':
        # Crear histograma de ocurrencias por tipo de BGC
        #Leer el archivo CSV
        data = Micro_fam
        # Preguntar al usuario por el tipo de BGC que desea analizar
        bgc_type = valor

        # Filtrar datos en función del tipo de BGC
        bgc_data = data[data["BGC type"] == bgc_type]

        # Calcular ocurrencias de cada género en función del tipo de BGC
        occurrences = bgc_data.groupby("#Genus").size().reset_index(name='Occurrences')

        # Colores para los BGC types
        color_palette = {
            'ni-siderophore': 'red',
            'lanthipeptide-class-i': 'yellow',
            'lanthipeptide-class-ii': 'yellow',
            'lassopeptide': 'yellow',
            'nrps': 'green',
            'terpene': 'purple',
            't1pks': 'blue',
            't2pks':'blue',
            't3pks': 'blue',
            'betalactone': 'cyan'
        }

        # Seleccionar el color adecuado para el BGC
        color = color_palette.get(bgc_type, 'gray')  # usa 'gray' si el tipo de BGC no tiene color asignado

        # Crear el histograma
        plt.figure(figsize=(18, 6))
        sns.barplot(data=occurrences, x="#Genus", y="Occurrences", color=color)
        plt.xlabel("Género")
        plt.ylabel("Frecuencia de Ocurrencias")
        plt.title(f"Histograma de Ocurrencias de {bgc_type} por Género")
        plt.xticks(rotation=45)  # Rotar los nombres de los géneros si son largos
        plt.tight_layout()
        plt.show()
        
def obtener_datos_entrada():
    #Obtener la columna y el valor de búsqueda de entrada
    columna = input("¿Qué deseas buscar? (NCBI accession o BGC type): ").strip()
    valor = input(f"Introduce el valor de {columna}: ").strip()
    return columna, valor

def main():
    #Función principal que maneja la entrada
    # Cargar los datos
    df = datos()

    # Preguntar al usuario por el tipo de búsqueda
    columna, valor = obtener_datos_entrada()

    # Validar que la columna ingresada sea válida
    if columna not in ['NCBI accession', 'BGC type']:
        print(Fore.RED + "Columna inválida. Elige entre 'NCBI accession' o 'BGC type'.")
        return

    # Mostrar los resultados
    mostrar_tabla_bgc(df, columna, valor)

if __name__ == "__main__":
    main()