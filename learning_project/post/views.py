from django.shortcuts import render
import pymongo
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required

#this is to create new post
def shit(request):
    client = pymongo.MongoClient("mongodb+srv://Dingo:1234@cluster0.8evqx.mongodb.net/")
    mydb = client["POSTS"]
    
    in_game_name=request.GET.get("ign","MADARA")
    role_y_w=request.GET.get("role","member")
    tell_a_y=request.GET.get("content","Tell Us About You")
    coll = mydb[request.user.username]
    
    
    posts=coll.find({})
    post=[]

    for i in posts:
        
        post.append(i)
         
    len_coll=len(post)
    x=post[len_coll]
    y=int(x["id"]-1)
    
    post={
        "id":y,
        "ign":in_game_name,
        "role":role_y_w,
        "content":tell_a_y
            }
    
    if in_game_name!="MADARA":
        coll.insert_one(post)
    return HttpResponse("<html><body><h1>post submitted successfulyy</h1></body></html>")

#this is the view for create a new post you will be redirected to newpost.html file ocated in the template folder in this post folder and the above function will take the input from the front end and put it in the back end and will save it in athe server
@login_required
def create(request):
    return render(request,'newpost.html')

#this function will parse data from mongodb and will show it in frontend in viewpost.html
@login_required  
def viewpost(request):
    client = pymongo.MongoClient("mongodb+srv://Dingo:1234@cluster0.8evqx.mongodb.net/")
    mydb = client["POSTS"]
    coll = mydb[request.user.username]
    posts=coll.find({})
    post=[]
    for i in posts:
        post.append(i)
    
    dict_={
        "post":post
        }
    
    return render(request,'viewpost.html',dict_)

#this func will delete the post user have searched for if he/she clicks the delete button
@login_required
def delete(request):
    client = pymongo.MongoClient("mongodb+srv://Dingo:1234@cluster0.8evqx.mongodb.net/")
    
    mydb = client["POSTS"]
    
    coll = mydb[request.user.username]
    
    ida=request.GET.get("id")
    
    query = {
        "id":int(ida)
        }
    
    coll.delete_one(query)
    
    return HttpResponse("<html><body><h1>Delete Successfully</h1></body></html>")

#this ffunction will update post for the users
@login_required
def update(request):
    client = pymongo.MongoClient("mongodb+srv://Dingo:1234@cluster0.8evqx.mongodb.net/")
    mydb = client["POSTS"]
    coll = mydb[request.user.username]
    ida=request.GET.get("id")
    posts=coll.find_one({"id":int(ida)})
    
    
       
    
    return render(request,'updatepost.html',posts)

def success(request):
    client = pymongo.MongoClient("mongodb+srv://Dingo:1234@cluster0.8evqx.mongodb.net/")
    mydb = client["POSTS"]
    coll = mydb[request.user.username]
    in_game_name=request.GET.get("ign")
    role_y_w=request.GET.get("role")
    tell_a_y=request.GET.get("content")
    ida=int(request.GET.get("id"))
    
    query={
        "id":ida
    }
    
    updated_post={
        "$set":{
        
            "ign":in_game_name,
            "role":role_y_w,
            "content":tell_a_y,
            "id":ida
        }
   
    }
    coll.update_one(query,updated_post)
    return HttpResponse("<html><body><h1>Update Successfully</h1></body></html>")