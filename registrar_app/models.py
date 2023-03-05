from django.db import models


def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)


class Application(models.Model):
    DOC_TYPES = (
        ('NOC', 'NOC-Application'),
        ('SM', 'Seminar-Application'),
    )

    application_type = models.CharField(max_length=3, choices=DOC_TYPES)
    upload_file = models.FileField(
        upload_to=upload_to, blank=False, null=False)
    remarks = models.TextField(blank=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)
