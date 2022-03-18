from django.db import models

class Pokemon(models.Model):
    number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    type1 = models.CharField(max_length=16)
    type2 = models.CharField(max_length=16,null=True)
    height = models.CharField(max_length=8)
    weight = models.CharField(max_length=8)
    description = models.CharField(max_length=256)

    class Meta:
        verbose_name_plural = 'Pokemon'
        ordering = ['number',]
    
    def __str__(self):
        return self.name
