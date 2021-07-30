from django.db import models
from django.contrib.auth.models import User
from organizations.models import Organization
from django.contrib.postgres.fields import JSONField


def jsonfield_default_value():
    pass


class Collection(models.Model):
    name = models.CharField(max_length=255)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/collections/%s/" % self.id


class APIRequest(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    request_header = models.JSONField(default=dict, blank=True, null=True)
    request_body = models.JSONField(default=dict, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return str(self.request_body)

    def __str__(self):
        return str(self.request_body)
