from django.shortcuts import render
from django.http import HttpResponse


#backend of home page
def home(request):
    if request.user.is_authenticated:
        roles={
        "cur_user":request.user.username,
        "users":[
            {
                'name':'Dingo',
                'role':'Senpai Of PC Gaming',
                'game': 'CS:GO God',
            }, 
            {
                'name':'Complex',
                'role':'Senpai Of PC Gaming',
                'game':'R6 God'
            }
        ]
    }
    else:
        roles={
            "users":[
            {
               'name':'Dingo',
               'role':'Senpai Of PC Gaming',
               'game': 'CS:GO God',
            }, 
            {
               'name':'Complex',
               'role':'Senpai Of PC Gaming',
               'game':'R6 God'
            }
       ]
    }
    return render(request,'home.html',roles)

#backend of about page
def about(request):
    return render(request,'about.html')

#backend of datacenter
def datacenter(request):
    import pymongo
    myclient=pymongo.MongoClient("mongodb+srv://Dingo:1234@cluster0.8evqx.mongodb.net/")
    mydb=myclient["DP"]
    coll=mydb["userinfo"]
    user1={
        "_id":"001",
        'name':'Dingo',
        'role_':['Senpai Of PC Gaming','Ninja'],
        'game': 'CS:GO God',    
    }
    
    user2={
        "_id":"002",
        'name':'Complex',
        'role_':['Senpai Of PC Gaming'],
        'game': 'R6 God',
    }
    coll.insert_many([user1,user2])
    print("data sent successfully")
    return HttpResponse("<html><body><h1>welcome to datacenter</h1></body></html>")

#backend of add section
def add(request):
    return HttpResponse("<html><body><h1>Add data here</h1></body></html>")

#backend of delete section
def delete(request):
    return HttpResponse("<html><body><h1>Delete data here</h1></body></html>")

#backend of viewdata section
def viewdata(request):
    return HttpResponse("<html><body><h1>view data here</h1></body></html>")
# Create your views here.
#request.user