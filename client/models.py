from django.db import models

# Create your models here.
from PustakaIntake.models import TimeStampModel


class Client(TimeStampModel):
    client_app = models.CharField(max_length=120)
    client_id = models.UUIDField()
    client_secret = models.UUIDField()

    def __str__(self):
        return self.client_app
