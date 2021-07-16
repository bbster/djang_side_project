from django.db import models
from account.models import Auth


class Board(models.Model):  # 게시판 상위
    type = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.type


class Post(models.Model):
    # 제목, 게시글, 유저정보
    board_type = models.ForeignKey(Board, on_delete=models.PROTECT)
    title = models.CharField(max_length=100, null=False)
    content = models.TextField()
    creator = models.ForeignKey(Auth, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True, editable=False)

    def __str__(self):
        return self.title + self.creator.username


class Comment(models.Model):
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.PROTECT)
    content = models.TextField(null=True, blank=True)

    creator = models.ForeignKey(Auth, on_delete=models.PROTECT, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True, editable=False)

    def __str__(self):
        return self.content + self.creator.username
