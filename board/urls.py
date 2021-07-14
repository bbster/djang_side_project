from django.urls import path, include
from .views import BoardViewset, CommentViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('boards', BoardViewset)
router.register('comments', CommentViewset)

urlpatterns =[
    path('', include(router.urls))
]
