# как работает сериализатор
from django.conf import settings
settings.configure()
from datetime import datetime
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser


class Comment: # объявлен некий класс
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()

comment = Comment(email='tranchak@gmail.com', content='мое мыло') # взят экземпляр нашего класса

print(comment.email,comment.content,comment.created) # выведены в консоль наши данные

class CommentSerializer(serializers.Serializer): #класс сериализатора атрибуты которого мы будем сериализовать
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

serial=CommentSerializer(comment) # получили переменную сериализатор связанный с данными (все преобразовано в строку)

json=JSONRenderer().render(serial.data) # преобразовали в json (байт строка), т.е. прошла сериализация
print(serial.data)
print(json)

stream = io.BytesIO(json)
data = JSONParser().parse(stream)
print(data, 'строка 34') #обратная десериализация из байт строки

serializer = CommentSerializer(data=data)
print(serializer.is_valid()) # True
print(serializer.validated_data)

akz=Comment(**serializer.validated_data) #распаковали order dict
print(akz)