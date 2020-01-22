## Scholarship management System 

- Scholarship management system allows students to apply for a scholarship and staff to approve and a sponsor to sponsor the application

### Required Features
- Users can create an account and log in.
- an Applicant can apply for a scholarship
- A Staff can approve a scholarship
- A sponsor can sponsor a scholarship application.



## Prerequisite

- [Python3.6](https://www.python.org/downloads/release/python-365/)
- [Virtual Environment](https://virtualenv.pypa.io/en/stable/installation/)
- [Django](https://www.djangoproject.com/)
- [Django-Rest Framework](https://www.django-rest-framework.org/)
- [Heroku](https://dashboard.heroku.com/)

## Technologies & Languages


**Version control (Git)** [https://git-scm.com/](url)

# Installation and Setup

Clone the repository below

```
git clone https://github.com/kelvinndmo/send.git
```

### Create and activate a virtual environment

    virtualenv env --python=python3.6

    source env/bin/activate

### Install required Dependencies

    pip install -r requirements.txt

## Running the application

```bash
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```


### Open postman and use the below endpoints.


## Endpoints Available

| Method | Endpoint                        | Description                           | Roles         |
| ------ | ------------------------------- | ------------------------------------- | ------------  |
| POST   | /auth/signup                    | sign up a user                        | users         |
| POST   | /auth/login                     | post a parcel order                   | users         |
| POST   |/scholarships/                   | Apply for a scholarship               | Applicant     |
| GET    | /scholarships/                  | get scholarships                      | All Users     |
| PUT    | /scholarships/sponsor/<sch:id>  | sponsor a scholarship                 | Sponsor       |
| PUT    | /scholarships/approve/<sch:id>  | sponsor a scholarship                 | Staff         |

## Fields:
```
## scholarship
### POST - /scholarships/
-    birth_certificate: File
    national_id: File,
    adress: text,
    phone: text
    school_name:text
    school_adress:text
    academic_level:text
    year_of_completion:text
    is_approved: bolean - default false
    recommendation_letter:File
    sponsor_reason
```

```
## scholarship
### PUT - /scholarships/sponsor/1/
- Only for sponsors,you pass a boolean field of whether to sponsor or not
-  sponsor:boolean default false
```

```
## scholarship
### PUT - /scholarships/approve/1/
- Only for staff,you pass a boolean field of whether to aprove or not
-  is_approved:boolean
```

### Testing

### Testing

    nosetests

    - Testing with coverage

    nosetests --with-coverage --cover-package=app

### Author

Kelvin Onkundi Ndemo

## License

MIT
