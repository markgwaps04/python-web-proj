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

class budgetExpenses(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=False,null=False,max_length=250)
    date_created = models.DateTimeField(null=False, blank=False, default=datetime.now)
    pass

class Items(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=False,null=False,max_length=250)
    budget_expenses = models.ForeignKey(budgetExpenses, blank=False, null=False,on_delete=models.CASCADE)
    date_created = models.DateTimeField(null=False, blank=False, default=datetime.now)
    weekly = models.FloatField(null=False, blank=False)
    bi_weekly = models.FloatField(null=False, blank=False)
    monthly = models.FloatField(null=False, blank=False)
    yearly = models.FloatField(null=False, blank=False)
    is_sub_query = models.BooleanField(default=False)
    pass

class itemsSub(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=False,null=False,max_length=250)
    item =  models.ForeignKey(Items, blank=False, null=False,on_delete=models.CASCADE)
    date_created = models.DateTimeField(null=False, blank=False, default=datetime.now)
    pass

