from .models import Gps
from .serializers import GpsSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET', 'POST'])
def gps_list(request, format=None):
    if (request.method == 'GET'):
        gpses = Gps.objects.all()
        serializer = GpsSerializer(gpses, many=True)
        return (Response(serializer.data))

    elif (request.method == 'POST'):
        serializer = GpsSerializer(data = request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return (Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST))
'''
POST data example
request_data = {
    (pk : Auto Increment,),
    name : CharField,
    latitude : FloatField,
    longitude : FloatField,
    (upload_date : (default : Now)),
}
'''

@api_view(['GET', 'PUT', 'DELETE'])
def gps_detail(request, pk, format=None):
    try:
        gps = Gps.objects.get(pk=pk)
    except Gps.DoesNotExist:
        return (Response(status=status.HTTP_404_NOT_FOUND))
    
    if request.method == 'GET':
        serializer = GpsSerializer(gps)
        return (Response(serializer.data))

    if request.method == 'PUT':
        serializer = GpsSerializer(gps, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return (Response(serializer.data))
        return (Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST))

    if request.method == 'DELETE':
        gps.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)