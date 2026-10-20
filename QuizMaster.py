import pgzrun
import time

WIDTH = 500
HEIGHT = 350
Game_over=False
t = 10
g = False
questionfile = "Quiz Master/questions.txt"
questions= []
score = 0
# Rectangle definitions
question_box = Rect((20, 60), (370, 75))
marqueue = Rect((10,15),(380,40))
answer_box1 = Rect((20, 140), (170, 75))
answer_box2 = Rect((215, 140), (170, 75))
answer_box3 = Rect((20, 230), (170, 75))
answer_box4 = Rect((215, 230), (170, 75))
timerbox = Rect((415, 60), (70, 75))
skip_box = Rect((415, 140), (70, 165))
def ReadFile():
    queuefile = open(questionfile,"r")
    for q in queuefile:
        questions.append(q)
    queuefile.close()
    print(questions)
ReadFile()
def ReadQuestion():
    return questions.pop(0).split(",")
questions1 = ReadQuestion()
def MoveMarqueue():
    marqueue.x -= 2
    if marqueue.right <=0:
        marqueue.left = 750
def GameOver():
    global g
    g = True
    print("GameOver")
def on_mouse_down(pos):
    global t, questions1, questions, score,g
    index = 1
    for box in [answer_box1, answer_box2, answer_box3, answer_box4]:
        if box.collidepoint(pos):
            if index == int(questions1[5]):
                score += 1
                if questions:
                   questions1 = ReadQuestion()
                   t = 10
                else:
                    GameOver()

            else:
                if questions:
                    questions1 = ReadQuestion()
                    t = 10
        index+=1
    if skip_box.collidepoint(pos):
        if questions:
            questions1 = ReadQuestion()
            t = 10
        else:
            GameOver()           
def draw():
    global g
    if g:
        screen.fill("black")
        screen.draw.text(f"Score is {score}/10 ",(180,200),color = "white")
    else:

        # Title
        screen.draw.filled_rect(marqueue,"black")
        screen.draw.textbox("Welcome To Quiz Master...",marqueue,color="white")

        # Question box
        screen.draw.filled_rect(question_box, "darkblue")
        screen.draw.textbox(questions1[0] ,question_box,color="white")

        # Answer boxes
        index = 1
        for box in [answer_box1, answer_box2, answer_box3, answer_box4]:
            screen.draw.filled_rect(box, "orange")
            screen.draw.textbox(questions1[index],box,color="black")
            index+=1

        # Score box
        screen.draw.filled_rect(timerbox, "yellow")
        #timer
        screen.draw.textbox(str(t),timerbox,color="black")

        # Skip box
        screen.draw.filled_rect(skip_box, "green")
        screen.draw.text("Skip",center=skip_box.center,color="black",fontsize=40,angle=90)
def update():
    MoveMarqueue()
def timer():
    global t
    if t >0:
        t -= 1
    if t == 0:
        GameOver()

clock.schedule_interval(timer, 1.0)
pgzrun.go()