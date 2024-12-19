from django.shortcuts import render
from .forms import OrderForm

def form_example(request):
    initial = {"email": "user@example.com"}
    if request.method == "POST":
        form = OrderForm(request.POST, initial=initial)
    else:
        form = OrderForm(initial=initial)

    return render(request, "form-example.html", {"method": request.method, "form": form})