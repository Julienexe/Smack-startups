# Generated by Django 5.1.5 on 2025-01-29 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='facebook',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='github',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='team'),
        ),
        migrations.AlterField(
            model_name='team',
            name='instagram',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='linkedin',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='twitter',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='youtube',
            field=models.URLField(blank=True, null=True),
        ),
    ]
