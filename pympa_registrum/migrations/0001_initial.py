# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comunicazione',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('ricezione_data', models.DateTimeField(verbose_name='Data e ora di ricezione', help_text='Seleziona ora e data di ricezione della comunicazione')),
                ('mittente_cognome', models.CharField(blank=True, verbose_name='Cognome', null=True, max_length=200)),
                ('mittente_nome', models.CharField(blank=True, verbose_name='Nome', null=True, max_length=200)),
                ('motivazione', models.TextField(blank=True, null=True)),
                ('recapito', models.CharField(blank=True, max_length=300, null=True, help_text='Recapito del mittente')),
                ('note', models.TextField(blank=True, null=True)),
                ('evasa', models.BooleanField(default=False)),
                ('destinatari', models.ManyToManyField(blank=True, related_name='destinatari', to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name_plural': 'Comunicazioni',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MezzoComunicazione',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nome', models.CharField(max_length=30)),
                ('desc', models.TextField(blank=True, verbose_name='Descrizione', null=True)),
            ],
            options={
                'verbose_name_plural': 'Mezzi di Comunicazione',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='comunicazione',
            name='mezzo',
            field=models.ForeignKey(to='pympa_registrum.MezzoComunicazione', help_text="Seleziona il mezzo con cui e' stata ricevuta la comunicazione", verbose_name='Ricevuta con'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comunicazione',
            name='ricevente',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, related_name='ricevente', null=True),
            preserve_default=True,
        ),
    ]
