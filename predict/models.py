from django.db import models
from django.urls import reverse

class Relationship(models.Model):
    male_name = models.CharField(max_length=25)
    female_name = models.CharField(max_length=25)
    slug = models.SlugField(max_length=50, default='s')
    header = models.CharField(max_length=25, null=True)
    percent_in_love = models.PositiveIntegerField(blank=True, null=True)
    percent_in_married = models.PositiveIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.male_name} -- {self.female_name}'

    def get_absolute_url(self):
        return reverse('predict:predict', args=[self.slug])



class MaleName(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.name}'


class FemaleName(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.name}'
