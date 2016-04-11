from django.db import models
from redactor.fields import RedactorField
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=100)
    text = models.TextField()
    publish_date = models.DateTimeField(blank=True,null=True)
    classified = models.BooleanField(default=False)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Page(models.Model):
    title = models.CharField(max_length=100)
    text = RedactorField(verbose_name=u'Text',default='')
