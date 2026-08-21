import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("没有读取到 OPENAI_API_KEY，请检查 .env 文件")

client = OpenAI(api_key=api_key)

response = client.responses.create(
    model="gpt-5.6-luna",
    input="请只回复一句话：API 连接成功！",
)

print(response.output_text)