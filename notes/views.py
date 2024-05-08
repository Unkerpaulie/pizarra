from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Note
from projects.models import Project


@login_required
def home(req, proj_id):
    project = Project.objects.filter(created_by=req.user).get(pk=proj_id)
    notes = Note.objects.filter(project=project)
    context = {"notes": notes, "project": project}
    return render(req, "notes/home.html", context)

@login_required
def new_note(req, proj_id):
    project = Project.objects.filter(created_by=req.user).get(pk=proj_id)
    if req.method == "POST":
        title = req.POST.get("title", "")
        body = req.POST.get("body", "")
        if title:
            Note.objects.create(title=title, body=body, project=project, created_by=req.user)
            return redirect(f"/projects/{proj_id}/notes")

    context = {"project_name": project.name}
    return render(req, "notes/new.html", context)

@login_required
def delete(req, proj_id, note_id):
    if req.method == "POST":
        note = Project.objects.filter(created_by=req.user).get(pk=proj_id).notes.get(pk=note_id)
        note.delete()

        return redirect(f"/projects/{proj_id}/notes")

@login_required
def edit(req, proj_id, note_id):
    note = Project.objects.filter(created_by=req.user).get(pk=proj_id).notes.get(pk=note_id)

    if req.method == "POST":
        title = req.POST.get("title", "")
        body = req.POST.get("body", "")

        if title:
            note.title = title
            note.body = body
            note.save()
            return redirect(f"/projects/{proj_id}/notes")

    return redirect(f"/projects/{proj_id}")

