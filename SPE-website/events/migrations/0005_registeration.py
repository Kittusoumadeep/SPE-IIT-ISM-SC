# Generated by Django 3.1.1 on 2020-10-02 13:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0004_auto_20200929_1231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registeration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user2', models.CharField(blank=True, max_length=300, null=True)),
                ('user3', models.CharField(blank=True, max_length=300, null=True)),
                ('user4', models.CharField(blank=True, max_length=300, null=True)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=200)),
                ('team_name', models.CharField(blank=True, max_length=300, null=True)),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='events.events')),
                ('first_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
