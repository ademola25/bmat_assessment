
from rest_framework.routers import DefaultRouter
from .views import  MusicalWorkViewset
from django.conf.urls import url, include
from . import views
router = DefaultRouter()
router.register('lookup', MusicalWorkViewset, basename='lookup')


urlpatterns = [
   
    url('', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
   
]

   
