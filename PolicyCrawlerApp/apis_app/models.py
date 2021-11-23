from django.db import models
import uuid
# Create your models here.

class Tblapis(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True, default=uuid.uuid4, editable=False)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    cloudtype = models.CharField(db_column='CloudType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    service = models.TextField(db_column='Service', blank=True, null=True)  # Field name made lowercase.
    conformitystatus = models.CharField(db_column='ConformityStatus', max_length=50, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    pic = models.TextField(db_column='PIC', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblapis'
