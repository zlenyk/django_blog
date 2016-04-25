from django.db import models

class Game(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    @models.permalink
    def get_absolute_url(self):
        return ('game',(),{
                'id': self.id,
        })

    def __str__(self):
        return self.name
