from django.urls import path, include
from .views import PostViewset, CommentViewset, BoardViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('boards', BoardViewset)
router.register('posts', PostViewset)
router.register('comments', CommentViewset)

urlpatterns =[
    path('', include(router.urls))
]
