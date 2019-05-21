from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    email_addr=models.CharField(max_length=30)
    password=models.CharField(max_length=20)
    class Meta:
        db_table="user"


class Chouse(models.Model):
    code=models.CharField(max_length=20)
    userid = models.ForeignKey(User, verbose_name=u'userid', db_constraint=False, on_delete=models.DO_NOTHING,
                                blank=True)
    class Meta:
        db_table="choose"
