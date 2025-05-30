from django.shortcuts import render,redirect
from . forms import UserForm


'''
def UserFormView(request):
    template_name = 'app1/UserForm.html'
    message = ''
    data = {}

    if request.method == 'POST':
        first = request.POST.get('first_name', '')
        last = request.POST.get('last_name', '')
        mobile = request.POST.get('mobile', '')
        email = request.POST.get('email', '')

        if not first:
            message = 'First name required'
        elif not last:
            message = 'Last name required'
        elif len(mobile) < 10 or len(mobile) > 13 or not mobile.isdigit():
            message = 'Mobile number invalid'
        elif '@' not in email or '.' not in email:
            message = 'Email invalid'
        else:
            data = {'first': first, 'last': last, 'mobile': mobile, 'email': email}

            request.session['form_info'] = {'first': first,'last': last,'mobile': mobile,'email': email}

            #return redirect('show_url')
    return render(request,template_name,{'message': message, 'data': data})





def show(request):
    template_name='app1/show.html'
    d=request.session.get('form_info')
    if d:
        context={'data':d}
        request.session.clear()
        return render(request,template_name,context)

    return redirect('userform_url')

'''

def UserFormView(request):
    template_name = 'app1/user_form.html'
    form = UserForm()
    #print(form)
    #print('method is:',request.method)

    if request.method == 'POST':
        form = UserForm(request.POST)
        #print(request.POST)
        if form.is_valid():
            #form.save()
            request.session['user_data'] = request.POST
            return redirect('show_url')
    

    context = {'form': form}
    return render(request, template_name, context)


def show_user_view(request):
    template_name = 'app1/show_user.html'
    data = request.session.get('user_data')
    if not data:
        print('not data')
        return redirect('user_url')

    context={'data':data}
    request.session.pop('user_data', None)
    return render(request,template_name ,context)

    



