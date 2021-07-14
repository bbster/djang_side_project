from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('users.urls')),
    path('comunity/', include('board.urls')),
    # path('comment/', include('comment.urls')),
]
