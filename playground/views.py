from django.shortcuts import render
from django.http import HttpResponse
from .models import Member, Role, Team


def home(request):
    return list(request)


def list(request):
    members = Member.objects.all

    context = {
        'members': members
    }
    return render(request, 'team_member_management_application/listmembers.html', context)


def add_form(request):
    if request.method == 'POST':

        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        role = request.POST.get('role')

        roles = Role.objects
        new_role = roles.filter(name = role)[:1].get()

        teams =  Team.objects
        new_team = teams.filter(id = 1)[:1].get()

        new_member = Member.objects.create(
        
            first_name=first_name,last_name=last_name,
                                   phone=phone,
                                   email=email,
                                   role=new_role,
                                   teammember=new_team
                                   )
       
        new_member.save()

        return list(request)
    elif request.method == 'GET':
        return render(request, 'team_member_management_application/addmember.html')

def edit_form(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        print(id)
        member = Member.objects.all().filter(id=id)[:1].get()
        print(member)
        context = {
            'member': member
        }
        return render(request, 'team_member_management_application/editmember.html', context)
    elif request.method == 'POST':
        id = request.POST.get('id')
        member = Member.objects.all().filter(id=id)[:1].get()

        if 'save_button' in request.POST:
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            role = request.POST.get('role')

            roles = Role.objects
            new_role = roles.filter(name = role)[:1].get()

            teams =  Team.objects

            print(member)
            member.first_name=first_name
            member.last_name=last_name
            member.email=email
            member.phone=phone
            member.role=new_role
            
            member.save()
        else:
            member.delete()
        return list(request)

