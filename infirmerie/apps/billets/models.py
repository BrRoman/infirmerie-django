from django.db import models
from django.contrib.auth.models import User

from apps.moines.models import Moine
from apps.toubibs.models import Toubib


class Billet(models.Model):
    moine = models.ForeignKey(
        Moine,
        related_name='billets',
        on_delete=models.CASCADE
    )
    toubib = models.ForeignKey(
        Toubib,
        related_name='billets',
        on_delete=models.CASCADE
    )
    datetime = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)