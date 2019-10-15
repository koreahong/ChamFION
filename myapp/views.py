from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import loader
import json
# Create your views here.
    
def IndexFunc(request):
    return render(request, 'index.html')

def SearchFunc(request):
    
    if request.POST["irum"] is None:
        
        return render(request, 'search.html', {'name':""})
    else :
        irum = request.POST["irum"]
        return render(request, 'search.html', {'name':irum})

    
def topplayerFunc(request):
    return render(request, 'TopPlayer.html')

def TOPatkFunc(request):
    return render(request, 'TOPatk.html')
def TOPmidFunc(request):
    return render(request, 'TOPmid.html')
def TOPdefFunc(request):
    return render(request, 'TOPdef.html')

def analysisFunc(request):
    return render(request, 'Analysis.html')

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
    
    context = {'msg': html, }
    return HttpResponse(json.dumps(context), "application/json")


def recommend(request):
    
    context= {"Pnum":"p214100","Season":"TT","Name":"굴리트","Pay":"22","OVR":"99","Mark":"TT"},{"Pnum":"p1109","Season":"NHD","Name":"말디니","Pay":"21","OVR":"98","Mark":"NHD"},{"Pnum":"p101004231","Season":"ICON","Name":"히바우두","Pay":"25","OVR":"107","Mark":"ICON"}
 
    return HttpResponse(json.dumps(context), "application/json")

def take(request):
    
    context= {}
 
    return HttpResponse(json.dumps(context), "application/json")

        
