from django.shortcuts import render,HttpResponse
from GitHubRelationship.models import *
import json
# Create your views here.
def home(request):
    return render(request, 'index.html')

def follow(request):
    return render(request, 'follow.html')

def graph_follow(request):
    username = request.GET.get('username', '')
    result = "false"
    user_id = -2
    user_login = ""
    user_list = []
    edge_list = []
    if username.isdigit():
        userid = int(username)
        user = follow_nodes.objects.filter(id=userid)
        if len(user) == 0:
            us = users.objects.filter(id=userid)
            if len(us) == 0:
                result = "true"
            else:
                result = "false"
                us_dict={"id": us[0].id, "label": us[0].login,"modularity":-1,"degree":0,
                               "inDegree":0,"outDegree":0}
                user_list.append(us_dict)
                user_id = us[0].id
                user_login = us[0].login
        else:
            result = "false"
            user_id = user[0].id
            user_login = user[0].label
            modu = user[0].modularity
            userlist = follow_nodes.objects.filter(modularity=modu)
            list_dict = {}
            for item in userlist:
                user_dict={"id": item.id, "label": item.label,"modularity":item.modularity,"degree":item.degree,
                               "inDegree":item.inDegree,"outDegree":item.outDegree}
                user_list.append(user_dict)
                list_dict[item.id] = len(user_list)-1
            id_list = userlist.values("id")
            edgelist = follow_edges.objects.filter(id__in=id_list)
            for item in edgelist:
                edge_dict = {"target":list_dict[item.target],"source":list_dict[item.source],"type":"follow"}
                edge_list.append(edge_dict)
    else:
        user = follow_nodes.objects.filter(label=username)
        if len(user) == 0:
            us = users.objects.filter(login=username)
            if len(us) == 0:
                result = "true"
            else:
                result = "false"
                us_dict = {"id": us[0].id, "label": us[0].login, "modularity": -1, "degree": 0,
                               "inDegree": 0, "outDegree": 0}
                user_list.append(us_dict)
                user_id = us[0].id
                user_login = us[0].login
        else:
            result = "false"
            user_id = user[0].id
            user_login = user[0].label
            modu = user[0].modularity
            userlist = follow_nodes.objects.filter(modularity=modu)
            list_dict = {}
            for item in userlist:
                user_dict = {"id": item.id, "label": item.label, "modularity": item.modularity,
                                 "degree": item.degree,
                                 "inDegree": item.inDegree, "outDegree": item.outDegree}
                user_list.append(user_dict)
                list_dict[item.id] = len(user_list) - 1
            id_list = userlist.values("id")
            edgelist = follow_edges.objects.filter(id__in=id_list)
            for item in edgelist:
                edge_dict = {"target":list_dict[item.target],"source":list_dict[item.source]}
                edge_list.append(edge_dict)
    return render(request, 'follow-graph.html', {'user_id':user_id,
                                              'user_login':user_login,
                                              'user_list': list(user_list),
                                              'edge_list': list(edge_list),
                                              'result': result})


def collaborate(request):
    return render(request,'collaboration.html')

def graph_project_all(request):
    pro = request.GET.get('project')
    coll_user_list = []
    coll_edge_list = []
    comm_user_list = []
    comm_edge_list = []
    coll_userlist = Collaborate_nodes.objects.filter(project=pro)
    coll_edgelist = Collaborate_edges.objects.filter(project=pro)
    comm_userlist = Commit_nodes.objects.filter(project=pro)
    comm_edgelist = Commit_edges.objects.filter(project=pro)
    list_dict = {}
    for item in coll_userlist:
        coll_user_dict = {"id": item.uid, "label": item.label, "modularity": item.modularity, "degree": item.degree,
                          "inDegree": item.inDegree, "outDegree": item.outDegree}
        coll_user_list.append(coll_user_dict)
        list_dict[item.uid] = len(coll_user_list) - 1
    for item in coll_edgelist:
        coll_edge_dict = {"target": list_dict[item.target], "source": list_dict[item.source]}
        coll_edge_list.append(coll_edge_dict)
    for item in comm_userlist:
        comm_user_dict = {"id": item.uid, "label": item.label, "modularity": item.modularity,
                     "degree": item.degree,
                     "inDegree": item.inDegree, "outDegree": item.outDegree}
        comm_user_list.append(comm_user_dict)
        if item.uid not in list_dict:
            coll_user_list.append(comm_user_dict)
            list_dict[item.uid] = len(coll_user_list) - 1
    for item in comm_edgelist:
        comm_edge_dict = {"target": list_dict[item.target], "source": list_dict[item.source]}
        comm_edge_list.append(comm_edge_dict)
    return render(request,'project-all.html',{'user_list': list(coll_user_list),
                                             'edge_list':list(coll_edge_list),
                                              'coll_edge_list': list(coll_edge_list),
                                              'comm_edge_list': list(comm_edge_list),
                                             })

