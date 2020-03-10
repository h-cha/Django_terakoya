from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Input,Question
from .forms import TerakoyaForm,IDForm,HelloForm
from django.views.generic import TemplateView
import random

def home(request):
    params = {
            'title':'Welcome',
            'msg':'',
            'goto':'Ksetumei',
            'goto1':'Rsetumei',
            'goto_memo':'計算の工夫',
            'goto1_memo':'ルートの計算',
            'home':'home',
            }
    return render(request,'terakoya/home.html',params)

def Ksetumei(request):
    params = {
            'title':'計算の工夫',
            'msg':'',
            'goto':'Kcreate',
            'goto_memo':'問題',
            'home':'home'
            }
    return render(request,'terakoya/Ksetumei.html',params)


  
def Kresult(request):
    last = Input.objects.all().last()
    deta = [last]
    params = {
            'title':'結果',
            'msg':'よく頑張りました!',
            'msg1':'問題番号を入力すると答えがでます',
            'form':IDForm(),
            'memo':'',
            'question':[],
            'deta':deta,
            'goto':'Kcreate',
            'goto_memo':'他の問題を解く',
            'home':'home',
            }
    if(request.method == 'POST'):
        num = request.POST['id']
        form = IDForm(request.POST)
        if(form.is_valid()):
            item = Question.objects.get(id=num)
            params['memo'] = '正しい答え'
            params['question'] = [item]
            params['form'] = IDForm(request.POST)
        else:
            params['memo'] = 'もう一度問題番号を入力してください'
    return render(request,'terakoya/Kresult.html',params)



#create model
def Kcreate(request):
    num = Question.objects.all().count()
    r = random.randint(1,num)
    question = Question.objects.get(id=r)
    q = [question]
    params = {
            'title':'問題',
            'memo':'問題番号:',
            'form':TerakoyaForm(),
            'home':'home',
            'question':q,
            'message':'回答欄',
            'msg1':'まず問題番号を入力してください',
            }
    if(request.method == 'POST'):
        form = TerakoyaForm(request.POST)
        if(form.is_valid()):
            q_num = int(request.POST['q_num'])
            a1 = int(request.POST['a1'])
            a2 = int(request.POST['a2'])
            a3 = int(request.POST['a3'])
            a4 = int(request.POST['a4'])
            a5 = int(request.POST['a5'])
            inputdeta = Input(q_num=q_num,a1=a1,a2=a2,a3=a3,a4=a4,a5=a5)
            inputdeta.save()
            return redirect(to='Kresult')
        else:
            params['memo'] = 'もう一度問題番号を入力してください'
        
    return render(request,'terakoya/Kcreate.html',params)




def Rsetumei(request):
    params = {
            'title':'ルートの計算',
            'msg':'',
            'goto':'Rquestion',
            'goto_memo':'問題',
            'home':'home'
            }
    return render(request,'terakoya/Rsetumei.html',params)

def Rquestion(request):
    params = {
            'title':'問題',
            'msg':'解いてみよう',
            'goto':'Rresult',
            'goto_memo':'結果',
            'home':'home',
            'form':HelloForm(),
            'num1':random.randint(0, 100),
            'num2':random.randint(0, 100),
            'num3':random.randint(0, 100),
            'num4':random.randint(0, 100),
            }
    class HelloView(TemplateView):

        def __init__(self):
            self.params = {
                    'title': 'Hello',
                    'form': HelloForm(),
                    'result': None
                    }

        def get(self,request):
            return render(request, 'terakoya/Rquestion.html', self.params)
    
        def post(self,request):
            ch = request.POST['choice']
            self.params['result'] = 'selected: "' + ch +'".'
            self.params['form'] = HelloForm(request.POST)
            return render(request, 'terakoya/Rquestion.html', self.params)
    return render(request,'terakoya/Rquestion.html',params)




def Rresult(request):
    params = {
            'title':'結果',
            'msg':'よく頑張りました!',
            'goto':'Rsetumei',
            'goto_memo':'説明に戻る',
            'home':'home',
            }
    return render(request,'terakoya/index.html',params)