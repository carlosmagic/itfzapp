from django.views.generic.base import TemplateView
from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import WellnessEntry
from .forms import NewWellnessEntry
from django.contrib.auth.models import User


def add_wellness(request):
    form = NewWellnessEntry()
    if request.method == 'POST':
        form = NewWellnessEntry(request.POST)
        if form.is_valid():
            user = request.POST.get('user','')
            wellness_date = request.POST.get('wellness_date','')
            wellnes_energy = request.POST.get('wellnes_energy','')
            wellnes_sleep = request.POST.get('wellnes_sleep','')
            wellnes_motivation = request.POST.get('wellnes_motivation','')
            wellnes_stress = request.POST.get('wellnes_stress','')
            wellnes_hungry = request.POST.get('wellnes_hungry','')
            wellnes_steps = request.POST.get('wellnes_steps','')
            wellnes_bath = request.POST.get('wellnes_bath','')
            wellnes_fasting = request.POST.get('wellnes_fasting','')
            WellnessData = WellnessEntry(user = user,
                            wellness_date = wellness_date,
                            wellnes_energy = wellnes_energy,
                            wellnes_sleep = wellnes_sleep,
                            wellnes_motivation = wellnes_motivation,
                            wellnes_stress = wellnes_stress,
                            wellnes_hungry = wellnes_hungry,
                            wellnes_steps = wellnes_steps,
                            wellnes_bath = wellnes_bath,
                            wellnes_fasting = wellnes_fasting
                            )
            WellnessData.save()
        return render(request, 'wellness/gracias.html')
    
    else: 
        form = NewWellnessEntry()
        context = {
            'form':form,
        } 

    return render(request, 'wellness/wellness_form.html', {'form':form}, context)

""" class WellnesEntryView(TemplateView): 
    template_name = "wellness_form.html"
    form_class = NewWellnessEntry

    def get_context_data(self, **kwargs):
        context = super(NewWellnessEntry, self).get_context_data(**kwargs)
        return context

    def get(self, request):
        return render(request, self.template_name, context)

    def form_valid(self, form):
        form.save()
        return super(WellnesEntryView,self).form.valid(form)"""