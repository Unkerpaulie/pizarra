# Pizarra Project Management

Based on the tutorial at https://youtu.be/m3nYd_IFZuU?si=HiIksNE95dwDO7CG

## Clone this repo

`git clone https://github.com/Unkerpaulie/pizarra.git`

## setup

`pip install django`

In the project directory

`python manage.py migrate`

`python manage.py runserver`

By default, the server address is http://127.0.0.1:8000/

## Using the app

Create an account by signing up

Log in with your credentials

You can now create projects

Each project can have an associated list of tasks, and a list of related notes

You can create, edit and delete projects, notes and notes

If you delete a project, all associated tasks and notes will also be deleted

## Things to add

1. Implement "Mark as done" functionality for projects, which also sets all related tasks to completed
2. Separate completed projects from ongoing projects as separate pages
3. Sort tasks by due date, also push completed tasks to the bottom of the list and give a faded appearance
4. Create search function for notes throughout the app
5. Implement log out functionality so multiple users can use the app
6. Remove "My Account" button since this isn't going to be implemented
7. Implement "Add Reminder" on tasks
8. Create a new view with all upcoming tasks across all projects by due date