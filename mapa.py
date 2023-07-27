import requests
import urllib
import webbrowser

api_url = "https://www.mapquestapi.com/directions/v2/route?"
key = "pmcCEtp7SwbG8Y2YGdyqUFDnb9pvtQ4F"

# titulo
print("Info de viajes en carro\n")

print("Para acabar la búsqueda dale 'l' minuscula.")

while True:
    origen = input("Ingresa el origen: ")
    if origen == "l":
        print("Gracias por consultarnos.")
        break
    destino = input("Ingrese el destino: ")
    if destino == "l":
        print("Gracias por consultarnos.")
        break

    url = api_url + urllib.parse.urlencode({"key": key, "from": origen, "to": destino})
    json_data = requests.get(url).json()
    status_code = json_data["info"]["statuscode"]
    distancia = json_data["route"]["distance"] * 1.61
    if status_code == 0:
        trip_duration = json_data["route"]["formattedTime"]
        print("______________________________________________________")
        print(f"Información del viaje desde {origen.capitalize()} hasta {destino.capitalize()}.")
        print(f"La duración del viaje: {trip_duration}.")
        print(f"La distancia: {distancia:.2f} km.")
        # GASTO DE LA GASOLINA
        fuel_efficiency = 12  
        fuel_consumption = distancia / fuel_efficiency
        print(f"El combustible aproximado usado: {fuel_consumption:.2f} litros.")
        print("_____________________________________________________")
        print("Indicaciones del viaje")

        for each in json_data["route"]["legs"][0]["maneuvers"]:
            distance_remaining = distancia - each["distance"] * 1.61            
            print(each["narrative"] + " (" + str("{:.2f}".format(distance_remaining)) + " Km faltantes)")

        # Open Google Maps with the entire route
        google_maps_url = f"https://www.google.com/maps/dir/{origen}/{destino}"
        webbrowser.open(google_maps_url)


        

