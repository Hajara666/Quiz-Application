from fastapi import FastAPI,Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import sqlite3

conn = sqlite3.connect('databases/quizzes.db')
cur = conn.cursor()
#homepage
#create a table for listing the topics of quizzes step. 1
cur.execute("DROP TABLE IF EXISTS QuizTopics")
cur.execute("CREATE TABLE IF NOT EXISTS QuizTopics (QID INTEGER PRIMARY KEY, QuizName TEXT(25));")
rows_of_topics = [('General_Knowledge',),('Sports',),('Science',),('Films',),('Music',),('fortesting',)]
cur.executemany('INSERT INTO QuizTopics (QuizName) VALUES (?);', rows_of_topics)
conn.commit()

#fetching the rows of topics table and convert it into a list of rows
cur.execute('SELECT * FROM QuizTopics;')
rows = cur.fetchall()
topics_list = []
for row in rows:
    topics_list.append((row))

app = FastAPI()
templates = Jinja2Templates(directory="pages")
app.mount("/static",StaticFiles(directory="assets"),name="static")

#Step 1.request to display available topics for the quizzes
@app.get('/homepage',response_class=HTMLResponse)
async def list_the_topics(request: Request):
    return templates.TemplateResponse("topics_list.html"
                                      , {"request": request, "topics_list": topics_list})

'''Creating tables for the quizzez'''
#create a table for General Knowledge quiz
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

#create a table for Sports quiz
cur.execute('DROP TABLE IF EXISTS Sports')
cur.execute('CREATE TABLE Sports (QuizID INTEGER PRIMARY KEY AUTOINCREMENT, Question TEXT(100) NOT NULL,Choice1 TEXT(30),Choice2 TEXT(30),Choice3 TEXT(30),Choice4 TEXT(30),Answer TEXT(30));')
rows_of_quesions = [
                    (1,' After how many Year’s FIFA World Cup is held?',
                     '2 Years','3 years','4 years','every year','4 years'),
                    (2,'Which Country won the first FIFA World Cup in the year 1930','Argentina','Uruguay','Italy','Brazil','Uruguay'),
                    (3,'Which Female has the Most Olympic Gold Medals in Olympic History?','Birgit Fischer','Marit Bjørgen','Larisa Latynina','Jenny Thompson','Larisa Latynina'),
                    (4,'What is the 100m World Record of Usain Bolt?','14.35 Sec','9.58 Sec','9.05 Sec','10.12 Sec','9.58 Sec'),
                    (5,'Who won the FIFA World Cup in 2018?','France','Germany','Portugal','Uraguay','France')
                    ]
cur.executemany('INSERT INTO Sports(QuizID,Question,Choice1,Choice2,Choice3,Choice4,Answer) VALUES(?,?,?,?,?,?,?);',rows_of_quesions)
conn.commit()

#create a table for Science quiz
cur.execute('DROP TABLE IF EXISTS Science')
cur.execute('CREATE TABLE Science (QuizID INTEGER PRIMARY KEY AUTOINCREMENT, Question TEXT(100) NOT NULL,Choice1 TEXT(30),Choice2 TEXT(30),Choice3 TEXT(30),Choice4 TEXT(30),Answer TEXT(30));')
rows_of_quesions = [
                    (1,'What is the normal pH level of the human blood??',
                     '7.40','6.0','13.5','10.3','7.40'),
                    (2,'At what temperature Celsius and Fahrenheit equal?','-32','-38','-40','-36','-40'),
                    (3,'Tinnitus problem is related to','Eye','Ear','Nose','Throat','Ear'),
                    (4,'What is the most deadly infectious disease in America?','Hepatitis B','Hepatitis C','Ebola','None','Hepatitis B'),
                    (5,'What is the medical term for low blood sugar?','Myocardial','Syncope','Hypoglycemia','Hyperglycaemia','Hypoglycemia')
                    ]
