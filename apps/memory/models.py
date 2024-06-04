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
    is_liked = models.BooleanField(default=False)

    class Meta:
        db_table = 'apps_memory'
