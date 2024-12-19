from django.urls import path

from . import views

urlpatterns = [
    path("detect/",views.detect_index,name="index"),
    path("detect/upload_img/", views.image_upload_view, name="image_upload_view"),
    path("detect/screen_shot/",views.screenshot_upload_view,name="screenshot_upload_view"),
    path("detect/result/",views.result,name="result")
]
