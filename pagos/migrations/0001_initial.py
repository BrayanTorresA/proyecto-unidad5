# Generated by Django 4.1.4 on 2022-12-20 19:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('servicios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymnentUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.FloatField(default=0.0)),
                ('fecha_pago', models.DateField(auto_now_add=True)),
                ('fecha_expiracion', models.DateField()),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='servicio', to='servicios.service')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cliente', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'pagos',
            },
        ),
    ]
