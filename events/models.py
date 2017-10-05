from django.db import models

# Create your models here.
class Event(models.Model):
    title=models.CharField(max_length=200)
    maxplayers = models.IntegerField(default=4)
    content = models.TextField(max_length=2000)
    time_start= models.DateTimeField(auto_now=False)
    time_finish= models.DateTimeField(auto_now=False)

    def __unicode__(self):
        return self.title
    class Meta:
        ordering=["-time_start"]
