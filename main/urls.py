
from django.urls import path
from . import views
app_name = "main"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create_brand, name="create"),
    path("edit/<int:brand_id>", views.edit_brand, name="edit"),
    path("finalize/<int:brand_id>", views.finalise_brand, name="finalize"),
    path("contact/", views.contact_us, name="contact")
]