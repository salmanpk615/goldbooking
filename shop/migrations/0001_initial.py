# Generated by Django 4.2 on 2023-05-19 07:18

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone', models.CharField(max_length=15)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=45)),
                ('address', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Company',
            },
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('gross_weight', models.CharField(max_length=5)),
                ('net_weight', models.CharField(max_length=5)),
                ('labour_wastage', models.CharField(max_length=5)),
                ('purity', models.CharField(max_length=5)),
                ('fine', models.CharField(max_length=5)),
                ('amount', models.CharField(max_length=10)),
                ('qr_code', models.ImageField(blank=True, upload_to='qr_codes')),
            ],
            options={
                'verbose_name': 'Item',
            },
        ),
        migrations.CreateModel(
            name='Types',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Gold', 'Gold'), ('Silver', 'Silver'), ('Diamond', 'Diamond')], max_length=7)),
            ],
            options={
                'verbose_name': 'Type',
            },
        ),
        migrations.CreateModel(
            name='Vendors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('address', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.company')),
            ],
            options={
                'verbose_name': 'Vendor',
            },
        ),
        migrations.CreateModel(
            name='UsersRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=45)),
                ('account', models.CharField(max_length=45)),
                ('billing', models.CharField(max_length=10)),
                ('sale', models.CharField(choices=[('Gold', 'Gold'), ('Silver', 'Silver'), ('Diamond', 'Diamond')], max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'UsersRole',
                'verbose_name_plural': 'UserRole',
            },
        ),
        migrations.CreateModel(
            name='StockOut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.items')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.vendors')),
            ],
            options={
                'verbose_name': 'StockOut',
                'verbose_name_plural': 'StockOut',
            },
        ),
        migrations.CreateModel(
            name='StockIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.items')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.vendors')),
            ],
            options={
                'verbose_name': 'StockIn',
                'verbose_name_plural': 'StockIn',
            },
        ),
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.items')),
                ('stockin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.stockin')),
                ('stockout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.stockout')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.vendors')),
            ],
            options={
                'verbose_name': 'Report',
            },
        ),
        migrations.AddField(
            model_name='items',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.types'),
        ),
        migrations.AddField(
            model_name='items',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.vendors'),
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(max_length=10)),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.items')),
            ],
            options={
                'verbose_name': 'Booking',
                'verbose_name_plural': 'Booking',
            },
        ),
    ]
