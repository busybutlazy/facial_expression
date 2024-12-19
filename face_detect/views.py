from django.shortcuts import render
from .forms import ImgUploadForm
from .models import predict_image
from PIL import Image
import base64
from io import BytesIO
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.urls import reverse

def to_result(request,came_from):
    print("start to result.")
    print(request.FILES)

    if request.method == "POST" and 'img' in request.FILES:
        form = ImgUploadForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.cleaned_data['img']
            image=Image.open(image)
            prediction = predict_image(image)
            buffered = BytesIO()
            image.save(buffered,format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
            return render(request, "face_detect/result.html", {
                    'form': form,
                    'prediction': prediction,
                    'img_str': img_str
                    })
    else:
        print("can't find img.")
        form = ImgUploadForm()
    return render(request,came_from,{'form':form})


def image_upload_view(request):
    if request.method == "POST" and 'img' in request.FILES:
        form = ImgUploadForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.cleaned_data['img']
            image=Image.open(image)
            prediction = predict_image(image)
            buffered = BytesIO()
            image.save(buffered,format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
            request.session['prediction'] = prediction
            request.session['img_str'] = img_str
            return redirect(f'/detect/result/?form={form}')

    else:
        form = ImgUploadForm()
    return render(request,"face_detect/detect_by_upload.html",{'form':form})

@csrf_exempt
def screenshot_upload_view(request):

    if request.method == "POST" and 'img' in request.FILES:
        form = ImgUploadForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.cleaned_data['img']
            image=Image.open(image)
            prediction = predict_image(image)
            buffered = BytesIO()
            image.save(buffered,format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
            request.session['prediction'] = prediction
            request.session['img_str'] = img_str
            return redirect(f'/detect/result/?form={form}')
    else:
        print("can't find img.")
        form = ImgUploadForm()
    return render(request,"face_detect/detect_by_video.html",{'form':form})

def result(request):    
    return render(request, 'face_detect/result.html', {
        'form': request.GET.get('form'),
        'prediction': request.session.get('prediction', 'No prediction available'),
        'img_str': request.session.get('img_str', None)
    })    

def detect_index(request):
    pass