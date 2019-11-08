from django.http.response import HttpResponse
import numpy as np
import pandas as pd
from django.shortcuts import render
from django.template import loader
from myapp import MongoDbManager
from myapp import MLExecution_549
import json
# Create your views here.

def detail(request):
    spid = request.GET["spid"]
    spgrade = request.GET["spgrade"]
    
    context = {'spid':spid, 'spgrade':spgrade}
    return render(request, 'detail.html', context)

def spdetail(request):
    spid = request.GET["spid"]
    spgrade = request.GET["spgrade"]
    
    if int(spgrade) < 2 :
        gradecolor = "grey"
    elif int(spgrade) < 5:
        gradecolor = "bronze"
    elif int(spgrade) < 8:
        gradecolor = "silver"
    elif int(spgrade) < 11:
        gradecolor = "gold"
    
    print('=========')
    print(spid +"and" + spgrade)
    print('=========')
    doc = MongoDbManager.start(int(spid), int(spgrade))
    #print (doc['Acceleration'])
    html  =""
    
    nlist = str(doc['spId'])
    print(nlist)
    glist = str(doc['spGrade'])
    print(glist)
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
    
    html +="<div style=\"width:150px; float:left; margin-right:50px; \">"
    html +="<img src="+backurl+" style=\"width:188px; height:302px;\">"
    html +="<img style=\"position: absolute; top: 28.5%;left:8.5%; width:140px; height:140px;\" src=\"http://fo4.dn.nexoncdn.co.kr/live/externalAssets/common/playersAction/p"+nlist+".png?rd=201910290610\" onerror=\"this.src='https://fo4.dn.nexoncdn.co.kr/live/externalAssets/common/players/p"+spID+".png?rd=201910290610'\" >"
    html +="<div style=\"width:100px; top:48%; left:11.5%; position: absolute; transform:translate(-50%,50%)\"><p style=\"text-align:center; font-family:맑은고딕;\"><font size=\"3\" color=\"black\">"+ Name +"</font></p></div>"
    html +="<div style=\"background-image: url(http://s.nx.com/s2/game/fo4/obt/sprite_191007.png); background-position: 20.5px -701px; width:70px; top:57%; left:11.9%; position: absolute; transform:translate(-50%,50%)\"><p style=\"text-align:center; font-family:맑은고딕;\"><font size=\"3\" color=\"black\">"+ str(doc['spGrade']) +"</font></p></div>"
    html +="<img style=\"position: absolute; top: 48.2%;left:5.9%;\" src=\"http://s.nx.com/s2/game/fo4/obt/externalAssets/season/"+Mark+".png\">"
    html +="<div class=\""+gradecolor+"\"><p ><font class=\"gradefont\" size=\"1.8\" color=\"black\">"+ glist +"</font></p></div>"
    html +="</div>"
    
    
    html += "<br><h1>&nbsp&nbsp&nbsp&nbsp&nbsp"+Name+"</h1><ul>"
    html += "<li ><div class=\"detaillist\">속력</div><div>"+str(doc['Acceleration'])+"</div></li>"
    html += "<li ><div class=\"detaillist\">가속력</div><div>"+str(doc['Sprint Speed'])+"</div></li>"
    html += "<li ><div class=\"detaillist\">드리블</div><div>"+str(doc['Dribbling'])+"</div></li>"
    html += "<li ><div class=\"detaillist\">볼컨트롤</div><div>"+str(doc['Ball Control'])+"</div></li>"
    html += "<li ><div class=\"detaillist\">짧은 패스</div><div>"+str(doc['Short Passing'])+"</div></li>"
    html += "<li ><div class=\"detaillist\">골 결정력</div><div>"+str(doc['Finishing'])+"</div></li>"
    html += "<li ><div class=\"detaillist\">슛 파워</div><div>"+str(doc['Shot Power'])+"</div></li>"
    html += "</ul>"
    
    html += "<ul>"
    html += "<li ><div class=\"detaillist\">헤더</div><div>"+str(doc['Heading'])+"</div></li>"
    html += "<li ><div class=\"detaillist\">중거리 슛</div><div>"+str(doc['Long Shots'])+"</div></li>"
    html += "<li ><div class=\"detaillist\">위치선정</div><div>"+str(doc['Positioning'])+"</div></li>"
    html += "<li ><div class=\"detaillist\">시야</div><div>"+str(doc['Vision'])+"</div></li>"
    html += "<li ><div class=\"detaillist\">반응속도</div><div>"+str(doc['Reactions'])+"</div></li>"
    html += "<li ><div class=\"detaillist\">발리 슛</div><div>"+str(doc['Volleys'])+"</div></li>"
    html += "<li ><div class=\"detaillist\">페널티 킥</div><div>"+str(doc['Penalties'])+"</div></li>"
    html += "</ul>"
    
    html += "<ul>"
    html += "<li ><div class=\"detaillist\">크로스</div><div>"+str(doc['Crossing'])+"</div></li>"
    html += "<li ><div class=\"detaillist\">긴 패스</div><div>"+str(doc['Long Passing'])+"</div></li>"
    html += "<li ><div class=\"detaillist\">프리킥</div><div>"+str(doc['Free Kick'])+"</div></li>"
    html += "<li ><div class=\"detaillist\">커브</div><div>"+str(doc['Curve'])+"</div></li>"
    html += "<li ><div class=\"detaillist\">민첩성</div><div>"+str(doc['Agility'])+"</div></li>"
    html += "<li ><div class=\"detaillist\">밸런스</div><div>"+str(doc['Balance'])+"</div></li>"
    html += "<li ><div class=\"detaillist\">대인 수비</div><div>"+str(doc['Marking'])+"</div></li>"
    html += "</ul>"
    
    html += "<ul>"
    html += "<li ><div class=\"detaillist\">태클</div><div>"+str(doc['Standing Tackle'])+"</div></li>"
    html += "<li ><div class=\"detaillist\">가로채기</div><div>"+str(doc['Interceptions'])+"</div></li>"
    html += "<li ><div class=\"detaillist\">슬라이딩 태클</div><div>"+str(doc['Sliding Tackle'])+"</div></li>"
    html += "<li ><div class=\"detaillist\">몸싸움</div><div>"+str(doc['Strength'])+"</div></li>"
    html += "<li ><div class=\"detaillist\">스테미너</div><div>"+str(doc['Stamina'])+"</div></li>"
    html += "<li ><div class=\"detaillist\">적극성</div><div>"+str(doc['Aggression'])+"</div></li>"
    html += "<li ><div class=\"detaillist\">점프</div><div>"+str(doc['Jumping'])+"</div></li>"
    html += "</ul>"
    
    html += "<ul>"
    html += "<li ><div class=\"detaillist\">침착성</div><div>"+str(doc['Composure'])+"</div></li>"
    html += "<li ><div class=\"detaillist\">GK 다이빙</div><div>"+str(doc['GK Diving'])+"</div></li>"
    html += "<li ><div class=\"detaillist\">GK 핸들링</div><div>"+str(doc['GK Handling'])+"</div></li>"
    html += "<li ><div class=\"detaillist\">GK 킥</div><div>"+str(doc['GK Kicking'])+"</div></li>"
    html += "<li ><div class=\"detaillist\">GK 반응속도</div><div>"+str(doc['GK Reflexes'])+"</div></li>"
    html += "<li ><div class=\"detaillist\">GK 위치선정</div><div>"+str(doc['GK Positioning'])+"</div></li>"
    html += "</ul>"
    
    html += ""
    
    context = {'msg':html,}
    return HttpResponse(json.dumps(context), "application/json")
    
