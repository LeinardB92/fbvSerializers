from django.shortcuts import render
# importamos el modelo sobre el que vamos a trabajar
from fbvApp.models import Student
# Serializador para serializar y deserializar los datos de nuestro modelo
from fbvApp.serializers import StudentSerializer
# 'Response', devuelve contenido que se puede representar en varios tipos de contenido, según la solicitud del cliente también podrías usar HttpResponse, pero 'Response'. El uso de la clase Response simplemente proporciona una interfaz más agradable para devolver respuestas de API web, que se pueden representar en múltiples formatos..
from rest_framework.response import Response
# Ayuda a describir el estado de los códigos HTTP, para mejorar la comprensión del código. 
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET','POST'])
def student_list(request):

    if request.method =='GET':
        # Obtenemos un queryset de la base de datos 
        students = Student.objects.all()
        # Serializamos el queryset 
        serializer = StudentSerializer(students,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Deserializamos los datos mandados por el usuario a través de 'request', serializer es ahora un objeto python que podemos utilizar.
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            # Guardamos en la base de datos
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def student_detail(request,pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
