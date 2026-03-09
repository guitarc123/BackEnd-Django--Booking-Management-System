from django.shortcuts import render, redirect
from .forms import BookingForm


def home(request):
    return render(request, 'home.html')


def create_booking(request):

    if request.method == "POST":
        form = BookingForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = BookingForm()

    return render(request, 'booking_form.html', {'form': form})