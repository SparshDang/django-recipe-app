from django.db import models


# Create your models here.


class Recipe(models.Model):

    class DishType(models.TextChoices):
        Beverages = "Beverages"
        Starter = 'Starter'
        MainCourse = 'Main course'
        Snacks = 'Snacks'
        Dessert = 'Dessert'
        Others = 'Others'

    name = models.CharField(max_length=50)
    preprationDuration = models.DurationField()
    servings = models.IntegerField()
    dishType = models.CharField(
        choices=DishType.choices, default='b', max_length=20
    )
    ingredients = models.JSONField(null=True)
    steps = models.JSONField()

    slug = models.SlugField()

    def __str__(self):
        return self.name.title()
