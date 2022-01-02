from django.db import models

class Train(models.Model):
    id = models.IntegerField("id", primary_key=True)
    name = models.CharField("name", max_length=255, blank = True, null = False)
    train_number = models.IntegerField("train_number", blank = True, null = True)
    train_type = models.CharField("train_type", max_length=255, blank = True, null = True)
    source = models.CharField("source", max_length=255, blank = True, null = True)
    destination = models.CharField("destination", max_length=255, blank = True, null = True)

    class Meta:
        db_table = "trains"


