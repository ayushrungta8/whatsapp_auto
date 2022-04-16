from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Whatsapp import send_msg
from fastapi import BackgroundTasks

server = FastAPI()

origins = ["*"]
server.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"]
)


@server.get("/")
def heartbeat():
    return {
        "message": "Up and Alive 🔥"
    }


@server.get("/send-message")
def send_message(message: str, number: str, password: str, bg: BackgroundTasks):
    if password != "str@ongMedha":
        return {
            "message": "Wrong credentials"
        }
    bg.add_task(send_msg, number, message)
    try:
        return {
            "message": "done"
        }
    except Exception as e:
        print(e, "for message", message, number)
        return {
            "message": "something went wrong",
        }
