from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from api import views

from api.views import get_prezent

from api.views import prezent_no_model

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('prezent/', get_prezent, name='prezent'),
    path('prezent_no_mod/', prezent_no_model, name='prezent_no_model'),

]