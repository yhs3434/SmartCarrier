from .models import Gps
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import GpsSerializer

@csrf_exempt
def gps_list(request):
    if (request.method == 'GET'):
        gpses = Gps.objects.all()
        serializer = GpsSerializer(gpses, many=True)
        return (JsonResponse(serializer.data, safe=False))

    elif (request.method == 'POST'):
        data = JSONParser().parse(request)
        serializer = GpsSerializer(data = data)
        if (serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return (JsonResponse(serializer.errors, status=400))
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

def gps_detail(request, pk):
    try:
        gps = Gps.objects.get(pk=pk)
    except Gps.DoesNotExist:
        return (HttpResponse(status=404))
    
    if request.method == 'GET':
        serializer = GpsSerializer(gps)
        return (JsonResponse(serializer.data))

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = GpsSerializer(gps, data=data)
        if serializer.is_valid():
            serializer.save()
            return (JsonResponse(serializer.data))
        return (JsonResponse(serializer.errors, status=400))

    if request.method == 'DELETE':
        gps.delete()
        return HttpResponse(status=204)