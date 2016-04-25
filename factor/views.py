from django.shortcuts import render
from django.http import HttpResponseRedirect
from factor.forms import FactorForm
def factor(request):
    if request.method == 'POST':
        form = FactorForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/factor/')
    else:
        form = FactorForm()
    return render(request,'factor/index.html',{'form': FactorForm()})
