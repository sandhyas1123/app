from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact

def list_contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'myapp/list_contacts.html', {'contacts': contacts})

def add_contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phno = request.POST.get("phno")
        regno = request.POST.get("regno")
        company = request.POST.get("company")
        address = request.POST.get("address")
        country = request.POST.get("country")
        Contact.objects.create(name=name, email=email,phno=phno,regno=regno,company=company,address=address,country=country)
        return redirect('list_contacts')
    return render(request, 'myapp/add_contact.html', {})

def edit_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        regno  = request.POST.get("regno")
        address = request.POST.get("address")
        contact.name = name
        contact.email = email
        contact.regno = regno
        contact.address = address
        contact.save()
        return redirect('list_contacts')

    return render(request, 'myapp/edit_contact.html', {'contact': contact})

def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    contact.delete()
    return redirect('list_contacts')