def IndexFunc(request):
    #print(imptest.checker())
    #graphchecker.kkk()
    realrecommend()
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
        glist = request.POST['list['+str(i)+'][spGrade]']
        
        if int(glist) < 2 :
            gradecolor = "grey"
        elif int(glist) < 5:
            gradecolor = "bronze"
        elif int(glist) < 8:
            gradecolor = "silver"
        elif int(glist) < 11:
            gradecolor = "gold"
            
        k = 3;
        while nlist[k:k+1] == '0':
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
        html +="                            <img style=\"position: absolute; top: 14%;left:35%;\" src=\"http://fo4.dn.nexoncdn.co.kr/live/externalAssets/common/playersAction/p"+nlist+".png?rd=201910290610\" onerror=\"this.src='https://fo4.dn.nexoncdn.co.kr/live/externalAssets/common/players/p"+spID+".png?rd=201910290610'\" width=\"72\" height=\"72\" onclick=\"recoplayer("+request.POST['list['+str(i)+'][spPosition]']+")\">"
        html +="                            <img style=\"position: absolute; top: 57.5%;left:10%;\" src=\"http://s.nx.com/s2/game/fo4/obt/externalAssets/season/"+Mark+"_big.png\" width=\"18px\" height=\"18px\" onclick=\"searchplayer(i)\">"
        html +="                            <div style=\"width:100px; top:50%; left:50%; position: absolute; transform:translate(-50%,50%)\"><p style=\"text-align:center; font-family:맑은고딕;\"><font size=\"1.8\" color=\"black\">"+ Name +"</font></p></div>"
        html +="                            <div class=\""+gradecolor+"\"><p ><font class=\"gradefont\" size=\"1.8\" color=\"black\">"+ glist +"</font></p></div>"
        html +="                        </div>"        
        html +="                   </div>"
        
    context = {'msg':html,}
    return HttpResponse(json.dumps(context), "application/json")


