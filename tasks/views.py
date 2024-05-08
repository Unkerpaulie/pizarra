from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from projects.models import Project

@login_required
def new_task(req, proj_id):
    project = Project.objects.filter(created_by=req.user).get(pk=proj_id)
    if req.method == "POST":
        name = req.POST.get("name", "")
        description = req.POST.get("description", "")
        due_date = req.POST.get("due_date", "") if req.POST.get("due_date", "") else None
        if name:
            Task.objects.create(name=name, description=description, project=project, due_date=due_date, created_by=req.user)
            return redirect(f"/projects/{proj_id}/")

    context = {"projecte": project}
    return render(req, "tasks/new.html", context)

@login_required
def delete(req, proj_id, task_id):
    if req.method == "POST":
        task = Project.objects.filter(created_by=req.user).get(pk=proj_id).tasks.get(pk=task_id)
        task.delete()

        return redirect(f"/projects/{proj_id}/")

@login_required
def edit(req, proj_id, task_id):
    task = Project.objects.filter(created_by=req.user).get(pk=proj_id).tasks.get(pk=task_id)

    if req.method == "POST":
        name = req.POST.get("name", "")
        description = req.POST.get("description", "")
        due_date = req.POST.get("due_date", "")

        if name:
            task.name = name
            task.description = description
            task.due_date = due_date if due_date else None
            task.save()
            return redirect(f"/projects/{proj_id}")

    return redirect(f"/projects/{proj_id}")

@login_required
def done(req, proj_id, task_id):
    task = Project.objects.filter(created_by=req.user).get(pk=proj_id).tasks.get(pk=task_id)

    if req.method == "POST":
        task.done = not task.done
        task.save()
        return redirect(f"/projects/{proj_id}")

    return redirect(f"/projects/{proj_id}")

