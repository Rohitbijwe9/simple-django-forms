from django.shortcuts import render
from .forms import CalcyForm

def CalcyView(request):
    template_name = 'Calcy/calcy.html'
    result = None
    msg = ''

    if request.method == 'POST':
        form = CalcyForm(request.POST)
        if form.is_valid():
            val1 = form.cleaned_data['value1']
            val2 = form.cleaned_data['value2']
            op = form.cleaned_data['operation']

            try:
                if op == '+':
                    result = val1 + val2
                elif op == '-':
                    result = val1 - val2
                elif op == '*':
                    result = val1 * val2
                elif op == '/':
                    if val2 == 0:
                        msg = 'Cannot divide by zero.'
                    else:
                        result = val1 / val2
                else:
                    msg = 'Invalid operator.'
            except Exception as e:
                msg = f"Error: {str(e)}"
    

    context = {'form': form, 'result': result, 'msg': msg}
    return render(request, template_name, context)
