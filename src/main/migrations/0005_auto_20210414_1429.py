# Generated by Django 3.1.7 on 2021-04-14 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_logger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logger',
            name='ip',
            field=models.GenericIPAddressField(),
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='Comment')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='main.post')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
