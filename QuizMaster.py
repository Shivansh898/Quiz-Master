import pgzrun
import time

WIDTH = 500
HEIGHT = 350
Game_over=False
t = 10
questionfile = "Quiz Master/questions.txt"
questions= []
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
def MoveMarqueue():
    marqueue.x -= 2
    if marqueue.right <=0:
        marqueue.left = 750
def draw():
    screen.clear()
    screen.fill("black")

    # Title
    screen.draw.filled_rect(marqueue,"black")
    screen.draw.textbox("Welcome To Quiz Master...",marqueue,color="white")

    # Question box
    screen.draw.filled_rect(question_box, "darkblue")
    screen.draw.text( "Game over!\nYou got 2 questions correct!",center=question_box.center,color="white",fontsize=24)

    # Answer boxes
    for box in [answer_box1, answer_box2, answer_box3, answer_box4]:
        screen.draw.filled_rect(box, "orange")
        screen.draw.text("-",center=box.center,color="black",fontsize=50)

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

clock.schedule_interval(timer, 1.0)
pgzrun.go()