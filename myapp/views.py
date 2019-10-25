from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import loader
from myapp import imptest
from myapp import finalrun
from myapp import graphchecker
import json


# Create your views here.
    
def IndexFunc(request):
    print(imptest.checker())
    graphchecker.kkk()
    #finalrun.finrun()
    return render(request, 'index.html')

def SearchFunc(request):
    
    if request.GET["ID"] is None:
        
        return render(request, 'search.html', {'ID':""})
    else :
        ID = request.GET["ID"]
        
        return render(request, 'search.html', {'ID':ID})
        #return render(request, 'search.html', {'ID':ID+str(imptest.checker())})
    
def testtem(request):
    return render(request, 'testtem.html')
    
def topplayerFunc(request):
    
    if request.GET["ID"] is None:
    
        return render(request, 'topplayer.html', {'ID':""})
    else :
        ID = request.GET["ID"]
    return render(request, 'topplayer.html', {'ID':ID})

def TOPatkFunc(request):
    return render(request, 'TOPatk.html')
def TOPmidFunc(request):
    return render(request, 'TOPmid.html')
def TOPdefFunc(request):
    return render(request, 'TOPdef.html')

def analysisFunc(request):
    if request.GET["ID"] is None:
        
        return render(request, 'Analysis.html', {'ID':""})
    else :
        ID = request.GET["ID"]
        return render(request, 'Analysis.html', {'ID':ID})

def ajaxproject(request):
    template = loader.get_template('test.html')
    context = {'latest_question_list': "5tte"}  
    return HttpResponse(template.render(context,request))

def searchData(request):
    data = request.POST['msg']
    example = request.POST['exam']
    context = {'msg': data+example, }
    return HttpResponse(json.dumps(context), "application/json")

def squadform(request):
    data = request.POST['msg']
    html =" <div class= \"squadmaker-view__field "+data+"\"> "
    
    for i in range(1,12):
        html +="                       <div id =\"formationPlayer"+ str(i) +"\">"
        html +="                            <img src='/static/images/c000.png'  width=\"120\" height=\"120\" onclick=\"recoplayer("+str(i)+")\"></img>"
        html +="                        </div>"        
    
    html +="                   </div>"
    
    context = {'msg':html,}
    return HttpResponse(json.dumps(context), "application/json")

def Mysquadform(request):
    data = request.POST['msg']
    html =" <div class= \"squadmaker-view__field "+data+"\"> "
    
    for i in range(1,12):
        html +="                       <div id =\"formationPlayer"+ str(i) +"\">"
        html +="                            <img src='/static/images/c000.png'  width=\"120\" height=\"120\" onclick=\"recoplayer("+str(i)+")\"></img>"
        html +="                        </div>"        
    
    html +="                   </div>"
    
    context = {'msg':html,}
    return HttpResponse(json.dumps(context), "application/json")


def recommend(request):
    
    context= {"Pnum":"p214100","Season":"TT","Name":"굴리트","Pay":"22","OVR":"99","Mark":"TT"},{"Pnum":"p1109","Season":"NHD","Name":"말디니","Pay":"21","OVR":"98","Mark":"NHD"},{"Pnum":"p101004231","Season":"ICON","Name":"히바우두","Pay":"25","OVR":"107","Mark":"ICON"}
 
    return HttpResponse(json.dumps(context), "application/json")

def take(request):
    
    context= {}
 
    return HttpResponse(json.dumps(context), "application/json")

        
