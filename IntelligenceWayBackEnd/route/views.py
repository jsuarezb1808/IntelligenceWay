"""
from typing import Any
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView, UpdateView
from django.views import View
from django import forms
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from .models import rutaAprendizaje, LearningPreferences, ContenidoEducacion

from django.contrib.auth import login, logout
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from .models import LearningPreferences
from .models import ContenidoEducacion
from django.contrib.auth.decorators import login_required
from .algoritmo import EstimacionEstudio
from .forms import AprendizajeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
"""