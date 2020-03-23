from django.db import models


class Relationship(models.Model):
    male_name = models.CharField(max_length=25)
    female_name = models.CharField(max_length=25)
    slug = models.SlugField(max_length=50, default='s')
    percent_in_love = models.PositiveIntegerField(blank=True, null=True)
    percent_in_married = models.PositiveIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.male_name} -- {self.female_name}'