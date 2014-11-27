# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib import admin
from django import forms
from .models import Comunicazione, MezzoComunicazione


class ComunicazioneAdminForm(forms.ModelForm):
    class Meta:
        model = Comunicazione

    def clean_mittente_cognome(self):
        return self.cleaned_data['mittente_cognome'].title()

    def clean_mittente_nome(self):
        return self.cleaned_data['mittente_nome'].title()


class ComunicazioneAdmin(admin.ModelAdmin):
    actions = ['evadi']
    date_hierarchy = 'ricezione_data'
    fields = ['ricezione_data', 'destinatari', 'mittente_cognome',
              'mittente_nome', 'mezzo', 'motivazione', 'recapito', 'note',
              'evasa']
    filter_horizontal = ['destinatari']
    form = ComunicazioneAdminForm
    list_display = ['id', 'ricezione_data', 'ld_elenco_destinatari', 'evasa',
                    'mittente_cognome', 'mittente_nome',
                    'recapito', 'motivazione', 'ld_ricevente']
    list_filter = ['evasa', 'ricezione_data', 'destinatari', 'ricevente',
                   'mezzo']
    list_per_page = 30
    list_select_related = True
    ordering = ['-id', 'mittente_cognome', 'mittente_nome']
    radio_fields = {'mezzo': admin.VERTICAL}
    search_fields = ['destinatari__last_name', 'destinatari__first_name',
                     'mittente_cognome', 'mittente_nome']

    def evadi(self, request, queryset):
        rows_updated = queryset.update(evasa=True)
        if rows_updated == 1:
            message_bit = "Comunicazione evasa correttamente"
        else:
            message_bit = "Comunicazioni selezionate evase correttamente"
        self.message_user(request, message_bit)
    evadi.short_description = "Evadi la comunicazione"

    def ld_elenco_destinatari(self, obj):
        destinatari = ['<li>{user.last_name} {user.first_name}</li>'.format(
            user=d) for d in obj.destinatari.all()]
        return "<ul>{}</ul>".format(''.join(destinatari))
    ld_elenco_destinatari.short_description = 'Destinatari'
    ld_elenco_destinatari.allow_tags = True

    def ld_ricevente(self, obj):
        return "{user.last_name} {user.first_name}".format(user=obj.ricevente)
    ld_ricevente.short_description = 'Ricevente'
    ld_ricevente.admin_order_field = 'ricevente'

    def save_model(self, request, obj, form, change):
        obj.ricevente = request.user
        obj.save()


admin.site.register(MezzoComunicazione)
admin.site.register(Comunicazione, ComunicazioneAdmin)