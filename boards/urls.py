from django.urls import path, include
from .views import BoardViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('boards', BoardViewset)

urlpatterns =[
    path('', include(router.urls))
]
