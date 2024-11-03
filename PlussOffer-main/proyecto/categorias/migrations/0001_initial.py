from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('idCategoria', models.AutoField(primary_key=True, serialize=False, verbose_name='ID CATEGORIA')),
                ('nombreCategoria', models.CharField(max_length=100, verbose_name='Nombre de la categoria')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['created'],
            },
        ),
    ]
