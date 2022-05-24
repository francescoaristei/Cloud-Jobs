# Generated by Django 4.0.4 on 2022-05-21 15:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobdescription',
            name='company',
            field=models.TextField(null=True, verbose_name='Company'),
        ),
        migrations.AddField(
            model_name='jobdescription',
            name='link',
            field=models.TextField(null=True, verbose_name='link'),
        ),
        migrations.AlterField(
            model_name='jobdescription',
            name='description',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='jobdescription',
            name='title',
            field=models.TextField(null=True, verbose_name='Title'),
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('category', models.CharField(blank=True, max_length=10, null=True)),
                ('instructions', models.CharField(blank=True, max_length=4000, null=True)),
                ('region', models.CharField(blank=True, max_length=20, null=True)),
                ('slug', models.SlugField(default='test')),
                ('image_url', models.CharField(blank=True, max_length=50, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
