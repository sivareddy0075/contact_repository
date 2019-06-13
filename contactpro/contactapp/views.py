from django.shortcuts import render

from .models import ContactData
from .forms import ContaForm
def contactview(request):
    if request.method == "POST":

        Cform = ContaForm(request.POST)
        if Cform.is_valid():
            first_name = request.POST.get('first_name', '')
            last_name = request.POST.get('last_name', '')
            salary = request.POST.get('salary', '')
            location = request.POST.get('location', '')
            mobile = request.POST.get('mobile', '')
            data = ContactData(
                first_name=first_name,
                last_name=last_name,
                salary=salary,
                location=location,
                mobile=mobile,
            )
            data.save()
            Cform = ContaForm()
            return render(request,'contact.html',{'Cform':Cform})
        else:
            Cform = ContaForm()
            return render(request,'contact.html',{'Cform':Cform})
    else:
        Cform = ContaForm()
        return render(request, 'contact.html', {'Cform':Cform})

