from django.db import models

# Create your models here.

class Wdress(models.Model):
    price = models.IntegerField("Цена")
    name = models.CharField("Название одежды", max_length=100)
    description = models.CharField("Описание одежды", max_length=212)
    image = models.CharField("Ссылка на фото", max_length=500)


    def __str__(self):
        return self.name
