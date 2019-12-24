from tkinter import *
import tkinter as TK
from tkinter import ttk
import time as t
# pip install pillow
from PIL import Image, ImageTk

Questions = [{'image': "banana.jpeg", 'answer': 'Banana', 'hint':'An important part of your calcium dose'},
             {'image': "tiger.jpeg", 'answer': 'Tiger', 'hint': 'National animal of India'},
             {'image': "ronaldo.jpeg", 'answer': 'Christiano Ronaldo', 'hint':'CR7'},
             {'image': "audi.jpeg", 'answer': 'Audi', 'hint':"One of the world's biggest car manufacturers"},
             {'image': "spiderman.jpeg", 'answer': 'Spiderman', 'hint':'Peter Parker'},
             {'image': "sundar.jpeg", 'answer': 'Sundar Pichai', 'hint':'recently made CEO of Alphabet inc.'},
             {'image': "MIT.jpeg", 'answer': 'Massachusetts Institute of Technology', 'hint': "World's number 1 university" },
             {'image': "tesla.jpeg", 'answer': 'Nikola Tesla', 'hint':'Father of AC current'},
             {'image': "python.jpeg", 'answer': 'Guido Van Rossum', 'hint':"Python"},
             {'image': "hyperloop.jpeg", 'answer': 'Hyperloop', 'hint':'A concept by elon musk'},
             ]

score = 0
time = 15
counter = 0
game_state = False


def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func


def hint(do=''):
    global score
    win = TK.Toplevel()
    if do == '':
        win.wm_title("Hint")
        win.configure(background='#fdcb6e')

        l = TK.Label(win, text=Questions[counter]['hint'], font='Arial 20 bold' , bg="#ecf0f1")
        l.grid(row=0, column=0)

        b = ttk.Button(win, text="OK", command=win.destroy)
        b.grid(row=1, column=0)

    elif do == 'finished' :

        win.wm_title("Result")
        win.configure(background='#fdcb6e')
        l = TK.Label(win, text="Hope you had a good time playing!\n Your score is " + str(score), font='Arial 15 bold',
                     bg="#ecf0f1")
        l.grid(row=0, column=0)

        b = ttk.Button(win, text="Play Again..", command=combine_funcs(win.destroy, reset), width=40)
        b.grid(row=1, column=0)

        q = ttk.Button(win, text="Quit", command=root.quit, width=40)
        q.grid(row=2, column=0)

    elif do == 'rules':
        win.wm_title("Rules")
        win.configure(background='#fdcb6e')
        l = TK.Label(win, text="Wildcard Guess Game\nRules:\nThere are 10 questions in total\nAnswer of the questions is supposed to be typed in the 'card name' textbox\nClick on 'submit' to check the answer and move to next question\nIf name of a person is asked type the full name\nIf your answer is right your textbox turns green and \n'Well Played' is displayed in the 'right answer' textbox\nIf your answer is right your textbox turns red and the \n correct answer is displayed in the 'right answer' textbox\nAll questions must be answered within 15 seconds only \n Incase you dont submit your answer within 15 sec the text in the text box will be autosubmitted\nHints are available for every question\nEnjoy!!", font='Arial 15 bold',
                     bg="#ecf0f1")
        l.grid(row=0, column=0)

        b = ttk.Button(win, text="Start!", command=combine_funcs(win.destroy, reset), width=40)
        b.grid(row=1, column=0)


def check(str):
    global Questions, time,score
    if str.lower() == Questions[counter]['answer'].lower():
        e1.configure(bg='green')
        e2.config(fg='green' , state = 'normal')
        e2.delete(0, END)
        e2.insert(0, 'Well Played!')
        e2.config(state='disabled')
        t.sleep(1)
        score += 1

    else:
        e1.configure(bg='red')
        e2.config(fg='red', state = 'normal')
        e2.delete(0, END)
        e2.insert(0, Questions[counter]['answer'])
        e2.config(state='disabled')
        t.sleep(1)

    e1.delete(0, END)
    load_next()
    time = 15


def control_time():
    global game_state
    global time
    if game_state == False:
        return
    time_label.config(text='Time Left: ' + str(time))
    time_label.after(1000, control_time)
    time -= 1
    if time == -1:
        check(e1.get())
        time = 15


def load_next():
    global game_state, counter,time
    if counter == 9 :
        game_state = False
        hint('finished')

    else:
        counter += 1
        load = Image.open(Questions[counter]['image'])
        load = load.resize((200, 200), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img.config(image=render)
        img.image = render
    scr['text'] = "Score: " +str(score)


def reset():
    global counter,score, time,game_state

    time = 15
    counter = 0
    score = 0
    load = Image.open(Questions[counter]['image'])
    load = load.resize((200, 200), Image.ANTIALIAS)
    render = ImageTk.PhotoImage(load)
    img.config(image=render)
    img.image = render
    e1.config(bg="#ffffff")
    e2.config(state='normal')
    e2.delete(0, END)
    e2.insert(0, '')
    e2.config(state='disabled')
    e1.delete(0, END)
    scr['text']='Score: 0'
    game_state = True
    control_time()


root = Tk()
root.configure(background='#fdcb6e')
root.wm_title("Card Game")
root.geometry("700x500")
load = Image.open(Questions[counter]['image'])
load = load.resize((200, 200), Image.ANTIALIAS)
render = ImageTk.PhotoImage(load)
img = Label(root, image=render)
img.image = render
img.place(x=250, y=100)

txt = Label(root, text="Card name:", font='Comic 10 bold', bg="#ecf0f1")
txt.place(x=150, y=350)

scr = Label(root, text="Score: 0", font='Comic 15 bold', bg="#ecf0f1")
scr.place(x=600, y=0)


e1 = Entry(root, width=30)
e1.place(x=250, y=350)

txt2 = Label(root, text="Right Answer:", font='Comic 10 bold', bg="#ecf0f1")
txt2.place(x=130, y=380)

e2 = Entry(root, width=30, state='disabled')
e2.place(x=250, y=380)

hint_button = Button(root, text="Hint", command=hint, bg="#ecf0f1", font='Comic 10 bold')
hint_button.place(x=230, y=430)

submit = Button(root, command=lambda: check(e1.get()), text="Submit", bg="#ecf0f1", font='Comic 10 bold')
submit.place(x=330, y=430)

time_label = Label(root, text="Time Left:", font='Comic 15 bold', bg="#ecf0f1")
time_label.place(x=0, y=0)

hint('rules')
control_time()
root.mainloop()





