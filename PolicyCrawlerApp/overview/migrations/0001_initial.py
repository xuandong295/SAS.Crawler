# Generated by Django 3.2.6 on 2021-09-07 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tblpolicies',
            fields=[
                ('id', models.CharField(db_column='Id', max_length=255, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True, db_column='Name', null=True)),
                ('cloudtype', models.CharField(blank=True, db_column='CloudType', max_length=50, null=True)),
                ('severity', models.TextField(blank=True, db_column='Severity', null=True)),
                ('descriptions', models.TextField(blank=True, db_column='descriptions', null=True)),
                ('standards', models.TextField(blank=True, db_column='Standards', null=True)),
                ('query', models.TextField(blank=True, db_column='Query', null=True)),
                ('recommendation', models.TextField(blank=True, db_column='Recommendation', null=True)),
                ('conformitystatus', models.CharField(blank=True, db_column='ConformityStatus', max_length=50, null=True)),
                ('reviewstatus', models.IntegerField(blank=True, db_column='ReviewStatus', null=True)),
                ('status', models.IntegerField(blank=True, db_column='Status', null=True)),
                ('pic', models.TextField(blank=True, db_column='PIC', null=True)),
                ('comment', models.TextField(blank=True, db_column='Comment', null=True)),
            ],
            options={
                'db_table': 'tblpolicies',
                'managed': False,
            },
        ),
    ]
