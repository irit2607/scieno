from django.shortcuts import render, redirect
from django.http import HttpResponse
from core.models import Host, Participant, Contact
from core.forms import HostForm, ParticipantForm
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages


def about(request):
    template_name = "core/about.html"
    return render(request, template_name)


def projects(request):
    template_name = "core/projects.html"
    projects = Participant.objects.all()
    context = {"projects": projects}
    return render(request, template_name, context)


def contact(request):
    template_name = "core/contact.html"
    return render(request, template_name)


@csrf_exempt
def add_contact(request):
    if request.method == "POST":
        Full_Name = request.POST["name"]
        Email_Address = request.POST["email"]
        Message = request.POST["message"]
        Contact.objects.create(
            Full_Name=Full_Name,
            Email_Address=Email_Address,
            Message=Message,
        )
        messages.success(request, "Your message is successfully sent!")

    return redirect("contact")


def host(request):
    template_name = "core/host.html"
    form = HostForm()
    context = {"form": form}

    return render(request, template_name, context=context)


def add_host(request):
    username = request.user.get_username()
    if request.method == "POST":
        form = HostForm(request.POST)
        if form.is_valid():
            Your_Full_Name = form.cleaned_data.get("Your_Full_Name")
            Email_address = form.cleaned_data.get("Email_address")
            Organization_hosting_the_contest = form.cleaned_data.get(
                "Organization_hosting_the_contest"
            )
            Type_of_Organization = form.cleaned_data.get("Type_of_Organization")
            Designation = form.cleaned_data.get("Designation")
            Phone_no = form.cleaned_data.get("Phone_no")
            Purpose_of_Contest = form.cleaned_data.get("Purpose_of_Contest")
            Breif_detail_about_your_event = form.cleaned_data.get(
                "Breif_detail_about_your_event"
            )
            Theme_of_Project = form.cleaned_data.get("Theme_of_Project")
            Guidelines_for_submission = form.cleaned_data.get(
                "Guidelines_for_submission"
            )
            Eligibility_Criteria = form.cleaned_data.get("Eligibility_Creteria")
            Last_Submission_Date = form.cleaned_data.get("Last_Submission_Date")
            Host.objects.create(
                username=username,
                full_name=Your_Full_Name,
                email=Email_address,
                org=Organization_hosting_the_contest,
                type_org=Type_of_Organization,
                designation=Designation,
                phone=Phone_no,
                purpose=Purpose_of_Contest,
                detail=Breif_detail_about_your_event,
                theme=Theme_of_Project,
                guidelines=Guidelines_for_submission,
                elig_cri=Eligibility_Criteria,
                last_sub=Last_Submission_Date,
            )

    return redirect("/")


def host_dashboard(request, username):
    username = username
    host_obj = Host.objects.get(username=username)
    host_id = host_obj.id
    projects = Participant.objects.all().filter(host_id=host_id)
    template_name = "core/dashboard.html"
    context = {"host_obj": host_obj, "projects": projects}
    return render(request, template_name, context)


def delete_host(request):
    username = request.user.get_username()
    host_obj = Host.objects.get(username=username)
    host_obj.delete()

    return redirect("/")


@csrf_exempt
def add_participant(request, host_id):
    host_id = host_id
    username = request.user.get_username()
    if request.method == "POST":
        School_Name = request.POST["school_name"]
        School_Phone_no = request.POST["school_phone"]
        School_Email_address = request.POST["school_email"]
        School_Address = request.POST["school_address"]
        State = request.POST["school_state"]
        Student_Name = request.POST["name"]
        Contact_no = request.POST["phone"]
        Email_address = request.POST["email"]
        House_Address = request.POST["address"]
        Gender = request.POST["gender"]
        Title_of_your_project = request.POST["title"]
        Question_or_Problem = request.POST["question"]
        Hypothesis_or_possible_solution = request.POST["solution"]
        Materials_needed = request.POST["material"]
        Results = request.POST["results"]
        Image_of_Project = request.POST["image"]
        Link_of_your_project = request.POST["link"]
        Participant.objects.create(
            username=username,
            School_Name=School_Name,
            School_Phone_no=School_Phone_no,
            School_Email_address=School_Email_address,
            School_Address=School_Address,
            State=State,
            Student_Name=Student_Name,
            Contact_no=Contact_no,
            Email_address=Email_address,
            House_Address=House_Address,
            Gender=Gender,
            Title_of_your_project=Title_of_your_project,
            Question_or_Problem=Question_or_Problem,
            Hypothesis_or_possible_solution=Hypothesis_or_possible_solution,
            Materials_needed=Materials_needed,
            Results=Results,
            Image_of_Project=Image_of_Project,
            Link_of_your_project=Link_of_your_project,
            host_id=host_id,
        )

    return redirect("projects")


def detail(request):
    template_name = "core/detail.html"
    hosts = Host.objects.all()
    context = {"hosts": hosts}
    return render(request, template_name, context)


def applyto(request, host_id):
    host_id = host_id
    template_name = "core/applyto.html"
    host_obj = Host.objects.get(pk=host_id)
    context = {"host_obj": host_obj, "host_id": host_id}
    return render(request, template_name, context)


def participant(request, host_id):
    host_id = host_id
    template_name = "core/participant.html"
    form = ParticipantForm()
    context = {"form": form, "host_id": host_id}

    return render(request, template_name, context=context)


def project_details(request, project_id):
    template_name = "core/project_details.html"
    project_obj = Participant.objects.get(pk=project_id)
    context = {"project_obj": project_obj}
    return render(request, template_name, context)


def project_view(request, project_id):
    template_name = "core/project_view.html"
    project_obj = Participant.objects.get(pk=project_id)
    context = {"project_obj": project_obj}
    return render(request, template_name, context)
