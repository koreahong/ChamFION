from pymongo import MongoClient 
import json

def start():
    client = MongoClient()
    # 클래스 객체 할당
    
    client = MongoClient('localhost', 27017)
    # localhost: ip주소
    # 27017: port 번호
    db = client["DBname"]
    collection = db["Collname"]
    # collection = db.coll_이름
    
    with open('C:\dev\psou\sqm\myapp\static\jsondata\stats.json') as data_file:    
        post2 = json.load(data_file)
    
    #post = { 
    #"author" : "BOB", 
    #"text" : "My Second blog post!", 
    #"tags" : ["mongodb", "python", "pymongo"]
    #}
       
    posts = db.posts
    #post_id = posts.insert_one(post).inserted_id
    post_id = posts.insert_many(post2)
    post_id
    
    
    coll_list = db.collection_names()
    print(coll_list) 
     
    # 콜랙션 삭제
    #db.drop_collection("posts")
    
    print(posts.find_one())
    
    
    #for list in posts.find():
    #    print(list)
    