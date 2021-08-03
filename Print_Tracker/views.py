from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import PrintTracker


class PrintListView(ListView):
    model = PrintTracker
    template_name = "base.html"
    context_object_name = "print_jobs"
    ordering = ["-date_of_print"]
