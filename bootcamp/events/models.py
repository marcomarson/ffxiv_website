from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from autoslug import AutoSlugField
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.db.models import Count

import markdown
from taggit.managers import TaggableManager


@python_2_unicode_compatible
class Events(models.Model):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title')
    tags = TaggableManager()
    content = models.TextField(max_length=4000)
    Dateevent= models.DateTimeField()
    nummaxplayers= models.IntegerField()
    create_user = models.ForeignKey(User)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    update_user = models.ForeignKey(User, null=True, blank=True,
                                    related_name="+")

    class Meta:
        verbose_name = _("Events")
        verbose_name_plural = _("Events")
        ordering = ("-create_date",)

    def __str__(self):
        return self.title

    def get_content_as_markdown(self):
        return markdown.markdown(self.content, safe_mode='escape')

    def get_summary(self):
        if len(self.content) > 255:
            return '{0}...'.format(self.content[:255])
        else:
            return self.content


@python_2_unicode_compatible
class ffxivclasses(models.Model):
    # article = models.ForeignKey(Article)
    role = models.CharField(max_length=10)
    name = models.CharField(max_length=15)


    class Meta:
        verbose_name = _("FFXIV Classes")
        verbose_name_plural = _("FFXIV Classes")
