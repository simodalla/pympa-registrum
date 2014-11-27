# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# User = get_user_model()


@python_2_unicode_compatible
class MezzoComunicazione(models.Model):
    nome = models.CharField(max_length=30)
    desc = models.TextField('Descrizione', blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Mezzi di Comunicazione"


@python_2_unicode_compatible
class Comunicazione(models.Model):
    ricezione_data = models.DateTimeField(
        verbose_name='Data e ora di ricezione',
        help_text='Seleziona ora e data di ricezione della comunicazione')
    mezzo = models.ForeignKey(MezzoComunicazione, verbose_name='Ricevuta con',
                              help_text="Seleziona il mezzo con cui e' stata"
                                        " ricevuta la comunicazione")
    destinatari = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, null=True, related_name="destinatari",
        limit_choices_to={'groups__name__exact': 'registrum_destinatari'})
    mittente_cognome = models.CharField(blank=True, null=True, max_length=200,
                                        verbose_name='Cognome')
    mittente_nome = models.CharField(blank=True, null=True, max_length=200,
                                     verbose_name='Nome')
    motivazione = models.TextField(blank=True, null=True)
    recapito = models.CharField(blank=True, null=True, max_length=300,
                                help_text='Recapito del mittente')
    note = models.TextField(blank=True, null=True)
    ricevente = models.ForeignKey(
        settings.AUTH_USER_MODEL, blank=True, null=True, related_name="ricevente",
        limit_choices_to={'groups__name__exact': 'registrum_riceventi'})
    evasa = models.BooleanField(default=False)

    def __str__(self):
        return 'comunicazione n. {}'.format(self.id)

    class Meta:
        verbose_name_plural = "Comunicazioni"
