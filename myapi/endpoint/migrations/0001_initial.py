# Generated by Django 2.2.19 on 2021-03-11 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=30)),
                ('zip', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Generic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(max_length=200)),
                ('rating', models.DecimalField(decimal_places=0, max_digits=2)),
                ('avatar', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('generic_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='endpoint.Generic')),
            ],
            bases=('endpoint.generic',),
        ),
        migrations.CreateModel(
            name='PropertyTypes',
            fields=[
                ('generic_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='endpoint.Generic')),
            ],
            bases=('endpoint.generic',),
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('generic_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='endpoint.Generic')),
            ],
            bases=('endpoint.generic',),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('generic_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='endpoint.Generic')),
            ],
            bases=('endpoint.generic',),
        ),
        migrations.CreateModel(
            name='Properties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.URLField()),
                ('price', models.PositiveIntegerField()),
                ('bath', models.DecimalField(decimal_places=0, max_digits=2)),
                ('beds', models.DecimalField(decimal_places=0, max_digits=2)),
                ('sqft', models.PositiveSmallIntegerField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='endpoint.Cities')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='endpoint.Categories')),
                ('propertietypes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='endpoint.PropertyTypes')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='endpoint.Transaction')),
            ],
        ),
        migrations.AddField(
            model_name='cities',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='endpoint.States'),
        ),
    ]
