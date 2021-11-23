from django.db import models
import uuid
# Create your models here.

class Tblpolicies(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, default=uuid.uuid4, editable=False, max_length=36)
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    cloudtype = models.CharField(db_column='CloudType', max_length=50, blank=True,
                                 null=True)  # Field name made lowercase.
    service = models.TextField(db_column='Service', blank=True, null=True)  # Field name made lowercase.
    severity = models.TextField(db_column='Severity', blank=True, null=True)  # Field name made lowercase.
    descriptions = models.TextField(db_column='Descriptions', blank=True, null=True)  # Field name made lowercase.
    standards = models.TextField(db_column='Standards', blank=True, null=True)  # Field name made lowercase.
    query = models.TextField(db_column='Query', blank=True, null=True)  # Field name made lowercase.
    recommendation = models.TextField(db_column='Recommendation', blank=True,
                                      null=True)  # Field name made lowercase.
    conformitystatus = models.CharField(db_column='ConformityStatus', max_length=50, blank=True,
                                        null=True)  # Field name made lowercase.
    reviewstatus = models.CharField(db_column='ReviewStatus', max_length=50, blank=True,
                                    null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, blank=True,
                              null=True)  # Field name made lowercase.
    pic = models.TextField(db_column='PIC', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.
    label = models.TextField(db_column='Label', blank=True, null=True)  # Field name made lowercase.
    reference = models.TextField(db_column='Reference', blank=True, null=True)  # Field name made lowercase.
    cronexpression = models.CharField(db_column='CroneExpression', max_length=50, blank=True,
                                       null=True)  # Field name made lowercase.
    timewindow = models.CharField(db_column='TimeWindow', max_length=50, blank=True,
                                  null=True)  # Field name made lowercase.
    mitreattacktatic = models.CharField(db_column='MitreAttackTatic', max_length=50, blank=True,
                                        null=True)  # Field name made lowercase.
    policytype = models.CharField(db_column='PolicyType', max_length=45, blank=True,
                                  null=True)  # Field name made lowercase.
    index = models.CharField(db_column='Index', max_length=50, blank=True, null=True)  # Field name made lowercase.
    config = models.CharField(db_column='Config', max_length=45, blank=True,
                              null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblpolicies'
