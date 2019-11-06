from django.db import models as modeldjango
from djongo import models
from pymongo import MongoClient

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

    def get_client(self):
        self.db = MongoClient(host='mongodb://105.103.67.60:27017/test')
        client = self.db.lessie_application.radioInterpreter_theme

        return client

    def get_theme_by_id(self, str_id_theme):
        client = self.get_client()
        result = client.find_one({'id': str_id_theme})

        return result

    def get_all_themes_available(self):
        result = {}
        client = self.get_client()
        result_all_themes = client.find()
        for document in result_all_themes:
            try:
                result[document['os']].append(document['name_theme'])
            except KeyError:
                result[document['os']] = [document['name_theme']]

        return result


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


