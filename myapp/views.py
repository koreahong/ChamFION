from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import loader
from myapp import imptest
from myapp import MongoDbManager
from myapp import graphchecker
import json


# Create your views here.
    
def IndexFunc(request):
    print(imptest.checker())
    graphchecker.kkk()
    MongoDbManager.start()
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
    html =""
    for i in range(0,11):  
        nlist = request.POST['list['+str(i)+'][spId]']
        olist = request.POST['list['+str(i)+'][spPosition]']
        print(olist)
        
        k = 3;
        while nlist[k:k+1] == '0':
            print(k)
            k = k + 1
            
        
        spSeason = nlist[:3]
        spID = nlist[k:]
        print('spSeason :'+ spSeason +' and spID : '+ spID)
            
            
        
        with open('C:\dev\psou\sqm\myapp\static\jsondata\seasonID.json') as data_file:    
            seasondata = json.load(data_file)
            j = 0;
            backurl =""
            
            while str(seasondata[j]["seasonId"]) != spSeason:
                j = j + 1
                
            backurl = seasondata[j]["url"]
            Mark = seasondata[j]["className"]
            
            #json_string = seasondata[0]["className"]
            #print(json_string)
        
        with open('C:\dev\psou\sqm\myapp\static\jsondata\spids.json') as data_file2:
            spid = json.load(data_file2)
            j = 0;
            
            print('full spID  :'+ nlist)
            while str(spid[j]["id"]) != nlist:
                j = j + 1
                
            Name = spid[j]["name"]
            print(Name)            
            #json_string = seasondata[0]["className"]
            #print(json_string)    
        
        html +=" <div class= \"squadmaker-view__field mySquad\"> "
        html +="                       <div id =\"formationPlayerspp"+ request.POST['list['+str(i)+'][spPosition]'] +"\">"
        html +="                            <img src="+backurl+" width=\"120\" height=\"120\" onclick=\"recoplayer("+request.POST['list['+str(i)+'][spPosition]']+")\">"
        html +="                            <img style=\"position: absolute; top: 14%;left:35%;\" src=\"http://http://fo4.dn.nexoncdn.co.kr/live/externalAssets/common/playersAction/"+nlist+".png?rd=201910290610\" onerror=\"this.src='https://fo4.dn.nexoncdn.co.kr/live/externalAssets/common/players/p"+spID+".png?rd=201910290610'\" width=\"72\" height=\"72\" onclick=\"recoplayer("+request.POST['list['+str(i)+'][spPosition]']+")\">"
        html +="                            <img style=\"position: absolute; top: 60%;left:11%;\" src=\"http://s.nx.com/s2/game/fo4/obt/externalAssets/season/"+Mark+".png\" width=\"15px\" height=\"12px\" onclick=\"searchplayer(i)\">"
        html +="                            <div style=\"width:100px; top:50%; left:50%; position: absolute; transform:translate(-50%,50%)\"><p style=\"text-align:center; font-family:맑은고딕;\"><font size=\"1.8\" color=\"black\">"+ Name +"</font></p></div>"
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

        
