from django.db import models
from .choices import *

# Create your models here.
class Artist(models.Model):
    rang = models.PositiveIntegerField(default=0, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    instrument = models.CharField(max_length=50, default='', blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to='img/artists/', blank=True, null=True)
    photo_credit = models.CharField(max_length=100, default='', blank=True, null=True)
    group = models.CharField(max_length=100, default='pve', blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Gast(models.Model):
    name = models.CharField(max_length=50, default='')
    bio = models.TextField()
    picture = models.ImageField(upload_to='img/artists/')
    photo_credit = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name


class TicketReservation(models.Model):
    anrede = models.IntegerField(choices=ANREDE_CHOICES, default=1)
    titel = models.CharField(max_length=15, default='', blank=True)
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    strasse = models.CharField(max_length=50, default='')
    hausnummer = models.CharField(max_length=4, default='')
    plz = models.CharField(max_length=5, default='')
    ort = models.CharField(max_length=50, default='')
    email = models.EmailField()
    tel = models.CharField(max_length=20, default='')
    tickets_schwanengesang = models.PositiveIntegerField(default=2)
    tickets_schwanengesang_erm = models.PositiveIntegerField(default=0)
    tickets_winterreise = models.PositiveIntegerField(default=2)
    tickets_winterreise_erm = models.PositiveIntegerField(default=0)
    tickets_quartettimkonzert = models.PositiveIntegerField(default=2)
    tickets_quartettimkonzert_erm = models.PositiveIntegerField(default=0)
    tickets_summe = models.FloatField(null=True, blank=True, default=0.0)
    nachricht = models.TextField(default='', blank=True)
    request_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{:%d.%m.%Y %H:%M} - {} {}'.format(
            self.request_date,
            self.first_name,
            self.last_name
        )


class TicketReservation2019(models.Model):
    anrede = models.IntegerField(choices=ANREDE_CHOICES, default=1)
    titel = models.CharField(max_length=15, default='', blank=True)
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    strasse = models.CharField(max_length=50, default='')
    hausnummer = models.CharField(max_length=4, default='')
    plz = models.CharField(max_length=5, default='')
    ort = models.CharField(max_length=50, default='')
    email = models.EmailField()
    tel = models.CharField(max_length=20, default='', blank=True)

    tickets_gesamtpaket = models.PositiveIntegerField(default=0)
    tickets_eroeffnung = models.PositiveIntegerField(default=2)
    tickets_eroeffnung_erm = models.PositiveIntegerField(default=0)
    tickets_romanzen = models.PositiveIntegerField(default=2)
    tickets_romanzen_erm = models.PositiveIntegerField(default=0)
    tickets_jungeslied = models.PositiveIntegerField(default=2)
    tickets_jungeslied_erm = models.PositiveIntegerField(default=0)
    tickets_melodies = models.PositiveIntegerField(default=2)
    tickets_melodies_erm = models.PositiveIntegerField(default=0)
    tickets_abschluss = models.PositiveIntegerField(default=2)
    tickets_abschluss_erm = models.PositiveIntegerField(default=0)
    tickets_summe = models.FloatField(null=True, blank=True, default=0.0)

    nachricht = models.TextField(default='', blank=True)
    request_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{:%d.%m.%Y %H:%M} - {} {}'.format(
            self.request_date,
            self.first_name,
            self.last_name
        )


