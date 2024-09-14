from django.urls import path
from .views import submit_review

app_name = 'products'  # Define namespace for this app

urlpatterns = [
    path('submit-review/', submit_review, name='submit_review'),
    # Other URL patterns specific to the 'products' app
]