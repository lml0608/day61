from django.shortcuts import render,HttpResponse

# Create your views here.
from django import forms
from django.forms import fields

class UploadForm(forms.Form):

    user = fields.CharField()
    img = fields.FileField()

def upload(request):


    if request.method == "GET":

        return render(request,'upload.html')

    if request.method == "POST":

        # obj = UploadForm(request.POST,request.FILES)
        # if obj.is_valid():
        #
        #     user = obj.cleaned_data['user']
        #     img = obj.cleaned_data['img']


        user = request.POST.get('user')
        print(user)

        print(type(user))  #str

        file = request.FILES.get('img')
        print(type(file))  #class 'django.core.files.uploadedfile.InMemoryUploadedFile'>
        #文件名称
        print(file.name)
        #文件大小（字节）
        print(file.size)

        f = open(file.name,'wb')
        for line in file.chunks():
            f.write(line)
        f.close()

        return HttpResponse("ok")