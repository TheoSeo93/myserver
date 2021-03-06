from django.db import models


class MenuSection(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.id)+" "+str(self.name)


class Item(models.Model):
    name = models.CharField(max_length=20)
    menuSection = models.ForeignKey(MenuSection, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
