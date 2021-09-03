from django.core import paginator
from django.shortcuts import render
from .models import QuesModel
from django.http import HttpResponse
from users.forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator





def logout(request):
    auth_logout(request)
    return redirect('/login')


def start(request):
    return render(request, 'blog/welcome.html')


@login_required
def report(request):
    suf = QuesModel.objects.all()
    for sufu in suf:
        template_path = 'blog/report.html'
        #context = {'suf': suf}
        context = {'suf': sufu.question}

        # Create a Django response object, and specify content_type as pdf
        response = HttpResponse(content_type='application/pdf')
        # if you to download the pdf file:
        #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
        # if you need to display the pdf file:
        response['Content-Disposition'] = 'filename="report.pdf"'
        # find the template and render it.
        template = get_template(template_path)
        html = template.render(context)

        # create a pdf
        pisa_status = pisa.CreatePDF(
            html, dest=response)
        # if error then show some funy view
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response


def index(request):

    suf = QuesModel.objects.all()
    # if response.method == 'POST':
    #    print(response.POST)
    #    if response.POST.get(submit):
    # for item in
    #    elif:
    #        pass
    request.session.set_test_cookie()
    return render(request, 'blog/home.html')

# def loggedout(request):
 #  try:
#      del request.session['form']
 #  except:
#      pass
 #  return HttpResponse("<strong>You are logged out.</strong>")


# def report(request):

    # return render(request,'blog/report.html')

# def report(request):

#    return render(request,'blog/result.html')


def home(request):
    # if request.session.test_cookie_worked():
    #    request.session.delete_test_cookie()
    #    else:
    #        request.session.set_test_cookie()
    #    messages.error(request, 'Please enable cookie')
    suf = QuesModel.objects.all()
    #context = {'sufu':suf}
    p = Paginator(suf, 1)
    page_num = request.GET.get('page', 5)
    page = p.page(page_num)
    context = {'suf': page}

    return render(request, 'blog/home.html', context)


def signup(request):
    form = RegisterForm()

    return render(request, 'registration/register.html', {'form': form})
   # return render(request,'registration/register.html')


def login(request):
    form = ' logged in'

    if request.method == 'POST':
        form = login(UserCreationForm)

        if form.is_valid():
            username = form.cleaned_data['form']
            request.session['form'] = form
        else:
            form = login(UserCreationForm)

    return render(request, 'register/login.html', {"form": form})

# def login(request):
#    form = login(UserCreationForm)

    # return render(request,'registration/login.html',{'form':form})
#    return render(request,'register/login.html',{'form':form})


def formView(request):
    if request.session.has_key('form'):
        username = request.session['form']
        return render(request, 'register/login.html', {"form": form})
    else:
        return render(request, 'registration/logout.html', {})


@login_required
def quiz(request):
    #print(request.session)
    #print(dir(request.session))
    #
    'session_key', 'set_expiry'
    #
    key = request.session.session_key
    print(key)
    suf = QuesModel.objects.all()
    #context = {'sufu':suf}
    paginator = Paginator(suf, 2)
    page = request.GET.get('page', 1)
    #page = p.page(page_num)
    msufu = paginator.page(page)
    #results = {'msufu':page}

    if request.method == 'POST':
        #print(request.POST)
        data = request.POST
        data_ = dict(data.lists())
        #print(type(data_))
        #print(data_)
        print(data)
        
        for k in data_.keys():
            print('key:',k)
       # print(type(data))
        score = 0
        wrong = 0
        correct = 0
        total = 0
        for sufu in suf:
            total += 1
            answer = request.POST.get(sufu.id)
            print(sufu.ans)
            print(answer)
            # print()
            if sufu.ans == answer:
                score += 4
                correct += 1
            else:
                wrong += 1
        percents = score/(total*4) * 100
        percent = round(percents, 1)
        result = context = {
            'score': 28,
            'time': request.POST.get(''),
            'correct': 7,
            'wrong': 8,
            'percent': 46.7,
            'total': total

        }

    #    html = template.render(context)

    #    pisa_status = pisa.CreatePDF(
    #       html, dest=response)

    #    if pisa_status.err:
    #       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    #    return response

        return render(request, 'blog/result.html', context)
        save(render(request, 'blog/result.html', context))
    else:
        suf = QuesModel.objects.all()

    return render(request, 'blog/quiz.html', {'msufu': msufu})

