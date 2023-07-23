from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Women
from .serializers import WomenSerializer


#class WomenAPIView(generics.ListAPIView):
#    queryset = Women.objects.all()#забирает все записи с модели
#    serializer_class = WomenSerializer

class WomenAPIView(APIView):#простая реализация API запроса GET
#    def get(self, request):
#        """обработка запроса"""
#        return Response({'title': 'Джоли, Анджелина'})

#    def post(self, request):#POST
#        return Response({'title': 'Джоли, Анджелина'})


    def get(self, request):
        lst = Women.objects.all().values()#qweryset+values()
        return Response({'posts': list(lst)})


    def post(self, request):
        """добавить на сервер поля"""
        post_new = Women.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )
        return Response({'post': model_to_dict(post_new)})

