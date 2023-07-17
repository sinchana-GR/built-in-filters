from django.shortcuts import render

# Create your views here.
import datetime

def built_in_filters(request):
    date=datetime.datetime.now()
    d={'data':'tHis Is buIlt_in filTerS','c':1,'date':date}
    return render(request,'built_in_filters.html',d)


 