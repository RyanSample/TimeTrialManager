# TIMETRIAL Manager
TimeTrial Manager, or TTM for short, is a django application for managing time trials in the metro east region. Users will be able to signup for races and view results afterwards.

## Installation
*ToDo*

## Development Roadmap
Quick napkin level plan:
1. Work on Models
2. Add user auth
3. Rework frontend
4. Deploy initial app

## Development Commands
Migrations:
```
py manage.py makemigrations [name of app]
#optional
py manage.py sqlmigrate [name of app] [migration number] # displays the sql schema
py manage.py migrate
```