cur.executemany('INSERT INTO Science(QuizID,Question,Choice1,Choice2,Choice3,Choice4,Answer) VALUES(?,?,?,?,?,?,?);',rows_of_quesions)
conn.commit()
#create a table for Films quiz
cur.execute('DROP TABLE IF EXISTS Films')
cur.execute('CREATE TABLE Films (QuizID INTEGER PRIMARY KEY AUTOINCREMENT, Question TEXT(100) NOT NULL,Choice1 TEXT(30),Choice2 TEXT(30),Choice3 TEXT(30),Choice4 TEXT(30),Answer TEXT(30));')
rows_of_quesions = [
                    (1,' Which of these is NOT a real job title that appears in movie credits?',
                     'Gaffer','Best boy','Splicer','Key grip','Splicer'),
                    (2,' What was the first movie in the Marvel Cinematic Universe?','Spider-Man','Batman','The Avengers','Iron man','Iron man'),
                    (3,' Which of these movies was NOT directed by M. Night Shyamalan?','The Ring','Signs','The Sixth Sense','Glass','The Ring'),
                    (4,'In the movie "Frozen", who is Olaf?','A knight','a snowman','A ghost','a reindeer','a snowman'),
                    (5,' For which of these movies did Leonardo DiCaprio win an Oscar for Best Actor?','Blood Diamond','The last king of Scotland','Titanic','The Revenant','The Revenant')
                    ]
cur.executemany('INSERT INTO Films(QuizID,Question,Choice1,Choice2,Choice3,Choice4,Answer) VALUES(?,?,?,?,?,?,?);',rows_of_quesions)
conn.commit()

#create a table for Music quiz
cur.execute('DROP TABLE IF EXISTS Music')
cur.execute('CREATE TABLE Music (QuizID INTEGER PRIMARY KEY AUTOINCREMENT, Question TEXT(100) NOT NULL,Choice1 TEXT(30),Choice2 TEXT(30),Choice3 TEXT(30),Choice4 TEXT(30),Answer TEXT(30));')
rows_of_quesions = [
                    (1,' To consider a band as a Big Band what is the minimum number of musicians to be needed?',
                     '11','21','12','10','10'),
                    (2,' Bjork was lead singer of what Icelandic band before pursuing a solo career?','Kukl','The Sugarcubes',' Cocteau Twins','The Elgar sisters','The Sugarcubes'),
                    (3,' In an Orchestra, which is the largest brass section instrument?','Trumpet','Tenor','French horns','Tuba','Tuba'),
                    (4,' Name the orchestral instrument that can play high note?','Viola','Piccolo','Violin',' Cellos','Violin'),
                    (5,'  The Clawhammer is a playing style associated with an instrument, what is it?','Ukulele','Banjo','Mandolin','Fiddle','Banjo')
                    ]
cur.executemany('INSERT INTO Music(QuizID,Question,Choice1,Choice2,Choice3,Choice4,Answer) VALUES(?,?,?,?,?,?,?);',rows_of_quesions)
conn.commit()
#Step 2. Showing the questions of the selected topic
@app.post('/quiz',response_class=HTMLResponse)
async def list_the_questions(request: Request,QuizID:int = Form(...)):
    query = "SELECT QuizName FROM QuizTopics WHERE QID=?"
    q = cur.execute(query, (QuizID,))
    row = q.fetchone()
    table_name = row[0]
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT Question,Choice1,Choice2,Choice3,Choice4 FROM {}'.format(table_name))
    r = c.fetchall()
    result = []
    for row in r:
        summary = dict(zip(row.keys(), row))
        result.append(summary)
    return templates.TemplateResponse("questions_list.html"
                                      , {"request": request,"result":result,"table_name":table_name})

# Step 3. Add a new quiz
@app.post('/checktopic',response_class=HTMLResponse)
async def check_the_topic(request: Request,Quizname:str = Form(...)):
    for item in topics_list:
        if Quizname in item:
            topic_already_added = True
            break
        else:
            topic_already_added = False
    if topic_already_added == True:
        return templates.TemplateResponse("check_topic.html",
                                              {"request": request})
    else:
        number = 1
        # add the new topic 'Quizname' into the table Quiztopics
        cur.execute('INSERT INTO QuizTopics (QuizName) VALUES (?);', (Quizname,))
        conn.commit()
        cur.execute('select * from QuizTopics;')
        records = cur.fetchall()
        for record in records:
            print(record)
        return templates.TemplateResponse("add_questions.html",
                                          {"request": request, "Quizname": Quizname,"number":number})

