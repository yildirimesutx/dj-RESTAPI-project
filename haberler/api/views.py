from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from haberler.models import Makale
from .serializers import MakaleSerializer

@api_view(["GET", 'POST'])
def makale_list_create_api_view(request):
    
    if request.method == 'GET':
        makaleler = Makale.objects.filter(aktif=True) # nesnelerden oluşan bir query set
        serializer= MakaleSerializer(makaleler, many=True) # query set, many=True eklenmez ise hata veriyor
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer= MakaleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        Response(status=status.HTTP_400_BAD_REQUEST)         




