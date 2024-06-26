import requests
from IPython.display import Image

image_url = "https://i.ibb.co/KyNtMw5/IMG-20240321-172354614-AE.jpg"
content = requests.get(image_url).content
Image(content)


from configparser import ConfigParser
import os

# Set up config parser
config = ConfigParser()
config.read("config.ini")

# Set up Google Gemini API key
os.environ["GOOGLE_API_KEY"] = config["Gemini"]["API_KEY"]

from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-pro-vision")
# example
image_url = "./ff.JPG"
# image_url = "https://i.ibb.co/KyNtMw5/IMG-20240321-172354614-AE.jpg"
# image_url_2 = "./aaa.JPG"
# image_url_3 = "./eeee.png"
# image_url = "images.jpeg"
user_question = "圖中的股票目前的趨勢是看好的嗎?"
user_question += " 請使用繁體中文回答。"
user_question += " 那依照目前美國股市大盤 今天會漲?"
message = HumanMessage(
    content=[
        {
            "type": "text",
            "text": user_question,
        },  # You can optionally provide text parts
        {"type": "image_url", "image_url": image_url}
    ]
)
result = llm.invoke([message])
print("問：", user_question)
print("答：", result.content.lstrip(" "))
if "http" in image_url:
    content = requests.get(image_url).content
else:
    content = image_url
Image(content)