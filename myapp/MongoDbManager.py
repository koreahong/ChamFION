from pymongo import MongoClient 
import json

def start(spId, spGrade):
    
    print(spId)
    print(spGrade)
    client = MongoClient()
    # 클래스 객체 할당
    
    client = MongoClient('localhost', 27017)
    # localhost: ip주소
    # 27017: port 번호
    db = client["DBname"]
    collection = db["Collname"]
    # collection = db.coll_이름
    
    #with open('C:\dev\psou\sqm\myapp\static\jsondata\stats.json') as data_file:    
    #   post2 = json.load(data_file)
    
    #post = { 
    #"author" : "BOB", 
    #"text" : "My Second blog post!", 
    #"tags" : ["mongodb", "python", "pymongo"]
    #}
       
    # posts = db.posts
    postss = db.postss
    #post_id = posts.insert_one(post).inserted_id
    #post_id = postss.insert_many(post2)
    #post_id
    
    
    coll_list = db.collection_names()
    #print(coll_list) 
     
    # 콜랙션 삭제
    #db.drop_collection("posts")
    
    #print(postss.find_one())
    
    #
    
    #print(postss.count_documents({'spId': 300230621}))
    
    for doc in postss.find({'spId': spId,'spGrade':spGrade}):
        print('doc is : '+str(doc))
    
    return doc
    #for list in posts.find():
    #    print(list)
    