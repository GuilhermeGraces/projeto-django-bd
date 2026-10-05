from django.db import models


class Person(models.Model):
    first_name = models.CharField(verbose_name="Nome", max_length=30)
    last_name = models.CharField(verbose_name="Sobrenome", max_length=30)

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"
        ordering = ["first_name", "last_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"