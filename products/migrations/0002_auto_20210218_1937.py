# Generated by Django 2.2 on 2021-02-18 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.Seller'),
        ),
        migrations.AddField(
            model_name='image',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='products.ImageAlbum'),
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together={('id', 'slug')},
        ),
    ]
