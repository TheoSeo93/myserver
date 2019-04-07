from django.db import models


class MenuSection(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.id)+" "+str(self.name)


class Item(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name