from django.db import models
from datetime import date, datetime
from django.contrib.auth.models import User, AnonymousUser
from app.misc import file_should_excel, path_unique_name


# Create your models here.
class AdminFileLog(models.Model):
    id = models.AutoField(primary_key=True)
    date_created = models.DateTimeField(null=False, blank=False, default=datetime.now)
    file = models.FileField(
        verbose_name="Excel file",
        upload_to=path_unique_name,
        blank=False, null=False,
        validators=[file_should_excel],
    )
    user_update = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=False, null=False)


    pass
