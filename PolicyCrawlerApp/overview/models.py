from django.db import models

# Create your models here.

class Tblpolicies(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=255)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    cloudtype = models.CharField(db_column='CloudType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    severity = models.TextField(db_column='Severity', blank=True, null=True)  # Field name made lowercase.
    descriptions = models.TextField(db_column='descriptions', blank=True, null=True)  # Field name made lowercase.
    standards = models.TextField(db_column='Standards', blank=True, null=True)  # Field name made lowercase.
    query = models.TextField(db_column='Query', blank=True, null=True)  # Field name made lowercase.
    recommendation = models.TextField(db_column='Recommendation', blank=True, null=True)  # Field name made lowercase.
    conformitystatus = models.CharField(db_column='ConformityStatus', max_length=50, blank=True, null=True)  # Field name made lowercase.
    reviewstatus = models.CharField(db_column='ReviewStatus', max_length=50, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pic = models.TextField(db_column='PIC', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.
    label = models.TextField(db_column='Label', blank=True, null=True)  # Field name made lowercase.
    reference = models.TextField(db_column='Reference', blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'tblpolicies'

class Tblthreatdetectionrules(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='name',max_length=50, blank=True, null=True)
    cloudtype = models.CharField(db_column='cloudtype',max_length=45, blank=True, null=True)
    severity = models.CharField(db_column='severity',max_length=45, blank=True, null=True)
    type = models.CharField(db_column='type',max_length=50, blank=True, null=True)
    descriptions = models.TextField(db_column='descriptions',blank=True, null=True)
    mitreattacktatic = models.CharField(db_column='mitreattacktactic',max_length=45, blank=True, null=True)
    index = models.CharField(db_column='index',max_length=45, blank=True, null=True)
    query = models.TextField(db_column='query',blank=True, null=True)
    timewindow = models.CharField(db_column='timewindow',max_length=45, blank=True, null=True)
    config = models.CharField(db_column='config',max_length=45, blank=True, null=True)
    recommendation = models.TextField(db_column='recommendation',blank=True, null=True)
    cronexpression = models.CharField(db_column='cronexpression',max_length=50, blank=True, null=True)
    status = models.IntegerField(db_column='status',blank=True, null=True)
    pic = models.TextField(db_column='pic',blank=True, null=True)
    comment = models.TextField(db_column='comment',blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblthreatdetectionrules'