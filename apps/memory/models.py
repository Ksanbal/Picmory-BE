from django.db import models


# 추억
class Memory(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        'user.User',
        on_delete=models.SET_NULL,
        null=True,
    )
    date = models.DateField()
    brand = models.CharField(
        max_length=100,
        null=True,
        default=None,
    )


# 추억 좋아요
class MemoryLike(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
    )
    memory = models.ForeignKey(
        'Memory',
        on_delete=models.CASCADE,
    )
