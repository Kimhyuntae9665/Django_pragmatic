# Generated by Django 4.2.2 on 2023-07-15 05:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projectapp', '0002_alter_project_created_at_alter_project_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subsciption', to='projectapp.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscription', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'project')},
            },
        ),
    ]
