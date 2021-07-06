from django.db import models
from users.models import Users


class Boards(models.Model):
    # 제목, 게시글, 유저정보
    id = models.AutoField(primary_key=True, null=False, blank=False)
    title = models.CharField(max_length=100)
    text = models.TextField()
    user = models.ForeignKey(Users, blank=True, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
