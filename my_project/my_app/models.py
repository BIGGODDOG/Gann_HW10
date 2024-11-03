from django.db import models

class Restaurant(models.Model):
    name = models.CharField("Название", max_length=100)
    specialization = models.CharField("Специализация", max_length=100)
    address = models.CharField("Адрес", max_length=200)
    website = models.URLField("Веб-сайт", blank=True)
    phone = models.CharField("Контактный телефон", max_length=20, blank=True)

    def __str__(self):
        return f"{self.name} ({self.specialization})"
