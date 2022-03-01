from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import PIL.ImageTk
import pyttsx3 as pp

engine = pp.init()

voices = engine.getProperty('voices')
print(voices)

engine.setProperty('voice', voices[0].id)


def speak(word):
    engine.say(word)
    engine.runAndWait()


    #Create a new chat bot named My Bot

bot = ChatBot("My Bot")
conversation = [
    "Hello",
    "Hi there!",
    "what is your name?",
    "my name is bot,i am created by Rabi Mandal",
    "How are you doing?",
    "I'm doing great these days.",
    "In which city do you live ?",
    "I live in delhi",
    "In which language you talk?",
    "I mostly talk in english",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

trainer = ListTrainer(bot)

#now training the bot with the help of trainer

trainer.train(conversation)

main = Tk()

main.geometry("500x650")

main.title("My Chat bot")

im = PIL.Image.open("bot2.png")
photo = PIL.ImageTk.PhotoImage(im)

label = Label(main, image=photo)
label.pack(pady=5)
#label.image = photo  # keep a reference!
label.pack()

def ask_from_bot():
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END, "you : " + query)
    print(type(answer_from_bot))
    msgs.insert(END, "bot : " + str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0, END)
    msgs.yview(END)


frame = Frame(main)

sc = Scrollbar(frame)
msgs = Listbox(frame, width=80, height=20, yscrollcommand=sc.set)

sc.pack(side=RIGHT, fill=Y)

msgs.pack(side=LEFT, fill=BOTH, pady=10)

frame.pack()


# creating text field

textF = Entry(main, font=("Verdana", 20))
textF.pack(fill=X, pady=10)

#creating a botton
btn = Button(main, text="Ask from bot", font=("Verdana", 20), command=ask_from_bot)
btn.pack()

# creating a function
def enter_function(event):
    btn.invoke()


# going to bind main window with enter key...

main.bind('<Return>', enter_function)




main.mainloop()