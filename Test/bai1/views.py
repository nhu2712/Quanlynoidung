from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .forms import FormLogin

from .forms import FormLogin, FormPublisher
from .models import Book,BookContributor,Contributor,Publisher
def home (request):
    return render(request,'home.html')
def sanpham(request):
    book=   Book.objects.all()
    print(book)
    return render(request,'sanpham.html',{'book':book})
def chungtoi (request):
    bien=request.GET.get('search')
    return render(request,'chungtoi.html',{'bien':bien})
# Create your views here.
def bookdetail(request,book_id):
    book=get_object_or_404(Book,pk=book_id)
    return render(request,'bookdetail.html',{'book':book})
def login(request):
    form=FormLogin()
    if request.method=='POST':
        print(request.POST)
    return render(request,'login.html',{'form':form})
def publishernew(request):
    form=FormPublisher()
    if request.method=='POST':
        form=FormPublisher(request.POST)
        form.save()
    return render(request,'create_publisher.html',{'form':form})
def publisheredit(request,publisher_id):
    publisher=get_object_or_404(Publisher,pk=publisher_id)
    form=FormPublisher(instance=publisher)
    if request.method=='POST':
        form=FormPublisher(request.POST,instance=publisher)
        if form.is_valid():
            form.save()
    return render(request,'edit_publisher.html',{'form':form})