# Submission for Adeleke Awwal - Written in Python
## Section one
The number concatenation and string compression are very *self-explanatory*, that means I added comments so anybody can understand the program logic and flow.

## Section two
I wrote the program with the Django and Django Rest Framework to properly visualize the API endpoints.

### To start, clone Project files or use your project files

#### Make sure you have git installed
-> `git clone https://github.com/codemaestro02/skillsforge.git`
#### clone with SSH
-> `git clone git@github.com:codemaestro02/skillsforge.git`

#### Create Virtual environment
-> Windows
`py -m venv env`

-> Linux and Mac
`python3 -m venv env`

#### Activate environment
-> Windows
`.\env\Scripts\activate`

-> Linux and Mac
`source env/bin/activate`

#### Install Requirements
`pip install -r requirements.txt`

#### Create first user
`python manage.py createsuperuser`

#### Make sure the app is running properly
`python manage.py check`
`python manage.py runserver`

### The Postman Documentation details on how to access the endpoints my API accepts
```
Blog Post List

Endpoint: GET /api/posts/
Description: Get a list of all blog posts
Request Headers: Authorization: Token <token>
Response: 200 OK
Blog Post Detail

Endpoint: GET /api/posts/<int:pk>/
Description: Get the details of a specific blog post
Request Headers: Authorization: Token <token>
Response: 200 OK
Blog Post Create

Endpoint: POST /api/posts/
Description: Create a new blog post
Request Headers: Authorization: Token <token>
Request Body:
Copy code
{
  "title": "My First Post",
  "description": "This is my first post",
  "tags": ["nodejs", "express"],
  "body": "This is the content of my post"
}
Response: 201 Created
Blog Post Update

Endpoint: PUT /api/posts/<int:pk>/
Description: Update a specific blog post
Request Headers: Authorization: Token <token>
Request Body:
Copy code
{
  "title": "My Updated Post",
  "description": "This is my updated post",
  "tags": ["nodejs", "express"],
  "body": "This is the updated content of my post"
}
Response: 200 OK
Blog Post Delete

Endpoint: DELETE /api/posts/<int:pk>/
Description: Delete a specific blog post
Request Headers: Authorization: Token <token>
Response: 204 No Content
Blog Comment List

Endpoint: GET /api/posts/<int:pk>/comments/
Description: Get a list of all comments for a specific blog post
Request Headers: Authorization: Token <token>
Response: 200 OK
Blog Comment Detail

Endpoint: GET /api/posts/<int:pk>/comments/<int:comment_pk>/
Description: Get the details of a specific comment for a specific blog post
Request Headers: Authorization: Token <token>
Response: 200 OK
Blog Comment Create

Endpoint: POST /api/posts/<int:pk>/comments/
Description: Create a new comment for a specific blog post
Request Headers: Authorization: Token <token>
Request Body:
Copy code
{
  "content": "This is a comment"
}
Response: 201 Created
Blog Comment Update

Endpoint: PUT /api/posts/<int:pk>/comments/<int:comment_pk>/
Description: Update a specific comment for a specific blog post
Request Headers: Authorization: Token <token>
Request Body:
Copy code
{
  "content": "This is an updated comment"
}
Response: 200 OK
Blog Comment Delete

Endpoint: DELETE /api/posts/<int:pk>/comments/<int:comment_pk>/
Description: Delete a specific comment for a specific blog post
Request Headers: Authorization: Token <token>
Response: 204 No Content
Note: Replace <token> with the actual token obtained from the user login endpoint.
```
