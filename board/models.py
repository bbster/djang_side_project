from django.db import models
from users.models import Users


class Boards(models.Model):
    # 제목, 게시글, 유저정보
    id = models.AutoField(primary_key=True, null=False, blank=False)
    title = models.CharField(max_length=100)
    content = models.TextField()
    creator = models.ForeignKey(Users, blank=True, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True, editable=False)

    def __str(self):
        return self.title


class Comment(models.Model):
    board = models.ForeignKey(Boards, null=True, blank=True, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)

    creator = models.ForeignKey(Users, on_delete=models.CASCADE, null=True, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True, editable=False)

    def __str__(self):
        return self.content + self.creator.username