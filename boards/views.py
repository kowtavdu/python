from django.shortcuts import render
from django.http import HttpResponse
import logging
logger = logging.getLogger(__name__)
# Create your views here.
def home(request):
    logger.error("Test!! Error")
    logger.debug("Test!! DEBUG")
    return HttpResponse("Hello World");