from django.db import models

from board.models import Boards
from users.models import Users


class Comment(models.Model):
    board = models.ForeignKey(Boards, null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, blank=True, null=True, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
