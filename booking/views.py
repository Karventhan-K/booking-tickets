from django.shortcuts import render
from .models import ticket_booking
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages


# Create your views here.
def index(request):
    if request.method == "POST":
        firstname = request.POST['first_name']
        lastname = request.POST['lastname']
        fathername = request.POST['fathername']
        gender = request.POST.getlist('gender_m_or_f')[0]
        email = request.POST['email']
        phonenumber = request.POST['mobilenumber']
        starting_point = request.POST.getlist('starting_point')[0]
        end_point = request.POST.getlist('end_point')[0]

        ticket_booking_count = ticket_booking.objects.filter(start_station=starting_point,
                                                             end_station=end_point)
        print(ticket_booking_count.count())
        if ticket_booking_count.count() > 2:
            return render(request, 'index.html', {'alert_flag': True})
        else:

            tb = ticket_booking(first_name=firstname,
                                last_name=lastname,
                                father_name=fathername,
                                Gender=gender,
                                mobile_number=phonenumber,
                                email=email,
                                start_station=starting_point,
                                end_station=end_point)
            tb.save()
            return render(request, 'index.html', {'saved_flag': True})
    return render(request, "index.html")
