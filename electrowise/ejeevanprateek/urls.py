from django.urls import path, include
from ejeevanprateek import views

urlpatterns = [
    path("", views.index, name="Home"),
    path("about", views.about, name="About Us"),
    path("contact", views.contact, name="Contact Us"),
    path("services", views.services, name="Services"),
    path("patient_data", views.patient_data, name="Patient's Data"),
    path("customer_signin", views.customer_signin, name="Customer Sigh In"),
    path("customer_login", views.customer_login, name="Customer Log In"),
    path("sign_in", views.handlesignin, name="Handle Sigh In"),
    path("log_in", views.handlelogin, name="Handle Log In"),
    path("log_out", views.handlelogout, name="Handle Log Out"),
]