#b. Add questions to the newly added topic by creating a new table for the topic
@app.post('/questions',response_class=HTMLResponse)
async def add_the_questions(request: Request,number= Form(...),Quizname= Form(...),question= Form(...),option1=Form(...),option2=Form(...),option3=Form(...),option4=Form(...),answer=Form(...)):
    # create a new table for 'Quizname'
    cur.execute('DROP TABLE IF EXISTS {}'.format(Quizname))
    cur.execute('CREATE TABLE IF NOT EXISTS {} (QuizID PRIMARY KEY, Question TEXT(100) NOT NULL,Choice1 TEXT(30),Choice2 TEXT(30),Choice3 TEXT(30),Choice4 TEXT(30),Answer TEXT(30))'.format(Quizname))
    # insert the rows into the newly created table
    row_values = [question,option1,option2,option3,option4,answer]
    cur.execute('INSERT INTO {} (Question,Choice1,Choice2,Choice3,Choice4,Answer) VALUES (?,?,?,?,?,?);'.format(Quizname), row_values)
    conn.commit()
    number = int(number)
    if number < 5:
        number += 1
        return templates.TemplateResponse("add_questions.html",
                                          {"request": request, "Quizname": Quizname, "number": number})
    else:
        cur.execute('SELECT QuizID,Question,Choice1,Choice2,Choice3,Choice4 FROM {}'.format(Quizname))
        return templates.TemplateResponse("note.html",
                                          {"request": request, "Quizname": Quizname})


# Step 4. Remove a quiz
@app.get('/removequiz', response_class=HTMLResponse)
async def remove_the_topic(request: Request):
    return templates.TemplateResponse("remove_topic.html"
                                      , {"request": request, "topics_list": topics_list})
@app.post('/removequiz', response_class=HTMLResponse)
async def remove_the_topic(request: Request,QuizID:int = Form(...)):
    query = "SELECT QuizName FROM QuizTopics WHERE QID=?"
    q = cur.execute(query, (QuizID,))
    row = q.fetchone()
    table_name = row[0]
    print(table_name)
    #remove the topic from the QuizTopics table
    cur.execute('DELETE FROM QuizTopics WHERE QID=?', (QuizID,))
    conn.commit()
    #delete the table, which contains questions for the specific topic
    cur.execute('DROP table IF EXISTS {};'.format(table_name))
    conn.commit()
    cur.execute('select * from QuizTopics;')
    records = cur.fetchall()
    return templates.TemplateResponse("removed.html"
                                      , {"request": request,"Quizname":table_name})

# Step 5. Solve the quiz
@app.post('/play',response_class=HTMLResponse)
async def list_the_questions(request: Request,QuizID:int = Form(...)):
    query = "SELECT QuizName FROM QuizTopics WHERE QID=?"
    q = cur.execute(query, (QuizID,))
    row = q.fetchone()
    table_name = row[0]
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT QuizID,Question,Choice1,Choice2,Choice3,Choice4 FROM {}'.format(table_name))
    r = c.fetchall()
    result = []
    for row in r:
        summary = dict(zip(row.keys(), row))
        result.append(summary)
    return templates.TemplateResponse("play_quiz.html"
                                      , {"request": request,"result":result,"table_name":table_name})

#request to check the answers
@app.post('/checkanswers',response_class=HTMLResponse)
async def check_the_answers(request: Request,table_name=Form(...),answer1=Form(...),answer2=Form(...),answer3=Form(...),answer4=Form(...),answer5=Form(...)):
    points = 0
    answers = []
    for answer in [answer1,answer2,answer3,answer4,answer5]:
        if answer == '1':
            answer = 'Choice1'
        elif answer == '2':
            answer = 'Choice2'
        elif answer == '3':
            answer = 'Choice3'
        elif answer == '4':
            answer = 'Choice4'
        answers.append(answer)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT * FROM {}'.format(table_name))
    r = c.fetchall()
    results = []
    for row in r:
        summary = dict(zip(row.keys(), row))
        results.append(summary)
    for a,r in zip(answers,results):
        print(r[a])
        print(r['Answer'])
        if r[a] == r['Answer']:
            points += 1
    #conn.row_factory = sqlite3.Row
    a = conn.cursor()
    a.execute('SELECT Question,Answer FROM {};'.format(table_name))
    QnA = a.fetchall()
    QnA_table = []
    for row in QnA:
        summary = dict(zip(row.keys(), row))
        QnA_table.append(summary)
    return templates.TemplateResponse("result.html"
                                      , {"request": request, "table_name": table_name,"points":points,"QnA_table":QnA_table})