class TicketReservation2020(models.Model):
    anrede = models.IntegerField(choices=ANREDE_CHOICES, default=1)
    titel = models.CharField(max_length=15, default='', blank=True)
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    strasse = models.CharField(max_length=50, default='')
    hausnummer = models.CharField(max_length=4, default='')
    plz = models.CharField(max_length=5, default='')
    ort = models.CharField(max_length=50, default='')
    email = models.EmailField()
    tel = models.CharField(max_length=20, default='', blank=True)

    # Gesamtpaket
    tickets_gesamtpaket = models.PositiveIntegerField(default=0)

    # Eröffnungskonzert Samstag, 9. Mai 2020, 20 Uhr
    tickets_eroeffnung = models.PositiveIntegerField(default=0)
    tickets_eroeffnung_erm = models.PositiveIntegerField(default=0)

    # Junges Lied Sonntag, 10. Mai 2020, 20 Uhr
    tickets_jungeslied = models.PositiveIntegerField(default=0)
    tickets_jungeslied_erm = models.PositiveIntegerField(default=0)

    # Liederabend Schwarz Mittwoch, 13. Mai 2020, 20 Uhr
    tickets_liederabend = models.PositiveIntegerField(default=0)
    tickets_liederabend_erm = models.PositiveIntegerField(default=0)

    # Winterreise Donnerstag, 14. Mai 2020, 20 Uhr
    tickets_winterreise = models.PositiveIntegerField(default=0)
    tickets_winterreise_erm = models.PositiveIntegerField(default=0)

    # Die Schöne Müllerin Freitag, 15. Mai 2020, 20 Uhr
    tickets_muellerin = models.PositiveIntegerField(default=0)
    tickets_muellerin_erm = models.PositiveIntegerField(default=0)

    # Abschluss Sonntag, 17. Mai 2020, 20 Uhr
    tickets_abschluss = models.PositiveIntegerField(default=0)
    tickets_abschluss_erm = models.PositiveIntegerField(default=0)

    tickets_summe = models.FloatField(null=True, blank=True, default=0.0)

    nachricht = models.TextField(default='', blank=True)
    request_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{:%d.%m.%Y %H:%M} - {} {}'.format(
            self.request_date,
            self.first_name,
            self.last_name
        )

class TicketReservation2021(models.Model):
    anrede = models.IntegerField(choices=ANREDE_CHOICES, default=1)
    titel = models.CharField(max_length=15, default='', blank=True)
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    strasse = models.CharField(max_length=50, default='')
    hausnummer = models.CharField(max_length=4, default='')
    plz = models.CharField(max_length=5, default='')
    ort = models.CharField(max_length=50, default='')
    email = models.EmailField()
    tel = models.CharField(max_length=20, default='', blank=True)

    # Gesamtpaket
    tickets_gesamtpaket = models.PositiveIntegerField(default=0)

    # Eröffnungskonzert Mein Herz und deine Stimme Samstag, 1. Mai 2021, 20 Uhr
    tickets_eroeffnung = models.PositiveIntegerField(default=0)
    tickets_eroeffnung_erm = models.PositiveIntegerField(default=0)

    # Die Winterreise Sonntag, 02. Mai 2021, 20 Uhr
    tickets_winterreise = models.PositiveIntegerField(default=0)
    tickets_winterreise_erm = models.PositiveIntegerField(default=0)

    # Könnt ich dich in Liedern preisen Donnerstag, 06. Mai 2021, 20 Uhr
    tickets_liederabend = models.PositiveIntegerField(default=0)
    tickets_liederabend_erm = models.PositiveIntegerField(default=0)

    # Junges Lied Freitag, 07. Mai 2021, 20 Uhr
    tickets_jungeslied = models.PositiveIntegerField(default=0)
    tickets_jungeslied_erm = models.PositiveIntegerField(default=0)

    # Die Schöne Müllerin Samstag, 8. Mai 2021, 20 Uhr
    tickets_muellerin = models.PositiveIntegerField(default=0)
    tickets_muellerin_erm = models.PositiveIntegerField(default=0)

    # Flammenauge, dunkles Haar Sonntag, 9. Mai 2021, 20 Uhr
    tickets_abschluss = models.PositiveIntegerField(default=0)
    tickets_abschluss_erm = models.PositiveIntegerField(default=0)

    tickets_summe = models.FloatField(null=True, blank=True, default=0.0)

    nachricht = models.TextField(default='', blank=True)
    request_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{:%d.%m.%Y %H:%M} - {} {}'.format(
            self.request_date,
            self.first_name,
            self.last_name
        )


