from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Project

# only accessible if logged in
@login_required
def home(req):
    project_list = Project.objects.filter(created_by=req.user)
    context = {"projects": project_list}
    return render(req, "projects/home.html", context)

@login_required
def new_project(req):
    if req.method == "POST":
        name = req.POST.get("name", "")
        description = req.POST.get("description", "")

        if name:
            Project.objects.create(name=name, description=description, created_by=req.user)
            # project.save()
            return redirect("/projects")

    return render(req, "projects/new.html")

@login_required
def details(req, pk):
    project = Project.objects.filter(created_by=req.user).get(pk=pk)
    tasks = project.tasks.all()
    note_count= project.notes.count()
    context = {"project": project, "tasks": tasks, "note_count": note_count}

    return render(req, "projects/detail.html", context)


@login_required
def edit(req, pk):
    project = Project.objects.filter(created_by=req.user).get(pk=pk)

    if req.method == "POST":
        name = req.POST.get("name", "")
        description = req.POST.get("description", "")

        if name:
            project.name = name
            project.description = description
            project.save()
            return redirect(f"/projects/{pk}")
    context = {"project": project}

    return render(req, "projects/edit.html", context)
 
@login_required
def delete(req, pk):
    if req.method == "POST":
        project = Project.objects.filter(created_by=req.user).get(pk=pk)
        project.delete()

        return redirect("/projects")


