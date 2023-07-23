import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Women


class WomenModel:
    def __int__(self, title, content):
        self.title = title
        self.content = content



#class WomenSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Women
#        fields = ('title', 'cat_id')
class WomenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()




def encode():
    model = WomenModel('Angelina Jolie', 'Content: Angelina Jolie')
    model_sr = WomenSerializer(model)
    print(model_sr.data, type(model_sr.data), sep='\n')
    json = JSONRenderer().render(model_sr.data)#передает строку JSON
    print(json)




def decode():
    stream = io.BytesIO(b'{"title": "Angelina Jolie", "content": "Angelina Jolie"}')
    data = JSONParser().parse(stream)
    serialazer = WomenSerializer(data=data)
    serialazer.is_valid()
    print(serialazer)




