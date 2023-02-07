# Generated by Django 4.0.1 on 2022-05-25 19:25

import ckeditor.fields
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('locality', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('zipcode', models.IntegerField()),
                ('state', models.CharField(choices=[('Barisal', 'Barisal'), ('Chittagong', 'Chittagong'), ('Dhaka', 'Dhaka'), ('Khulna', 'Khulna'), ('Rajshahi', 'Rajshahi'), ('Sylhet', 'Sylhet')], max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('selling_price', models.FloatField()),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('brand', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('T', 'Tractor'), ('E', 'Engine'), ('GT', 'Gadening Tools'), ('FT', 'Farming Tools')], max_length=2)),
                ('product_image', models.ImageField(upload_to='productimg')),
                ('stock_available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderPlaced',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('ordered_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Accepted', 'Accepted'), ('Packed', 'Packed'), ('On The Way', 'On The Way'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel')], default='Pending', max_length=50)),
                ('Start_date', models.DateField(blank=True, default=datetime.datetime(2022, 5, 26, 1, 25, 7, 343036), null=True)),
                ('End_date', models.DateField(blank=True, default=datetime.datetime(2022, 5, 26, 1, 25, 7, 344034), null=True)),
                ('Days', models.IntegerField(blank=True, default=1, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('Start_date', models.CharField(blank=True, default=datetime.datetime(2022, 5, 26, 1, 25, 7, 343036), max_length=255, null=True)),
                ('End_date', models.CharField(blank=True, default=datetime.datetime(2022, 5, 26, 1, 25, 7, 343036), max_length=255, null=True)),
                ('Days', models.PositiveIntegerField(blank=True, default=1, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]