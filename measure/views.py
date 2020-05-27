from django.shortcuts import render, HttpResponse
import requests

# Create your views here.
def home(request):
    return render(request, "measure/home.html")

def measure(request):
    # Verifica si hay un parametro value en la petición GET
    if 'value' in request.GET:
        value = request.GET['value']
        # Verifica si el value no esta vacio
        if value:
            # Crea el json para realizar la petición POST al Web Service
            args = {'type': 'ph', 'value': value}
            response = requests.post('http://127.0.0.1:8000/measuressssss/', args)
            # Convierte la respuesta en JSON
            measure_json = response.json()

    # Realiza una petición GET al Web Services
    response = requests.get('http://127.0.0.1:8000/measuressssss/')
    # Convierte la respuesta en JSON
    measuressssss = response.json()
    # Rederiza la respuesta en el template measure
    return render(request, "measure/measure.html", {'measuressssss': measuressssss})