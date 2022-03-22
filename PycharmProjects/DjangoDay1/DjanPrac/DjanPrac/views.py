# #I am Sushant
# from django.http import HttpResponse
# def index(Request):
#     s='''
#     <div>
#     <h1>Hello  I am Sushant</h1>
#     <a href=''>You Tube</a><br>
#     <a href=''>Facebook</a><br>
#     <a href=''>Instagram</a><br>
#     <a href=''>Portfolio</a><br>
#     <a href=''>Jamm</a><br>
#     </div>
#     '''
#     return HttpResponse(s)
#
# def about(Request):
#     return HttpResponse('About me Yeah')
from django.http import HttpResponse
from django.shortcuts import render
# def index(request):
#     s='''<button><a href='/removepunc'>Remove Punc</button>'''
#
#     #return HttpResponse()
#     render(request,'index.html')
def analyze(request):
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    print(removepunc)
    analyzed=djtext
    params={'purpose':'Removed pun','analyzed_text':analyzed}

    render(request,'analyze.html',params)
def index(request):
    text1=request.GET.get('text','default')
    print(text1)

    return render(request, 'index.html')
def removepunc(request):
    return HttpResponse('Remove punc')

def capitalizeFirst(request):
    return HttpResponse("Cpaitalize First")

def newlineremove(request):

    return HttpResponse("capitalize first")

def spaceremove(request):

    return HttpResponse("space remover")

def charcount(request):

    return HttpResponse("charcount ")