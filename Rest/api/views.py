from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Prezent
from .serializers import UserSerializer, GroupSerializer, PrezentSerializer, SerializerPrezent


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

@api_view(['GET','POST'])
def get_prezent(request):
    all_present=Prezent.objects.all()
    # print(all_present)
    # print(all_present[0])
    serialise=PrezentSerializer(all_present, many=True)
    # print(serialise.data)
    if request.method=='POST':
        print(request.POST)
        if not all_present.filter(name=request.POST.get('name')):

            serialize = PrezentSerializer(data=request.data)
            serialize.is_valid()
        # print(serialize.validated_data)
            serialize.save()
        else:
            return Response({'message': 'Такой пользователь есть'})
    return Response({'message':serialise.data})

@api_view(['GET','POST'])
def prezent_no_model(request):
    all_prez=Prezent.objects.all()
    serializer=SerializerPrezent(all_prez, many=True)
    p=Prezent(name='Johan', price=100, description='Hello')

    # p.save()
    # print(p.pk, p.name, p.price, p.description, p.created)
    if request.method=='POST':
        serializer=SerializerPrezent(data=request.data)
        # print(serializer)
        if serializer.is_valid():
            # serializer.create(validated_data=serializer.validated_data) # сохраняет в базу данных
            serializer.save() # можно использовать или тот или тот метод
            return Response({'message':serializer.data})
    else:
        return Response({'message':serializer.data})