def recommend(request):
    # 추천 알고리즘 들어가야 할 곳
    
    list_tuples = [        
       #( 'spId\' :'+request.POST['list[0][spId]'], int(request.POST['list[0][spPosition]']), request.POST['list[0][spGrade]']),
       (request.POST['list[0][spId]'], int(request.POST['list[0][spGrade]']), int(request.POST['list[0][spPosition]'])),
       (request.POST['list[1][spId]'], int(request.POST['list[1][spGrade]']), int(request.POST['list[1][spPosition]'])),
       (request.POST['list[2][spId]'], int(request.POST['list[2][spGrade]']), int(request.POST['list[2][spPosition]'])),
       (request.POST['list[3][spId]'], int(request.POST['list[3][spGrade]']), int(request.POST['list[3][spPosition]'])),
       (request.POST['list[4][spId]'], int(request.POST['list[4][spGrade]']), int(request.POST['list[4][spPosition]'])),
       (request.POST['list[5][spId]'], int(request.POST['list[5][spGrade]']), int(request.POST['list[5][spPosition]'])),
       (request.POST['list[6][spId]'], int(request.POST['list[6][spGrade]']), int(request.POST['list[6][spPosition]'])),
       (request.POST['list[7][spId]'], int(request.POST['list[7][spGrade]']), int(request.POST['list[7][spPosition]'])),
       (request.POST['list[8][spId]'], int(request.POST['list[8][spGrade]']), int(request.POST['list[8][spPosition]'])),
       (request.POST['list[9][spId]'], int(request.POST['list[9][spGrade]']), int(request.POST['list[9][spPosition]'])),
       (request.POST['list[10][spId]'], int(request.POST['list[10][spGrade]']), int(request.POST['list[10][spPosition]'])),
     
    ]
    
    
    
    '''    paytotal = 0
    for i in range(0,11):
        temp = int(request.POST['list['+str(i)+'][spId]'])
        temp2 = int(request.POST['list['+str(i)+'][spGrade]'])
        print('temp is : '+str(temp))
        print('temp2 is : '+str(temp2))
        doc = MongoDbManager.start(temp, temp2)
        
        paytotal += doc['pay']
        
    print(paytotal)
    print('hi')'''
    
    sortedlist = (sorted(list_tuples, key=lambda list: list[2]))
    
    
    totalpay =0
    totalprice =0
    for i in range(0,10):
        
        totalpay += MLExecution_549.getprice(request.POST['list['+str(i)+'][spId]'], request.POST['list['+str(i)+'][spGrade]']).iloc[0]['pay']
        totalprice += MLExecution_549.getprice(request.POST['list['+str(i)+'][spId]'], request.POST['list['+str(i)+'][spGrade]']).iloc[0]['price']
    totalpay = int(totalpay)
    totalprice = int(totalprice/100000000)
    
    after_tuples = [ 
        (totalpay, float('NaN'), 'pay_total'),
        (totalprice, float('NaN'), 'price_total'),
        ('맨체스터 시티', float('NaN'), 'teamColor'),
    ]
    
    seclist = np.vstack([sortedlist,after_tuples])

    
    sorteddf = pd.DataFrame(seclist, columns=["spId", "spGrade", "positionNum"])
    
    sortedlist2 = sorteddf[sorteddf.positionNum != request.POST['selectedposition']]
    print('==sort2==')
    print(sortedlist2)
    
    sortedlist2['spGrade']=sortedlist2['spGrade'].astype('float')
      
    
    #dict_sj = json.loads(stringjson)
    nameList = pd.DataFrame(sortedlist2)  
    print(nameList)  
    
    resultvalue = MLExecution_549.useModel(nameList)
    
    print(int(resultvalue.iloc[0]['spId']))
    
    
    if int(int(resultvalue.iloc[0]['spGrade'])) < 2 :
        gradecolor = "grey"
    elif int(int(resultvalue.iloc[0]['spGrade'])) < 5:
        gradecolor = "bronze"
    elif int(int(resultvalue.iloc[0]['spGrade'])) < 8:
        gradecolor = "silver"
    elif int(int(resultvalue.iloc[0]['spGrade'])) < 11:
        gradecolor = "gold"
        
    k = 3;
    while str(resultvalue.iloc[0]['spId'])[k:k+1] == '0':
        print(k)
        k = k + 1
        
    spSeason = str(int(resultvalue.iloc[0]['spId']))[:3]
    spID = str(int(resultvalue.iloc[0]['spId']))[k:]
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
        
        print('full spID  :'+ str(int(resultvalue.iloc[0]['spId'])))
        while str(spid[j]["id"]) != str(int(resultvalue.iloc[0]['spId'])):
            j = j + 1
            
        Name = spid[j]["name"]
        print(Name)            
        #json_string = seasondata[0]["className"]
        #print(json_string)    

    
    
    
    
    #print(sorted(request.POST[list[0]], key=itemgetter(1)))
    context= {"fullspId":str(int(resultvalue.iloc[0]['spId'])),"Pnum":"p"+str(spID),"Season":Mark,"Name":Name,"Pay":str(int(resultvalue.iloc[0]['pay'])),"Price": str(int(resultvalue.iloc[0]['price'])) ,"spGrade":str(int(resultvalue.iloc[0]['spGrade'])),"Mark":Mark},{"Pnum":"p1109","Season":"NHD","Name":"말디니","Pay":"21","OVR":"98","Mark":"NHD"},{"Pnum":"p101004231","Season":"ICON","Name":"히바우두","Pay":"25","OVR":"107","Mark":"ICON"}
    return HttpResponse(json.dumps(context), "application/json")


def realrecommend():
    
    nameList = pd.DataFrame(
    {'spId' : [300192119 , 300188377 , 215212218 , 214184432 , 216183277 , 207215914 , 214003647 , 215218667 , 211192985 , 215153079 , 175 , 8 , '첼시, 맨체스터 시티'],
    'spGrade' : [5, 6,1,5,1,6,4,1,1,1,None,None,None],
     'positionNum' : [0,3,6,7,9,11,12,16,18,25,'pay_total' , 'price_total' , 'teamColor']})
    
    
    MLExecution_549.useModel(nameList)


def take(request):
    
    context= {}
 
    return HttpResponse(json.dumps(context), "application/json")

        
