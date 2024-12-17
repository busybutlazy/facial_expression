from django.shortcuts import render
from .forms import ImgUploadForm
from .models import predict_image
from PIL import Image
import base64
from io import BytesIO

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
            return render(request, 'face_detect/upload.html', {
                    'form': form,
                    'prediction': prediction,
                    'img_str': img_str
                    })    
    else:
        form = ImgUploadForm()
    
    return render(request,"face_detect/upload.html",{'form':form})
        
