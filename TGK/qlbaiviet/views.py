from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from .forms import BaiVietForm
from .models import BaiViet, ChuyenMuc


def xembaiviet(request,idbaiviet):
    baiviet=get_object_or_404(BaiViet,pk=idbaiviet)
    print(baiviet)
    return render(request,'xembaiviet.html',{'baiviet':baiviet})
def dsbaiviet(request,idchuyenmuc):
    dsbaiviet=get_object_or_404(ChuyenMuc,pk=idchuyenmuc)
    baiviet=dsbaiviet.baiviet_set.all()
    print (baiviet)
    return render(request,'dsbaiviet.html',{'baiviet':baiviet})
def suabaiviet(request,pk=None):
    global form
    if pk is not None:
        baiviet=get_object_or_404(BaiViet,pk=pk)
    else:
        baiviet=None
        if request.method == 'POST':
            form = BaiVietForm(request.POST,instance=baiviet)
            if form.is_valid():
                updated_baiviet=form.save()
                if baiviet is None:
                    messages.success(request, 'Tạo mới bài viết "{}" thành công.'.format(updated_baiviet))
                else:
                    messages.success(request, 'Chỉnh sửa bài viết "{}" thành công.'.format(updated_baiviet))
                return redirect ('xembaiviet',updated_baiviet.pk)
        else:
            form = BaiVietForm(instance=baiviet)
    return render(
            request,
            "suabaiviet.html",
            {
                "method": request.method,
                "form": form,
                "model_type": "BaiViet",
                "instance": baiviet,
            },
        )
    # Create your views here.
