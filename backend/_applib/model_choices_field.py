from django.db import models

class GenderChoice(models.TextChoices):
    MALE="MALE",
    FEMALE="FEMALE",
    OTHER="OTHER"


class status(models.TextChoices):
    PENDING= "PENDING",
    APPROVED= "APPROVED",
    DELETED= "DELETED",