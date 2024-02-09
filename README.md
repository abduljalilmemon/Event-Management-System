# Event Management System

Description:

This Django-based Event Management System empowers users to effortlessly organize and participate in events. The platform features a user-friendly interface allowing users to seamlessly navigate through various events, register, and access detailed information.

## Key Features:

- User-Friendly Homepage: The homepage provides a comprehensive view of all events, enabling users to browse and search for specific events based on their preferences.
- Detailed Event View: Users can access in-depth event details by clicking on the respective event, facilitating informed decisions on participation.
- Event Registration: Seamless event registration functionality allows users to register for events they wish to attend, enhancing user engagement and event management.
- Staff Management Interface: Staff members have exclusive access to create new events individually or import events via CSV in the prescribed format, streamlining event management tasks.
- This Event Management System offers a holistic solution for both event organizers and participants, fostering a seamless and efficient event management experience.

## Installation

Python and Django need to be installed

```bash
pip install django
```

## Usage

Go to the College-ERP folder and run

```bash
python manage.py runserver
```

Then go to the browser and enter the url **http://127.0.0.1:8000/**

Use **Events.csv** for importing events

## Login

The login page is common for staff.  
The username is their name and password for everyone is 'admin12345'.  

Example usernames:  
- 'abdul'
- 'haseeb'

You can access the django admin page at **http://127.0.0.1:8000/admin** and login with username 'admin' and the above password.

Also a new admin user can be created using

```bash
python manage.py createsuperuser
