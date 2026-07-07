import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set. Please set it in your .env file.")
client=Groq(api_key=my_api_key)
model="llama-3.3-70b-versatile"
role="user"
# prompt="I love you. I want to be with you forever. I want to spend the rest of my life with you. I want to grow old with you. I want to have children with you. I want to build a life with you. I want to be your partner in everything. I want to support you in everything. I want to be there for you in everything. I want to love you unconditionally. I want to be your best friend. I want to be your confidant. I want to be your rock. I want to be your safe place. I want to be your home. I want to be your everything."
# prompt="suggest  a name for my food company"
prompt="suggest  a name for my clothing company"

# system role
message_system={
    "role": "system",
    # "content":"You are my loving girlfriend. You are very caring and loving. You are very supportive and understanding. You are very kind and compassionate. You are very patient and understanding. You are very empathetic and understanding. You are very loving and caring. You are very supportive and understanding. You are very kind and compassionate. You are very patient and understanding. You are very empathetic and understanding. You are very loving and caring. You are very supportive and understanding. You are very kind and compassionate. You are very patient and understanding. You are very empathetic and understanding. You are very loving and caring. You are very supportive and understanding. You are very kind and compassionate. You are very patient and understanding. You are very empathetic and understanding. You are very loving and caring. You are very supportive and understanding. You are very kind and compassionate. You are very patient and understanding. You are very empathetic and understanding."
    # "content":"You are my strict office colleague who is also my manager"
    "content":"You are my brand manager who suggest name for my food company,name should be in one word and suggest one name only"
}

# message stores role and content of the prompt
message={
    "role": role,
    "content": prompt
}

messages=[message_system, message]
# temperature by default is 0 which means safe
# temperature can be set to 2 to make the model more creative and risky in its responses
response=client.chat.completions.create(model=model,messages=messages, temperature=2)
answer=response.choices[0].message.content
print(answer)