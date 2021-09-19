from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from clientes.models import Clientes
from clientes.serializers import ClientesSerializer
from clientes.models import DadosConcessionarias
from clientes.serializers import DadosConcessionariasSerializer
from clientes.models import RespostaComercial
from clientes.serializers import RespostaComercialSerializer
from clientes.models import RespostaTecnica
from clientes.serializers import RespostaTecnicaSerializer
from rest_framework.decorators import api_view


## Clientes API METHOD

@api_view(['GET', 'POST', 'DELETE'])
def clientes_list(request):
    # GET list of tutorials, POST a new tutorial, DELETE all tutorials
    if request.method == 'GET':
        clientes = Clientes.objects.all()

        nome = request.GET.get('Nome', None)
        if nome is not None:
            clientes = clientes.filter(nome__icontains=nome)
        clientes_serializers = ClientesSerializer(clientes, many=True)
        return JsonResponse(clientes_serializers.data, safe=False)

    elif request.method == 'POST':
        clientes_data = JSONParser().parse(request)
        clientes_serializer = ClientesSerializer(data=clientes_data)
        if clientes_serializer.is_valid():
            clientes_serializer.save()
            return JsonResponse(clientes_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(clientes_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Clientes.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

 
 
@api_view(['GET', 'PUT', 'DELETE'])
def clientes_detail(request, pk):
    try: 
        Clientes = Clientes.objects.get(pk=pk) 
    except Clientes.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 

    if request.method == 'GET':
        clientes_serializer = ClientesSerializer(Clientes)
        return JsonResponse(clientes_serializer.data)
    
    elif request.method == 'PUT':
        clientes_data = JSONParser().parse(request)
        clientes_serializer = ClientesSerializer(Clientes, data=clientes_data)
        if clientes_serializer.is_valid():
            clientes_serializer.save()
            return JsonResponse(clientes_serializer.data)
        return JsonResponse(clientes_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Clientes.delete()
        return JsonResponse({'message': 'Clientes was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

## DadosConcessionarias API METHOD

@api_view(['GET', 'POST', 'DELETE'])
def DadosConcessionarias_list(request):
    # GET list of tutorials, POST a new tutorial, DELETE all tutorials
    if request.method == 'GET':
        dadosConcessionarias = DadosConcessionarias.objects.all()

        DadosConcessionarias_serializers = DadosConcessionariasSerializer(dadosConcessionarias, many=True)
        return JsonResponse(DadosConcessionarias_serializers.data, safe=False)

    elif request.method == 'POST':
        DadosConcessionarias_data = JSONParser().parse(request)
        DadosConcessionarias_serializer = DadosConcessionariasSerializer(data=DadosConcessionarias_data)
        if DadosConcessionarias_serializer.is_valid():
            DadosConcessionarias_serializer.save()
            return JsonResponse(DadosConcessionarias_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(DadosConcessionarias_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = DadosConcessionarias.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def DadosConcessionarias_detail(request, pk):
    try: 
        dadosConcessionarias = DadosConcessionarias.objects.get(pk=pk) 
    except dadosConcessionarias.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 

    if request.method == 'GET':
        DadosConcessionarias_serializer = DadosConcessionariasSerializer(DadosConcessionarias)
        return JsonResponse(DadosConcessionarias_serializer.data)
    
    elif request.method == 'PUT':
        DadosConcessionarias_data = JSONParser().parse(request)
        DadosConcessionarias_serializer = DadosConcessionariasSerializer(DadosConcessionarias, data=DadosConcessionarias_data)
        if DadosConcessionarias_serializer.is_valid():
            DadosConcessionarias_serializer.save()
            return JsonResponse(DadosConcessionarias_serializer.data)
        return JsonResponse(DadosConcessionarias_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        DadosConcessionarias.delete()
        return JsonResponse({'message': 'DadosConcessionarias was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


## RespostaComercial API METHOD

@api_view(['GET', 'POST', 'DELETE'])
def RespostaComercial_list(request):
    # GET list of tutorials, POST a new tutorial, DELETE all tutorials
    if request.method == 'GET':
        respostaComercial = RespostaComercial.objects.all()
        RespostaComercial_serializers = RespostaComercialSerializer(respostaComercial, many=True)
        return JsonResponse(RespostaComercial_serializers.data, safe=False)

    elif request.method == 'POST':
        RespostaComercial_data = JSONParser().parse(request)
        RespostaComercial_serializer = RespostaComercialSerializer(data=RespostaComercial_data)
        if RespostaComercial_serializer.is_valid():
            RespostaComercial_serializer.save()
            return JsonResponse(RespostaComercial_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(RespostaComercial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = RespostaComercial.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

 
 
@api_view(['GET', 'PUT', 'DELETE'])
def RespostaComercial_detail(request, pk):
    try: 
        respostaComercial = RespostaComercial.objects.get(pk=pk) 
    except respostaComercial.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 

    if request.method == 'GET':
        RespostaComercial_serializer = RespostaComercialSerializer(RespostaComercial)
        return JsonResponse(RespostaComercial_serializer.data)
    
    elif request.method == 'PUT':
        RespostaComercial_data = JSONParser().parse(request)
        RespostaComercial_serializer = RespostaComercialSerializer(RespostaComercial, data=RespostaComercial_data)
        if RespostaComercial_serializer.is_valid():
            RespostaComercial_serializer.save()
            return JsonResponse(RespostaComercial_serializer.data)
        return JsonResponse(RespostaComercial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        RespostaComercial.delete()
        return JsonResponse({'message': 'RespostaComercial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


## RespostaTecnica API METHOD

@api_view(['GET', 'POST', 'DELETE'])
def RespostaTecnica_list(request):
    # GET list of tutorials, POST a new tutorial, DELETE all tutorials
    if request.method == 'GET':
        respostaTecnica = RespostaTecnica.objects.all()
        RespostaTecnica_serializers = RespostaTecnicaSerializer(respostaTecnica, many=True)
        return JsonResponse(RespostaTecnica_serializers.data, safe=False)

    elif request.method == 'POST':
        RespostaTecnica_data = JSONParser().parse(request)
        RespostaTecnica_serializer = RespostaTecnicaSerializer(data=RespostaTecnica_data)
        if RespostaTecnica_serializer.is_valid():
            RespostaTecnica_serializer.save()
            return JsonResponse(RespostaTecnica_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(RespostaTecnica_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = RespostaTecnica.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

 
 
@api_view(['GET', 'PUT', 'DELETE'])
def RespostaTecnica_detail(request, pk):
    try: 
        respostaTecnica = RespostaTecnica.objects.get(pk=pk) 
    except respostaTecnica.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 

    if request.method == 'GET':
        RespostaTecnica_serializer = RespostaTecnicaSerializer(RespostaTecnica)
        return JsonResponse(RespostaTecnica_serializer.data)
    
    elif request.method == 'PUT':
        RespostaTecnica_data = JSONParser().parse(request)
        RespostaTecnica_serializer = RespostaTecnicaSerializer(RespostaTecnica, data=RespostaTecnica_data)
        if RespostaTecnica_serializer.is_valid():
            RespostaTecnica_serializer.save()
            return JsonResponse(RespostaTecnica_serializer.data)
        return JsonResponse(RespostaTecnica_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        RespostaTecnica.delete()
        return JsonResponse({'message': 'RespostaTecnica was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)