from django.shortcuts import render
#from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from django.core.mail import send_mail
#from django.http import HttpResponse
from django.utils import timezone

from django.template import Context, Template

from .models import Artist, MailTemplate, Sponsor, Concert, Gast, Footer
from .forms import TicketReservationForm, TicketReservation2021Form, WorkshopReservationForm, TicketReservation2022Form
# from forms.py import TicketReservation2020Form

# Create your views here.

#@login_required(login_url='/login/')
def index(request):
    #artists = Artist.objects.all()
    artists = Artist.objects.filter(group="pve").order_by("rang")
    #gaeste = Gast.objects.all()
    gaeste = Artist.objects.filter(group="gast").order_by("rang")
    youngsters = Artist.objects.filter(group="youngster").order_by("rang")
    concerts = Concert.objects.order_by("performance_date")
    sponsors = Sponsor.objects.order_by("rang")
    footer = Footer.objects.filter()[:1].get()

    return render(
        request,
        'home/base.html',
        {
            'concerts': concerts,
            'artists': artists,
            'gaeste': gaeste,
            'youngsters': youngsters,
            'sponsors': sponsors,
            'footer': footer,
        }
    )


def letmesee(request, tag):

    return redirect('/#{}'.format(tag))


def karten(request):

    footer = Footer.objects.filter()[:1].get()

    if request.method == "POST":

        # Formular mit Daten aus dem POST
        form = TicketReservation2021Form(request.POST) # TicketReservation2021Form

        if form.is_valid():
            reservation = form.save(commit=True) #False
            reservation.request_date = timezone.now()
            reservation.save()

            temp = MailTemplate.objects.get(name='karten_bestaetigung_2021') # karten_bestaetigung_2021
            t = Template(temp.text)
            c = Context({"r":reservation})

            # Benachrichtigung an den Kunden
            res = send_mail(
                temp.subject,
                t.render(c),
                "vorbestellung@liedfestival-kassel.de",
                [reservation.email]
            )

            # interne Benachrichtigung
            res = send_mail(
                "Kartenvorbestellung - {} {}".format(
                    reservation.first_name,
                    reservation.last_name
                ),
                t.render(c),
                "vorbestellung@liedfestival-kassel.de",
                # ['felix@werthschulte.info']
                #["m.kravtchin@liedfestival-kassel.de",
                #"t.schmaderer@liedfestival-kassel.de"]
                ["leo.kravtchin@gmail.com", "michael.kravtchin@gmail.com", "T.Schmaderer@web.de"]
                # "michael.kravtchin@gmail.com",
                # "T.Schmaderer@web.de"
            )

            return render(request, 'home/karten_2021.html', # auch für 2022, nur neue Klassen & Forms
                    {
                        'order_okay': True,
                        'footer': footer
                    }
                )

    else:
        form = TicketReservation2021Form() # TicketReservation2021Form()

    return render(request, 'home/karten_2021.html',
            {
                'form': form,
                'footer': footer
            }
        )


def workshop_anmeldung(request):

    footer = Footer.objects.filter()[:1].get()

    if request.method == "POST":
        form = WorkshopReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.request_date = timezone.now()
            reservation.save()

            temp = MailTemplate.objects.get(name='workshop_bestaetigung')
            t = Template(temp.text)
            c = Context({"r":reservation})

            # E-Mail an Kunden
            res = send_mail(
                temp.subject,
                t.render(c),
                "workshop@liedfestival-kassel.de",
                [reservation.email]
            )

            # interne E-Mail
            res = send_mail(
                temp.subject,
                t.render(c),
                "workshop@liedfestival-kassel.de",
                ["t.schmaderer@liedfestival-kassel.de"]
            )

            return render(request, 'home/workshop_res.html',
                    {
                        'order_okay': True,
                        'footer': footer
                    }
                )
    else:
        form = WorkshopReservationForm()

    return render(request, 'home/workshop_res.html',
            {
                'form': form,
                'footer': footer
            }
        )


# Redirect to Favicon at static file folder
def favicon(request):
    return redirect('/static/img/favicon.ico')


def google(request):
    return redirect('/static/google/googleba5118c5e56500e9.html')

def main():
    karten(request)

if __name__ == "__main__":
    main()
