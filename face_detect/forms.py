from django import forms

class ImgUploadForm(forms.Form):
    img=forms.ImageField()