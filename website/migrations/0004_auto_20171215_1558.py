# Generated by Django 2.1.dev20171109164034 on 2017-12-15 15:58

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_hackathons_talks_workshops'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=120)),
                ('phoneNo', models.CharField(max_length=20)),
                ('department', models.CharField(max_length=120)),
                ('fb', models.CharField(max_length=255)),
                ('linkedin', models.CharField(max_length=255)),
            ],
            managers=[
                ('persons', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='hackathons',
            managers=[
                ('events_hackathons', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='person',
            managers=[
                ('persons', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='talks',
            managers=[
                ('events_talks', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='workshops',
            managers=[
                ('events_workshops', django.db.models.manager.Manager()),
            ],
        ),
    ]