def project(request):
    pro = request.GET.get('project')
    return render(request,'project.html',{'project':pro})


def graph_project(request):
    pro = request.GET.get('project')
    username = request.GET.get('username')
    result_1 = "false"
    result_2 = "false"
    coll_user_list = []
    coll_edge_list = []
    comm_user_list = []
    comm_edge_list = []
    list_dict = {}
    if username.isdigit():
        userid = int(username)
        user = []
        user = Collaborate_nodes.objects.filter(uid=userid,project=pro)
        if len(user) == 0:
            result_1 = "true"
        else:
            result_1 = "false"
            modu = user[0].modularity
            userlist = []
            userlist = Collaborate_nodes.objects.filter(modularity=modu,project=pro)

            for item in userlist:
                user_dict = {"id": item.uid, "label": item.label, "modularity": item.modularity,
                                 "degree": item.degree,
                                 "inDegree": item.inDegree, "outDegree": item.outDegree}
                coll_user_list.append(user_dict)
                list_dict[item.uid] = len(coll_user_list) - 1
            id_list = userlist.values("uid")
            edgelist = []
            edgelist = Collaborate_edges.objects.filter(target__in=id_list,source__in=id_list,project=pro)
            for item in edgelist:
                edge_dict = {"target": list_dict[item.target], "source": list_dict[item.source]}
                coll_edge_list.append(edge_dict)

        userid = int(username)
        user = []
        user = Commit_nodes.objects.filter(uid=userid,project=pro)
        if len(user) == 0:
            result_2 = "true"
        else:
            result_2 = "false"
            modu = user[0].modularity
            userlist = []
            userlist = Commit_nodes.objects.filter(modularity=modu,project=pro)
            for item in userlist:
                user_dict = {"id": item.uid, "label": item.label, "modularity": item.modularity,
                                 "degree": item.degree,
                                 "inDegree": item.inDegree, "outDegree": item.outDegree}
                comm_user_list.append(user_dict)
                if item.uid not in list_dict:
                    coll_user_list.append(user_dict)
                    list_dict[item.uid] = len(coll_user_list) - 1
            id_list = userlist.values("uid")
            edgelist = []
            edgelist = Commit_edges.objects.filter(target__in=id_list,source__in=id_list,project=pro)
            for item in edgelist:
                edge_dict = {"target": list_dict[item.target], "source": list_dict[item.source]}
                comm_edge_list.append(edge_dict)
    else:
        user = []
        user = Collaborate_nodes.objects.filter(label=username,project=pro)
        if len(user) == 0:
            result_1 = "true"
        else:
            result_1 = "false"
            modu = user[0].modularity
            userlist = []
            userlist = Collaborate_nodes.objects.filter(modularity=modu,project=pro)
            list_dict = {}
            for item in userlist:
                user_dict = {"id": item.uid, "label": item.label, "modularity": item.modularity,
                                 "degree": item.degree,
                                 "inDegree": item.inDegree, "outDegree": item.outDegree}
                coll_user_list.append(user_dict)
                list_dict[item.uid] = len(coll_user_list) - 1
            id_list = userlist.values("uid")
            edgelist = []
            edgelist = Collaborate_edges.objects.filter(target__in=id_list,source__in=id_list,project=pro)
            for item in edgelist:
                edge_dict = {"target": list_dict[item.target], "source": list_dict[item.source]}
                coll_edge_list.append(edge_dict)

        user = []
        user = Commit_nodes.objects.filter(label=username,project=pro)
        if len(user) == 0:
            result_2 = "true"
        else:
            result_2 = "false"
            modu = user[0].modularity
            userlist = []
            userlist = Commit_nodes.objects.filter(modularity=modu,project=pro)
            for item in userlist:
                user_dict = {"id": item.uid, "label": item.label, "modularity": item.modularity,
                                 "degree": item.degree,
                                 "inDegree": item.inDegree, "outDegree": item.outDegree}
                comm_user_list.append(user_dict)
                if item.uid not in list_dict:
                    coll_user_list.append(user_dict)
                    list_dict[item.uid] = len(coll_user_list) - 1
            id_list = userlist.values("uid")
            edgelist = []
            edgelist = Commit_edges.objects.filter(target__in=id_list,source__in=id_list,project=pro)
            for item in edgelist:
                edge_dict = {"target": list_dict[item.target], "source": list_dict[item.source]}
                comm_edge_list.append(edge_dict)
    return render(request, 'project-graph.html', {'project': pro,
                                            'result_1': result_1,
                                            'result_2': result_2,
                                            'user_list': list(coll_user_list),
                                            'comm_user_list': list(comm_user_list),
                                            'coll_edge_list': list(coll_edge_list),
                                            'comm_edge_list': list(comm_edge_list),
                                            })
