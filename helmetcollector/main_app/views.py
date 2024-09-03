from django.shortcuts import render , redirect , get_object_or_404 , reverse
from .models import Helmet  
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from main_app.models import Helmet , Brand
from .forms import BrandForm
from django.contrib.auth.views import LoginView


class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

def helmet_index(request):
    helmets = Helmet.objects.all() 
    return render(request, 'helmets/index.html', {'helmets': helmets})


def helmet_detail(request, helmet_id):
    helmet = get_object_or_404(Helmet, id=helmet_id)
    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            new_brand = form.save(commit=False)
            new_brand.helmet = helmet
            new_brand.save()
            return redirect('helmet-detail', helmet_id=helmet_id)
    else:
        form = BrandForm()

    return render(request, 'helmets/detail.html', {
        'helmet': helmet,
        'brand_form': form
    })



def add_brand(request, helmet_id):
    helmet = get_object_or_404(Helmet, id=helmet_id)
    
    if request.method == 'POST':
        form = BrandForm(request.POST)
        
        if form.is_valid():
            brand_name = form.cleaned_data['brand']
            
            # Check if the brand already exists for this helmet
            if Brand.objects.filter(helmet=helmet, brand=brand_name).exists():
                # Redirect with a message or handle as needed
                return redirect('helmet-detail', helmet_id=helmet_id)
            
            # Save the new brand if it's not a duplicate
            new_brand = form.save(commit=False)
            new_brand.helmet = helmet
            new_brand.save()
            
            return redirect('helmet-detail', helmet_id=helmet_id)
        else:
            print('Form errors:', form.errors)
    
    return redirect('helmet-detail', helmet_id=helmet_id)


class BrandCreate(CreateView):
    model = Brand
    fields = ['brand']
    template_name = 'brands/brand_form.html'

    def form_valid(self, form):
        form.instance.helmet_id = self.kwargs['helmet_id']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('helmet-detail', kwargs={'helmet_id': self.object.helmet.id})

class BrandUpdate(UpdateView):
    model = Brand
    fields = ['brand']
    template_name = 'brands/brand_form.html'

    def get_success_url(self):
        return reverse('helmet-detail', kwargs={'helmet_id': self.object.helmet.id})

class BrandDelete(DeleteView):
    model = Brand
    template_name = 'brands/brand_confirm_delete.html'

    def get_success_url(self):
        return reverse('helmet-detail', kwargs={'helmet_id': self.object.helmet.id})



    

class HelmetCreate(CreateView):
    model = Helmet
    fields = '__all__'
    success_url = '/helmets/'

class HelmetUpdate(UpdateView):
    model = Helmet
    fields = ['driver', 'year', 'description']

class HelmetDelete(DeleteView):
    model = Helmet
    success_url = '/helmets/'