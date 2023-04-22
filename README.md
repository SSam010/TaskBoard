# Project Summary

This project implements a RESTful API to manage a personal task list.

# Setup and Launch

The application supports deployment in Docker. To launch the application, use the command `docker compose up`. By default, the application is accessible at http://localhost:8000/.

# Management and Functionality

A superuser is pre-created in the application. Login credentials are as follows: username: `root`, password: `1234`.

To create new users, use the built-in admin panel at http://localhost:8000/admin/ and navigate to the "Users" table.

To use this service via the RESTful API, you must be an authorized user.

# Authorization

To log in to the application, you can either:

Go through the authorization process via the graphical interface at http://127.0.0.1:8000/api/v1/auth/login/
Provide login information in the request body. For example, via Postman, select Basic Auth in the Authorization tab and provide your login information.

# API Endpoints

The following API endpoints are available:

### Retrieve all tasks

- URL: `/api/v1/`
- Method: GET
- Permissions: All authorized users
- Description: Retrieve all task records.

### Retrieve a single task

- URL: `/api/v1/<id>/`
- Method: GET
- Permissions: All authorized users
- Description: Retrieve a single task record by its ID.
### Create a new task
- URL: `/api/v1/create/`
- Method: POST
- Permissions: All authorized users
- Required Parameters: `title`, `description`, `deadline`
- Optional Parameters: `is_done` (default is `False`)
- Description: Create a new task record.
### Update an existing task
- URL: `/api/v1/update/<id>/`
- Method: POST
- Permissions: Admins or task owner
- Description: Update an existing task record by its ID.
### Delete a task
- URL: `/api/v1/delete/<id>/`
- Method: POST
- Permissions: Admins or task owner
- Description: Delete a task record by its ID.
