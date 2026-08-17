import os
from google import genai
from dotenv import load_dotenv
from PIL import Image

load_dotenv()


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
Photo = Image.open(r"C:\projetos\Pyai\test.png")
chat = client.chats.create(model = "gemini-3.1-flash-lite")

response = chat.send_message([Photo, "Analyze the image and say what you see"])
print ("Ai", response.text)

while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        break

    response = chat.send_message(user_input)
    print("AI:", response.text)