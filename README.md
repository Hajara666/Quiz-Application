# Quiz-Application
Created some endpoints for a quiz application using FastAPI,jinja2,HTML templates and sqlite3<br>
The application is called main.py<br>

Main tasks are:
1. Display the categories
2. View a quiz for the selected category
3. Add a new category and questions
4. Delete a category and its questions
5. Solve a quiz and get points

Basic Requirements:

Python 3.9.4 (installed with updated pip)

fastapi --> pip install fastapi

uvicorn --> pip install uvicorn

jinja2 --> pip install jinja2

After all the pre-requisites are installed, use this command to run this application:<br>

<mark style="background-color: #FFFF00">uvicorn main:app --reload</mark>

Then, in browser, write: http://127.0.0.1:8000/homepage

To see docs, write: http://127.0.0.1:8000/docs