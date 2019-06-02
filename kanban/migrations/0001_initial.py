# Generated by Django 2.1.3 on 2019-06-01 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Issues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issueID', models.IntegerField()),
                ('desc', models.TextField()),
                ('status', models.CharField(choices=[('Backlog', 'Backlog'), ('To-do', 'To-do'), ('Doing', 'Doing'), ('Completed', 'Completed'), ('QA', 'QA'), ('Closed', 'Closed')], max_length=10)),
                ('priority', models.CharField(choices=[('H', 'High'), ('M', 'Medium'), ('L', 'Low')], max_length=10)),
            ],
        ),
    ]
