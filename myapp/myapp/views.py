from django.http import HttpResponse


def hola(request):
    numeros = [int(n) for n in request.GET['numeros'].split(',')]
    numeros_ord = sorted(numeros)

    print(request.GET)
    return HttpResponse(str(numeros_ord))