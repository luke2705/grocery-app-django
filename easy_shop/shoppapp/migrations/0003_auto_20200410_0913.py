# Generated by Django 3.0.5 on 2020-04-10 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shoppapp', '0002_delete_meal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('recipe', models.TextField(max_length=3000)),
                ('image', models.ImageField(default=None, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered_date', models.DateTimeField(default='timezone.now()')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('friends', models.ManyToManyField(to='shoppapp.User')),
            ],
        ),
        migrations.CreateModel(
            name='OrderIngredients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoppapp.Ingredient')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoppapp.Order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='creator',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='shoppapp.User'),
        ),
        migrations.AddField(
            model_name='order',
            name='ingredients',
            field=models.ManyToManyField(through='shoppapp.OrderIngredients', to='shoppapp.Ingredient'),
        ),
        migrations.CreateModel(
            name='MealIngredients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoppapp.Ingredient')),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoppapp.Meal')),
            ],
        ),
        migrations.AddField(
            model_name='meal',
            name='creator',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='shoppapp.User'),
        ),
        migrations.AddField(
            model_name='meal',
            name='ingredients',
            field=models.ManyToManyField(through='shoppapp.MealIngredients', to='shoppapp.Ingredient'),
        ),
    ]