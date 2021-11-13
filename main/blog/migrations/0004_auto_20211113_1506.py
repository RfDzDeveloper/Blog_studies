# Generated by Django 3.1.5 on 2021-11-13 14:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_comment_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailToken',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('token', models.CharField(db_column='Token', max_length=100, unique=True)),
                ('email', models.CharField(db_column='Email', max_length=100)),
                ('create_date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='number_of_ratings',
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(db_column='User', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='UserRatings',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ratings', models.PositiveSmallIntegerField(db_column='Ratings', null=True)),
                ('post', models.ForeignKey(db_column='Post', on_delete=django.db.models.deletion.CASCADE, to='blog.post')),
                ('user', models.ForeignKey(db_column='User', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
