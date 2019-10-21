from django.db import models as modeldjango
from djongo import models

# Create your models here.


OS_IN_MODELS = [
    ('NN', 'Android 7.0'),
    ('OO', 'Android 8.0'),
    ('PP', 'Android 9.0'),
    ('QQ', 'Android 10.0')
]


class Theme(models.Model):
    """
    This model is going to register all problems with a OS associated.
    It will be use to match key strings with problems.
    """
    name_theme = models.CharField(max_length=60)
    os = models.CharField(max_length=2, choices=OS_IN_MODELS)

    def __str__(self):
        return self.name_theme

    class Meta:
        ordering = ['name_theme']


class Key(models.Model):
    """
    This model is to register all the strings in a list associated with a theme.
    Ideally, we should have just one Keys(Model) for each Theme(Model), but we can have more.
    For that reason, this model is many-to-one relationship.
    """
    name_key = models.CharField(max_length=60)

    def __str__(self):
        return self.name_key


class RadioKey(models.Model):
    keys = models.ManyToManyField(Key)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)


