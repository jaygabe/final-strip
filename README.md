# FinalStrip
## The Fencing Journal Project

### Overview

This project was created to allow fencers of all skill levels have an easy and quantifiable way to take notes and record bouts.


### The current goal of the MVP:

* Have a clean way to sign up and onto the platform
* record tournaments, events, bouts, and fencers
* link a fencer's profile to a usfa number
* A minimal dashboard to analyze opponents
* a minimal dashboard for a coach to analyze all their students
* stripe page to start a subscription


### Future features to include:

* fencing ELO
* ability to share bouts and profiles
* customize appearance to twitter and facebook
* ability to save and share video with coaches
* customize profiles
* blog to boost SEO
* home, contact, benefits, FAQ pages


### Far in the Future:
* a merch store
* better styling
* prizes for best results at tournaments


### Starting up the app

There are two ways to start the backend in its current form.  Either through `python manage.py runserver` from `finalstrip-django` or by running the command `docker compose -f local.yml up --build -d --remove-orphans` which will build a series of containers and launch the backend.  Once that is complete you then need to start up the react app separately in another terminal with `npm start` from within the `finalstrip-react` folder.


### Routes:

* All django api pages are through port 8000
* Mailhog runs on 8025
* Flower should be on 5555
* Nginx is on 8080
* React is on 3000

flower, nginx and mailhog require docker to be up and running


### django commands to know:

* `python manage.py makemigrations` creates files to update the database to changes in the models
* `python manage.py migrate` pushes the changes to the database
* `python manage.py runserver` runs the django web server
* `python manage.py createsuperuser` used to create a superuser that can log into the `localhost:8000/admin/` page and manually edit data without code.
* `python manage.py migrate --run-syncdb` sometimes the db does not migrate correctly and this command fixes that



