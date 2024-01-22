from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Account
from .forms import accountForm
# Create your views here.

# Display the list of all accounts
def index(request):
    return render(request, 'accounts/index.html',{ #Renders the 'accounts/index.html' template.
        'accounts': Account.objects.all()          #Retrieves all accounts from the database using Account.objects.all().
    })

# Search for accounts based on a query parameter 'q'
def search_account(request):
    if request.method == 'GET':
        query = request.GET.get('q', '')
        accounts = Account.objects.filter(
            first_name__icontains=query) | Account.objects.filter(
            last_name__icontains=query) | Account.objects.filter(
            email__icontains=query) | Account.objects.filter(
            sex__icontains=query) | Account.objects.filter( 
            residence__icontains=query) # Add more fields as needed

        return render(request, 'accounts/search_results.html', {'query': query, 'accounts': accounts})
    return render(request, 'accounts/index.html')
        
# Dummy function for viewing an account (redirects to index)
def view_account(request, id):
    return HttpResponseRedirect(reverse('index'))

# Add a new account to the database
def add_account(request):
    if request.method == 'POST':
        form = accountForm(request.POST)
        if form.is_valid():
            new_account_number = form.cleaned_data['account_number']
            new_email = form.cleaned_data['email']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_sex = form.cleaned_data['sex']
            new_residence = form.cleaned_data['residence']

            new_account = Account(
                account_number = new_account_number,
                email = new_email,
                first_name = new_first_name,
                last_name = new_last_name,
                sex = new_sex,
                residence = new_residence
            )
            new_account.save()
            return render(request, 'accounts/add.html', {
                'form': accountForm(),
                'success': True
            })
    else:
        form = accountForm()
    return render(request, 'accounts/add.html', {
        'form': accountForm()
    })

# Update an existing account
def update(request, id):
    if request.method == 'POST':
        account = Account.objects.get(pk=id)
        form = accountForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            return render(request, 'accounts/update.html', {
                'form': form,
                'success': True
            })
    else:
        account = Account.objects.get(pk=id)
        form = accountForm(instance=account)
    return render(request, 'accounts/update.html', {
        'form': form
    })

# Delete an existing account
def delete(request, id):
  if request.method == 'POST':
    account = Account.objects.get(pk=id)
    account.delete()
  return HttpResponseRedirect(reverse('index'))
