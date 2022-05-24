from fastapi import FastAPI,Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import sqlite3
from psycopg2 import sql

conn = sqlite3.connect('databases/quizzes.db')
cur = conn.cursor()
#create a table for listing the topics of quizzes
cur.execute("DROP TABLE IF EXISTS QuizTopics")
cur.execute("CREATE TABLE QuizTopics (QID INTEGER PRIMARY KEY, QuizName TEXT(25));")
rows_of_topics = [(1,'General_Knowledge'),(2,'Sports'),(3,'Science'),(4,'Films'),(5,'Music')]
cur.executemany('INSERT INTO QuizTopics(QID,QuizName) VALUES (?,?);', rows_of_topics)
conn.commit()

app = FastAPI()
templates = Jinja2Templates(directory="pages")
app.mount("/static",StaticFiles(directory="assets"),name="static")
#1.request to display available topics for the quizzes
@app.get('/topics',response_class=HTMLResponse)
async def list_the_topics(request: Request):
    cur.execute('SELECT * FROM QuizTopics;')
    rows = cur.fetchall()
    topics_list = []
    for row in rows:
        topics_list.append((row))
    return templates.TemplateResponse("topics_list.html"
                                      , {"request": request, "topics_list": topics_list})

#create a table for General Knowledge quiz questions
cur.execute('DROP TABLE IF EXISTS General_Knowledge')
cur.execute('CREATE TABLE General_Knowledge (QuizID INTEGER PRIMARY KEY AUTOINCREMENT, Question TEXT(100) NOT NULL,Choice1 TEXT(30),Choice2 TEXT(30),Choice3 TEXT(30),Choice4 TEXT(30),Answer TEXT(30));')
rows_of_quesions = [
                    (1,' What is the longest that an elephant has ever lived? (That we know of)',
                     '17 years','49 years','86 years','142 years','86 years'),
                    (2,'How many rings are on the Olympic flag?','None','4','5','7','5'),
                    (3,'What is a tarsier?','A bird','A lizard','A primate','None','A primate'),
                    (4,'In darts, what is the most points you can score with a single throw?','20','50','60','100','60'),
                    (5,'Which of these animals does NOT appear in the Chinese zodiac?','Bear','Dog','Dragon','Rabbit','Bear')
                    ]
cur.executemany('INSERT INTO General_Knowledge(QuizID,Question,Choice1,Choice2,Choice3,Choice4,Answer) VALUES(?,?,?,?,?,?,?);',rows_of_quesions)
conn.commit()

conn.row_factory = sqlite3.Row
c = conn.cursor()
c.execute('Select * from General_Knowledge;')
r = c.fetchone()
print(r[2])
print(r.keys())
print(r['Question'])
for member in r:
    print(member)
# def dict_factory(cur, row):
#     d = {}
#     for idx, col in enumerate(cur.description):
#         d[col[0]] = row[idx]
#     return d
#
# conn.row_factory = dict_factory
# cur = conn.cursor()
# cur.execute("select 1 as a")
# print(cur.fetchone()["a"])
# rows = cur.fetchall()
# questions_list = []
# for row in rows:
#     questions_list.extend([str(row[0]),row[1],row[2],row[3],row[4],row[5]])
# print(questions_list)
#2.request to display quiz details
@app.get('/quiz',response_class=HTMLResponse)
async def list_the_quistions(request: Request,QuizID = Form(...)):
    table_name = cur.execute("SELECT QuizName FROM QuizTopics WHERE QID = QuizID;")
    cur.execute(sql.SQL("Select * from {};").format(sql.Identifier(table_name)))
    rows = cur.fetchall()
    questions_list = []
    for row in rows:
        questions_list.extend([str(row[0]),row[1],row[2],row[3],row[4],row[5]])
    return templates.TemplateResponse("questions_list.html"
                                      , {"request": request, "QuizID":QuizID,"questions_list": questions_list})