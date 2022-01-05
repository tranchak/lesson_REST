from django.contrib import admin
from django.urls import include, path

from api import views

from api.views import get_prezent

from api.views import prezent_no_model
# from rest_framework import routers


# router=routers.SimpleRouter()
# router.register(r"re_prezent",get_prezent,basename="re_prezent") #функцию мы прокинуть в роутер не можем

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('prezent/', get_prezent, name='prezent'),
    path('prezent_no_mod/', prezent_no_model, name='prezent_no_model'),

]
# urlpatterns+=router.urls