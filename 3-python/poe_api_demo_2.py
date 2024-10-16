from openai import OpenAI

API_ENDPOINT = 'http://127.0.0.1:10000/v1'
API_KEY = 'vLXuN4NTHNe2ZOGG-1Ksl9-Zvftt6m8CAZpf3bXPMHg' # 从 https://poe.com/api_key 获取
MODEL_NAME = 'GPT-4o-Mini' # 按照 Poe 中的命名选择模型   #原文：GPT-4o

client = OpenAI(base_url=API_ENDPOINT, api_key=API_KEY)

print("Testing stream completion")

completion = client.chat.completions.create(
    model=MODEL_NAME,
    messages=[{"role": "user", "content": "Say this is a test"}],
    stream=True,
)

for chunk in completion:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
      
print("\n\nTesting non-stream completion")
        
completion = client.chat.completions.create(
    model=MODEL_NAME,
    messages=[{"role": "user", "content": "Say this is a test"}],
    stream=False,
)
print(completion.choices[0].message.content)