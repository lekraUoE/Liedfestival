from django import forms
from .models import TicketReservation, TicketReservation2019, TicketReservation2020, TicketReservation2021, WorkshopReservation, TicketReservation2022
from .choices import *

class TicketReservationForm(forms.ModelForm):

    class Meta:
        model = TicketReservation

        titel = forms.CharField(required=False)

        fields = ('anrede',
            'titel',
            'first_name',
            'last_name',
            'strasse',
            'hausnummer',
            'plz',
            'ort',
            'email',
            'tel',
            'tickets_schwanengesang',
            'tickets_schwanengesang_erm',
            'tickets_winterreise',
            'tickets_winterreise_erm',
            'tickets_quartettimkonzert',
            'tickets_quartettimkonzert_erm',
            'nachricht')
        labels = {
            'anrede': 'Anrede',
            'titel': 'Titel (falls vorhanden)',
            'first_name': 'Vorname',
            'last_name': 'Nachname',
            'strasse': 'Straße',
            'hausnummer': 'Hausnummer',
            'plz': 'PLZ',
            'ort': 'Ort',
            'email': 'E-Mail',
            'tel': 'Telefon',
        }


class TicketReservation2019Form(forms.ModelForm):

    class Meta:
        model = TicketReservation2019

        titel = forms.CharField(required=False)

        fields = ('anrede',
            'titel',
            'first_name',
            'last_name',
            'strasse',
            'hausnummer',
            'plz',
            'ort',
            'email',
            'tel',
            'tickets_gesamtpaket',
            'tickets_eroeffnung',
            'tickets_eroeffnung_erm',
            'tickets_romanzen',
            'tickets_romanzen_erm',
            'tickets_jungeslied',
            'tickets_jungeslied_erm',
            'tickets_melodies',
            'tickets_melodies_erm',
            'tickets_abschluss',
            'tickets_abschluss_erm',
            'nachricht')
        labels = {
            'anrede': 'Anrede',
            'titel': 'Titel (falls vorhanden)',
            'first_name': 'Vorname',
            'last_name': 'Nachname',
            'strasse': 'Straße',
            'hausnummer': 'Hausnummer',
            'plz': 'PLZ',
            'ort': 'Ort',
            'email': 'E-Mail',
            'tel': 'Telefon (optional)',
        }


class TicketReservation2020Form(forms.ModelForm):

    class Meta:
        model = TicketReservation2020

        titel = forms.CharField(required=False)

        fields = ('anrede',
            'titel',
            'first_name',
            'last_name',
            'strasse',
            'hausnummer',
            'plz',
            'ort',
            'email',
            'tel',
            'tickets_gesamtpaket',
            'tickets_eroeffnung',
            'tickets_eroeffnung_erm',
            'tickets_jungeslied',
            'tickets_jungeslied_erm',
            'tickets_liederabend',
            'tickets_liederabend_erm',
            'tickets_winterreise',
            'tickets_winterreise_erm',
            'tickets_muellerin',
            'tickets_muellerin_erm',
            'tickets_abschluss',
            'tickets_abschluss_erm',
            'nachricht')
        labels = {
            'anrede': 'Anrede',
            'titel': 'Titel (falls vorhanden)',
            'first_name': 'Vorname',
            'last_name': 'Nachname',
            'strasse': 'Straße',
            'hausnummer': 'Hausnummer',
            'plz': 'PLZ',
            'ort': 'Ort',
            'email': 'E-Mail',
            'tel': 'Telefon (optional)',
        }


class TicketReservation2021Form(forms.ModelForm):

    class Meta:
        model = TicketReservation2021

        titel = forms.CharField(required=False)

        fields = ('anrede',
            'titel',
            'first_name',
            'last_name',
            'strasse',
            'hausnummer',
            'plz',
            'ort',
            'email',
            'tel',
            'tickets_gesamtpaket', # 70
            'tickets_eroeffnung', # Krämerspiegel
            'tickets_eroeffnung_erm',
            'tickets_winterreise', # Carl und Veronica
            'tickets_winterreise_erm',
            'tickets_liederabend', # Ernste Gesänge
            'tickets_liederabend_erm',
            'tickets_muellerin', # Stimme des Abends
            'tickets_muellerin_erm',
            'tickets_jungeslied', # same thing, freier Eintritt
            'tickets_abschluss', # Aus jiddischer Volkspeosie
            'tickets_abschluss_erm',
            'nachricht')
        labels = {
            'anrede': 'Anrede',
            'titel': 'Titel (falls vorhanden)',
            'first_name': 'Vorname',
            'last_name': 'Nachname',
            'strasse': 'Straße',
            'hausnummer': 'Hausnummer',
            'plz': 'PLZ',
            'ort': 'Ort',
            'email': 'E-Mail',
            'tel': 'Telefon (optional)',
        }


class TicketReservation2022Form(forms.ModelForm): # now for 2022

    class Meta:
        model = TicketReservation2022

        titel = forms.CharField(required=False)

        fields = ('anrede',
            'titel',
            'first_name',
            'last_name',
            'strasse',
            'hausnummer',
            'plz',
            'ort',
            'email',
            'tel',
            'tickets_gesamtpaket', # Alle Konzerte für 70€
            'tickets_eroeffnung', # Krämerspiegel
            'tickets_eroeffnung_erm',
            'tickets_winterreise', # Carl und Veronica
            'tickets_winterreise_erm',
            'tickets_liederabend', # Ernste Gesänge
            'tickets_liederabend_erm',
            'tickets_muellerin', # Stimme des Abends
            'tickets_muellerin_erm',
            'tickets_jungeslied', # same thing, freier Eintritt
            'tickets_abschluss', # Aus jiddischer Volkspeosie
            'tickets_abschluss_erm',
            'nachricht')
        labels = {
            'anrede': 'Anrede',
            'titel': 'Titel (falls vorhanden)',
            'first_name': 'Vorname',
            'last_name': 'Nachname',
            'strasse': 'Straße',
            'hausnummer': 'Hausnummer',
            'plz': 'PLZ',
            'ort': 'Ort',
            'email': 'E-Mail',
            'tel': 'Telefon (optional)',
        }


class WorkshopReservationForm(forms.ModelForm):

    class Meta:
        model = WorkshopReservation

        fields = ('anrede',
            'titel',
            'first_name',
            'last_name',
            'strasse',
            'hausnummer',
            'plz',
            'ort',
            'email',
            'tel',
            'alter',
            'stimmfach',
            'ermaessigt')

        labels = {
            'anrede': 'Anrede',
            'titel': 'Titel (falls vorhanden)',
            'first_name': 'Vorname',
            'last_name': 'Nachname',
            'strasse': 'Straße',
            'hausnummer': 'Hausnummer',
            'plz': 'PLZ',
            'ort': 'Ort',
            'email': 'E-Mail',
            'tel': 'Telefon',
            'alter': 'Alter',
            'stimmfach': 'Stimmfach',
            'ermaessigt': 'Schüler, Student'
        }
