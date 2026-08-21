import requests

url = "http://127.0.0.1:11434/api/generate"

data = {
    "model": "qwen3:4b",
    "prompt": "请只回复一句话：Ollama API 连接成功！",
    "stream": False,
}

session = requests.Session()

# 不读取系统代理设置
session.trust_env = False

response = session.post(
    url,
    json=data,
    timeout=120,
)

response.raise_for_status()

result = response.json()

print(result["response"])