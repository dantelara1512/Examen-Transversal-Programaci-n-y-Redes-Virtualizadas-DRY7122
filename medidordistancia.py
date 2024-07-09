from geopy.distance import geodesic
from datetime import timedelta

def calcular_distancia_y_duracion(ciudad_origen, ciudad_destino, medio_transporte):
    # Coordenadas de algunas ciudades de ejemplo en Chile y Argentina
    ciudades = {
        'santiago': (-33.4489, -70.6693),
        'buenos aires': (-34.6037, -58.3816)
    }
    
    if ciudad_origen.lower() not in ciudades:
        print(f"No se encontraron coordenadas para la ciudad de origen '{ciudad_origen}'")
        return
    
    if ciudad_destino.lower() not in ciudades:
        print(f"No se encontraron coordenadas para la ciudad de destino '{ciudad_destino}'")
        return
    
    # Obtener coordenadas de las ciudades
    origen = ciudades[ciudad_origen.lower()]
    destino = ciudades[ciudad_destino.lower()]
    
    # Calcular la distancia en kilómetros
    distancia_km = geodesic(origen, destino).kilometers
    
    # Convertir la distancia a millas
    distancia_millas = geodesic(origen, destino).miles
    
    # Calcular la duración del viaje (suponiendo velocidad promedio en diferentes medios)
    if medio_transporte.lower() == 'auto':
        velocidad_promedio_kmh = 100  # km/h
    elif medio_transporte.lower() == 'avion':
        velocidad_promedio_kmh = 800  # km/h
    elif medio_transporte.lower() == 'tren':
        velocidad_promedio_kmh = 120  # km/h
    else:
        print(f"Tipo de medio de transporte '{medio_transporte}' no reconocido")
        return
    
    duracion_horas = distancia_km / velocidad_promedio_kmh
    duracion = timedelta(hours=duracion_horas)
    
    # Mostrar los resultados
    print(f"Distancia entre {ciudad_origen.title()} y {ciudad_destino.title()}:")
    print(f"- En kilómetros: {distancia_km:.2f} km")
    print(f"- En millas: {distancia_millas:.2f} mi")
    print(f"Duración del viaje en {medio_transporte.lower()} aproximadamente:")
    print(f"- {duracion}")

# Ejemplo de uso del script
while True:
    ciudad_origen = input("Ingrese la ciudad de origen (o 's' para salir): ").strip().lower()
    if ciudad_origen == 's':
        break
    
    ciudad_destino = input("Ingrese la ciudad de destino: ").strip().lower()
    medio_transporte = input("Ingrese el tipo de medio de transporte (auto, avion, tren): ").strip().lower()
    
    calcular_distancia_y_duracion(ciudad_origen, ciudad_destino, medio_transporte)