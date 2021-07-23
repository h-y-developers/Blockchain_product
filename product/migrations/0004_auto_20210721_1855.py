# Generated by Django 3.2.5 on 2021-07-21 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_user_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Images',
            field=models.TextField(default='H&Y.png', null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='address1',
            field=models.CharField(blank=True, default='', max_length=400),
        ),
        migrations.AddField(
            model_name='product',
            name='address2',
            field=models.CharField(blank=True, default='', max_length=400),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('mb', 'Mobile & Accesary'), ('fb', 'Food and Bevarages'), ('cl', 'Clothing'), ('el', 'Electronics')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='city',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='product',
            name='comapany_name',
            field=models.CharField(blank=True, default='', max_length=264),
        ),
        migrations.AddField(
            model_name='product',
            name='country',
            field=models.CharField(choices=[('us', 'America'), ('in', 'India'), ('it', 'Italy'), ('brt', 'Britain'), ('rs', 'Russia')], max_length=264, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='first_name',
            field=models.CharField(blank=True, default='', max_length=264),
        ),
        migrations.AddField(
            model_name='product',
            name='landline_no',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='last_name',
            field=models.CharField(blank=True, default='', max_length=264),
        ),
        migrations.AddField(
            model_name='product',
            name='manufacturer_name',
            field=models.CharField(blank=True, default='', max_length=264),
        ),
        migrations.AddField(
            model_name='product',
            name='mobile_no',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='postcode',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='product_name',
            field=models.CharField(blank=True, default='', max_length=264),
        ),
        migrations.AddField(
            model_name='product',
            name='product_number',
            field=models.CharField(default=1, max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=''),
        ),
        migrations.AddField(
            model_name='product',
            name='state',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='username',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product.user'),
            preserve_default=False,
        ),
    ]
