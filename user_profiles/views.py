from django.shortcuts import render, redirect, reverse
from .models import Profile, User, UserAgent, Contact
from django.contrib.auth import login, authenticate, logout
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from .forms import CustomerSignUpForm, UserAgentSignUpForm, LoginForm, ContactMessageForm
from django.contrib.auth.decorators import login_required


class CustomerSignUpView(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'registration/customer_register.html'#optionally the original registration/signup.html

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('products:product_list')#Redirect to the products page and the user can buy products

class UserAgentSignUpView(CreateView):
    model = User
    form_class = UserAgentSignUpForm
    template_name = 'registration/agent_register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'agent'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('django_chatter:index')#Redirect to the agent page where they can manage usres from 

#login for he customer
def testlogin(request):
        # username = request.POST['username']
        # password = request.POST['password']
   
    msg = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None and user.user_type == 1:
                login(request, user)
                # Redirect to a success page.
                return redirect('products:product_list')
            else:
                msg = 'Invalid Username or Password'
    else:
        form = LoginForm()              
    context = {
        'msg': msg,
        'form': form,
    }    
    return render(request, 'user_profiles/customerlogin.html', context)    


#login for he customer

def mylogin(request):
        # username = request.POST['username']
        # password = request.POST['password']
   
    msg = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                 
            else:
                msg = 'Invalid Username or Password'
    else:
        form = LoginForm()              
    context = {
        'msg': msg,
        'form': form,
    }    
    return render(request, 'registration/mylogin.html', context)    



def login_success(request):
    """
    Redirects users based on whether they are in the admins group
    """

    if request.user.user_type == 2:
        # Redirect to a success page.
        user_id = request.user.id
        #return redirect('seller:seller_detail', args=[user_id],)  
        #return redirect(reverse('seller:seller_detail', args=(user_id,))) 
        return redirect('seller:profile')
       
    elif request.user.user_type == 1:    
        return redirect('products:product_list')
    elif request.user.user_type == 3:    
        return redirect('django_chatter:index')   
    else:
       return "No account Found Pliiz"



    # @login_required
    # def mylogin(request):
            
    
    #     msg = ''
    #     if request.method == 'POST':
    #         form = LoginForm(request.POST)
    #         if form.is_valid():
    #             username = form.cleaned_data['username']
    #             password = form.cleaned_data['password']
    #             user = authenticate(request, username=username, password=password)
    #             if user is not None and user.is_active:
    #                 login(request, user)
    #                 user_type = user.user_type
    #                 if user.user_type == 2:
    #                     # Redirect to a success page.
    #                     return redirect('seller:seller_detail', args=(user.id,))
    #                 elif user.user_type == 1:    
    #                     return redirect('products:product_list')
    #                 elif user.user_type == 3:    
    #                     return redirect('django_chatter:chatroom')    
    #             else:
    #                 msg = 'Invalid Username or Password'
    #     else:
    #         form = LoginForm()              
    #     context = {
    #         'msg': msg,
    #         'form': form,
    #     }    
    #     return render(request, 'registration/login.html', context)    


def mylogout(request):
    logout(request)
    return redirect('products:home')   
    # Redirect to a success page or the home page.


def contact(request):#Create the contact form and submit the data to the backend for processing
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            contact = Contact.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message']
            )
            contact.save()
            return redirect('products:product_list')#Redirect back to the account and not the list
    else:
        form = ContactMessageForm() 
    context = {
        'form': form,
        #'contact': contact,#You may not want to display a contact message
    }           
    return render(request, 'user_profiles/contact.html', context)
