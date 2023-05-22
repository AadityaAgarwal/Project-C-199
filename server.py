import socket
from threading import Thread
import random

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_address="127.0.0.1"
port=8000
server.bind((ip_address,port))

server.listen()
clients_list=[]

questions = [
     " What is the Italian word for PIE? \n a.Mozarella\n b.Pasty\n c.Patty\n d.Pizza",
     " Water boils at 212 Units at which scale? \n a.Fahrenheit\n b.Celsius\n c.Rankine\n d.Kelvin",
     " Which sea creature has three hearts? \n a.Dolphin\n b.Octopus\n c.Walrus\n d.Seal",
     " Who was the character famous in our childhood rhymes associated with a lamb? \n a.Mary\n b.Jack\n c.Johnny\n d.Mukesh",
     " How many bones does an adult human have? \n a.206\n b.208\n c.201\n d.196",
     " How many wonders are there in the world? \n a.7\n b.8\n c.10\n d.4",
     " What element does not exist? \n a.Xf\n b.Re\n c.Si\n d.Pa",
     " How many states are there in India? \n a.24\n b.29\n c.30\n d.31",
     " Who invented the telephone? \n a.A.G Bell\n b.John Wick\n c.Thomas Edison\n d.G Marconi",
     " Who is Loki? \n a.God of Thunder\n b.God of Dwarves\n c.God of Mischief\n d.God of Gods",
     " Who was the first Indian female astronaut ? \n a.Sunita Williams\n b.Kalpana Chawla\n c.None of them\n d.Both of them ",
     " What is the smallest continent? \n a.Asia\n b.Antarctic\n c.Africa\n d.Australia",
     " The beaver is the national embelem of which country? \n a.Zimbabwe\n b.Iceland\n c.Argentina\n d.Canada",
     " How many players are on the field in baseball? \n a.6\n b.7\n c.9\n d.8",
     " Hg stands for? \n a.Mercury\n b.Hulgerium\n c.Argenine\n d.Halfnium",
     " Who gifted the Statue of Libery to the US? \n a.Brazil\n b.France\n c.Wales\n d.Germany",
     " Which planet is closest to the sun? \n a.Mercury\n b.Pluto\n c.Earth\n d.Venus"
]

answers = ['d', 'a', 'b', 'a', 'a', 'a', 'a', 'b', 'a', 'c', 'b', 'd', 'd', 'c', 'a', 'b', 'a']


print("Server is started")


def get_random_question_answer(con,addr):
    random_index=random.randint(0,len(questions)-1)
    question=questions[random_index]
    answer=answers[random_index]
    con.send(question.encode('utf-8'))
    return random_index,question,answer

def remove_question(i):
    questions.pop(i)
    answers.pop(i)

def client_thread(con,addr):
    score=0
    con.send("Welcome to the quiz game!".encode("utf-8"))
    con.send("Enter the correct option number (a/b/c/d) only".encode("utf-8"))
    index, question, answer = get_random_question_answer(con)
    while True:
        try:
            message = con.recv(2048).decode('utf-8')
            if message:
                if message.lower() == answer:
                    score += 1
                    con.send(f"Correct answer! Score: {score}".encode('utf-8'))
                else:
                    con.send("Wrong answer!".encode('utf-8'))
                remove_question(index)
                index, question, answer = get_random_question_answer(con)
            else:
                remove(con)
        except:
            continue
def remove(con):
    if con in clients_list:
        clients_list.remove(con)
while True:

    con,addr=server.accept()
    clients_list.append(con)
    print(addr[0]," connected")

    new_thread=Thread(target=client_thread,args=(con,addr))
    new_thread.start