from django.db import models
import datetime
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50)
    text = models.TextField()
    publish_date = models.DateTimeField(default=datetime.datetime.now)
    classified = models.BooleanField(default=False)

    @models.permalink
    def get_absolute_url(self):
        return ('post',(),{
                'slug': self.slug,
                'id': self.id,
        })

    def __str__(self):
        return self.title
