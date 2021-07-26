from django.shortcuts import render
from .models import QuesModel
from django.http import HttpResponse
from users.forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm




def index(request):

    suf = QuesModel.objects.all()
    #if response.method == 'POST':
    #    print(response.POST)
    #    if response.POST.get(submit):
            #for item in
    #    elif:
    #        pass
    return render(request,'blog/quiz.html',{'suf':suf})


def home(request):

    return render(request,'blog/home.html')

def signup(request):
    form = RegisterForm()

    return render(request,'registration/register.html',{'form':form})
    #return render(request,'registration/register.html')

def login(request):
    form = login(UserCreationForm)

    #return render(request,'registration/login.html',{'form':form})
    return render(request,'register/login.html',{'form':form})

def quiz(request):

    #suf = QuesModel.objects.all()
    #return render(request,'blog/base.html',{'suf':suf})

    if request.method == 'POST':

        print(request.POST)
        suf=QuesModel.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for sufu in suf:
            total+=1
            answer = request.POST.get(sufu.question)
            #print(sufu.ans)
            print(answer)
            #print()
            if sufu.ans ==  answer:
                score+=4
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total

        }
        return render(request,'blog/result.html',context)
    else:
        suf=QuesModel.objects.all()

        #context = {
        #    'suf':suf
        #}
        #return render(request,'Quiz/home.html',context)
    return render(request,'blog/base.html',{'suf':suf})