class TicketReservation2022(models.Model): # 2022
    anrede = models.IntegerField(choices=ANREDE_CHOICES, default=1)
    titel = models.CharField(max_length=10, default='', blank=True)
    first_name = models.CharField(max_length=20, default='')
    last_name = models.CharField(max_length=30, default='')
    strasse = models.CharField(max_length=40, default='')
    hausnummer = models.PositiveIntegerField(max_length=4, default='')
    plz = models.PositiveIntegerField(max_length=5, default='')
    ort = models.CharField(max_length=30, default='')
    email = models.EmailField(max_length=30, default='')
    tel = models.PositiveIntegerField(max_length=20, default='', blank=True)

    # Gesamtpaket
    tickets_gesamtpaket = models.PositiveIntegerField(default=0)

    # Eröffnungskonzert KRÄMERSPIEGEL, 1. Mai 2022, 20 Uhr
    tickets_eroeffnung = models.PositiveIntegerField(default=0)
    tickets_eroeffnung_erm = models.PositiveIntegerField(default=0)

    # CARL UND VERONIKA, 04. Mai 2022, 20 Uhr
    tickets_winterreise = models.PositiveIntegerField(default=0)
    tickets_winterreise_erm = models.PositiveIntegerField(default=0)

    # ERNSTE GESÄNGE, 05. Mai 2022, 20 Uhr
    tickets_liederabend = models.PositiveIntegerField(default=0)
    tickets_liederabend_erm = models.PositiveIntegerField(default=0)

    # STIMME DES ABENDS, 6. Mai 2022, 20 Uhr
    tickets_muellerin = models.PositiveIntegerField(default=0)
    tickets_muellerin_erm = models.PositiveIntegerField(default=0)

    # Junges Lied Freitag, 07. Mai 2022, 11 Uhr, NO ENTRY FEE
    tickets_jungeslied = models.PositiveIntegerField(default=0)
    tickets_jungeslied_erm = models.PositiveIntegerField(default=0)

    # AUS JIDDISCHER VOLKSPOESIE, 8. Mai 2021, 20 Uhr
    tickets_abschluss = models.PositiveIntegerField(default=0)
    tickets_abschluss_erm = models.PositiveIntegerField(default=0)

    tickets_summe = models.FloatField(null=True, blank=True, default=0.0)

    nachricht = models.TextField(default='', blank=True)
    request_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{:%d.%m.%Y %H:%M} - {} {}'.format(
            self.request_date,
            self.first_name,
            self.last_name
        )


class WorkshopReservation(models.Model):
    anrede = models.IntegerField(choices=ANREDE_CHOICES, default=1)
    titel = models.CharField(max_length=15, default='', blank=True)
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    strasse = models.CharField(max_length=50, default='')
    hausnummer = models.CharField(max_length=4, default='')
    plz = models.CharField(max_length=5, default='')
    ort = models.CharField(max_length=50, default='')
    email = models.EmailField()
    tel = models.CharField(max_length=20, default='')
    alter = models.PositiveIntegerField(default=None)
    stimmfach = models.IntegerField(choices=STIMMFACH_CHOICES, default=1)
    ermaessigt = models.BooleanField(default=None)

    def __str__(self):
        return '{:%d.%m.%Y %H:%M} - {} {}'.format(
            self.request_date,
            self.first_name,
            self.last_name
        )


class MailTemplate(models.Model):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=200, default='')
    text = models.TextField()

    def __str__(self):
        return '{} (\'{}\')'.format(self.name, self.subject)


class Sponsor(models.Model):
    rang = models.IntegerField(default=0)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Concert(models.Model):
    performance_date = models.DateTimeField()
    location = models.CharField(max_length=50, default='')
    title = models.CharField(max_length=50, default='')
    subtitle = models.CharField(max_length=50, default='')
    text = models.TextField()
    ticket_prices = models.CharField(max_length=20, default='')

    def __str__(self):
        return '{} - {}'.format(self.performance_date, self.title)


class Footer(models.Model):
    impressum = models.TextField()
    contact = models.EmailField()
    disclaimer = models.TextField()
