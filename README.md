# IReporter-V2

![license](https://img.shields.io/github/license/mashape/apistatus.svg)
<<<<<<< HEAD
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/52f19a52e9ba44a2974515c87c29f0dd)](https://app.codacy.com/app/markmumo/IReporter-V2?utm_source=github.com&utm_medium=referral&utm_content=markmumo/IReporter-V2&utm_campaign=Badge_Grade_Dashboard)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/24f3c19789c64cea904d6ac5155119f4)](https://app.codacy.com/app/markmumo/IReporter-API?utm_source=github.com&utm_medium=referral&utm_content=markmumo/IReporter-API&utm_campaign=Badge_Grade_Dashboard)
=======
>>>>>>> [Chore #162412710] updated badges on  README.md
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)
[![Build Status](https://travis-ci.org/markmumo/IReporter-V2.svg?branch=develop)](https://travis-ci.org/markmumo/IReporter-V2)
[![codecov](https://codecov.io/gh/markmumo/IReporter-API/branch/develop/graph/badge.svg)](https://codecov.io/gh/markmumo/IReporter-API)

# IReporter-V2

iReporter is an app enables citizen to report any form of corruption.

## How it Works

-A user registers for an account

-A user then logs in

-A logged in user can report a red flag or request for a government intervention

-An admin then reviews the incident and can mark it as under investigation, resolved or rejected

-A user will then get notified with an sms or email regarding the marked status of the incident

## Prerequisite

- [Python3.6](https://www.python.org/downloads/release/python-365/)
- [Virtual Environment](https://virtualenv.pypa.io/en/stable/installation/)

# Installation and Setup

Clone the repository below

```
git clone git@github.com:markmumo/IReporter-V2.git
```

### Create and activate a virtual environment

    virtualenv env --python=python3.6

    source env/bin/activate

### Install required Dependencies

    pip install -r requirements.txt

## Running the application

```bash
$ export FLASK_APP=run.py

$ export MODE=development

$ flask run
```

## Endpoints Available

| Method | Endpoint                  | Description                            | Roles       |
| ------ | ------------------------- | -------------------------------------- | ----------- |
| POST   | /api/v2/auth/Sign_up      | register a user.                       | User        |
| POST   | /api/v2/auth/Sign_in      | login a user.                          | User        |
| GET    | /api/v2/users             | get all users.                         | Admin       |
| POST   | /api/v2/incident          | create an incident record.             | User        |
| GET    | /api/v2/incident          | Get all incident records.              | Admin/users |
| GET    | /api/v2/incident/<int:id> | Get a specific incident.               | Admin/users |
| PUT    | /api/v2/incident/<int:id> | Edit a specific incident field by. id. | Admin/users |
| DELETE | /api/v2/incident/<int:id> | Delete a specific incident by id.      | Admin/users |

### Testing

nosetests

- Testing with coverage

nosetests --with-coverage --cover-package=app

### Author

Mark Mumo
