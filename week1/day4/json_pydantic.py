import os
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel
import json

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set. Please set it in your .env file.")
client=Groq(api_key=my_api_key)
model="llama-3.3-70b-versatile"
# need structure output so we use pydantic model to define the output structure
class Ticket(BaseModel):
    name: str
    issue:str
    email: str
    phone_number:str

#schema 
schema=Ticket.model_json_schema()
#response format
response_format={
    "type": "json_object"
}
system_prompt=f"""
extract the personal information from the user complaint and return it in the following json format:
{schema}
"""
message_system={
    "role": "system",
    "content": system_prompt
}

# user complaint
text="Hello,My name is John Smith. My father's name is Robert Smith.I recently purchased a product from your store. However, I am extremely disappointed with the quality of the item. It arrived damaged and does not function as advertised.I would like to request a refund or a replacement for the defective product.My contact details are:Address221B Baker StreetLondon, NW1 6XEUnited KingdomEmail: john.smith@example.comPhone Number: +44 7700 900123Please let me know how to proceed with this matter.Thank you."
# use f string so that we can easily insert the text variable into the prompt
prompt=f"""
this is a user complaint, please extract the personal information from this text.
{text}
"""
message_user={
    "role": "user",
    "content": prompt
}
messages=[message_system, message_user]
response=client.chat.completions.create(model=model,messages=messages,response_format=response_format);
answer=response.choices[0].message.content
print(answer)

# parse the answer to read and acess the values in the json object


parsed_answer=json.loads(answer)
ticket=Ticket(**parsed_answer)

print(ticket.name)
print(ticket.issue)
print(ticket.email)
print(ticket.phone_number)