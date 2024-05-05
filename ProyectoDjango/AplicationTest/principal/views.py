from django.shortcuts import render

# Create your views here.
def contact(request):
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
    
    if form.is_valid():
        
        cd = form.cleaned_data
        send_mail(
            cd['Nombre'],
            cd['Mensaje'],
            cd.get('correo','noreply@example.com'),
            ['siteowner@example.com'],
        )
        return HttpResponseRedirect('/contact/thanks/')
    
    else:
        
        form = ContactForm(initial={'correo': 'noreply@example.com'})
        return render_to_response('contact_form.html', {'form':form})
        