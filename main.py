from messageProcessor import MessageProcessor
from message import Message

if __name__ == "__main__":
    proc = MessageProcessor()
    print("Hi, lets talk a bit?")
    while proc.continue_dialog:
        message = Message(input("Enter your message >> "))
        message.analyze()
        answer = proc.generate_answer(message)
        print(answer)
