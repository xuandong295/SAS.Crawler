# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Tblapis(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=255)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    cloudtype = models.CharField(db_column='CloudType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    service = models.TextField(db_column='Service', blank=True, null=True)  # Field name made lowercase.
    conformitystatus = models.CharField(db_column='ConformityStatus', max_length=50, blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    pic = models.TextField(db_column='PIC', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblapis'


class Tblmapperpolicyapi(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=255)  # Field name made lowercase.
    policyid = models.ForeignKey('Tblpolicies', models.DO_NOTHING, db_column='PolicyId', blank=True, null=True)  # Field name made lowercase.
    apiid = models.ForeignKey(Tblapis, models.DO_NOTHING, db_column='ApiId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblmapperpolicyapi'


class Tblpolicies(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=255)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    cloudtype = models.CharField(db_column='CloudType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    service = models.TextField(db_column='Service', blank=True, null=True)  # Field name made lowercase.
    severity = models.TextField(db_column='Severity', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
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
    croneexpression = models.CharField(db_column='CroneExpression', max_length=50, blank=True, null=True)  # Field name made lowercase.
    timewindow = models.CharField(db_column='TimeWindow', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mitreattacktatic = models.CharField(db_column='MitreAttackTatic', max_length=50, blank=True, null=True)  # Field name made lowercase.
    policytype = models.CharField(db_column='PolicyType', max_length=45, blank=True, null=True)  # Field name made lowercase.
    index = models.CharField(db_column='Index', max_length=50, blank=True, null=True)  # Field name made lowercase.
    config = models.CharField(db_column='Config', max_length=45, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=45, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'tblpolicies'


class Tblthreatdetectionrules(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=50, blank=True, null=True)
    cloudtype = models.CharField(max_length=45, blank=True, null=True)
    severity = models.CharField(max_length=45, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    mitreattacktactic = models.CharField(max_length=45, blank=True, null=True)
    index = models.CharField(max_length=45, blank=True, null=True)
    query = models.TextField(blank=True, null=True)
    timewindow = models.CharField(max_length=45, blank=True, null=True)
    config = models.CharField(max_length=45, blank=True, null=True)
    recommendation = models.TextField(blank=True, null=True)
    cronexpression = models.CharField(max_length=50, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    pic = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblthreatdetectionrules'
