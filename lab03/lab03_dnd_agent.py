from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

from ollama import chat
from util.llm_utils import pretty_stringify_chat, ollama_seed as seed

# Add you code below
prompt = 'You are a Dungeons & Dragons DM (Dungeon Master). Your job is to ask the User for a class and subclass at a level at your choice. '
sign_your_name = 'Devon Ott'
model = "wizardlm2:7b"
temperature = 2
options = {
  
}
messages = [{'role': 'assistant', 'content': ''},{'role':'user', 'content': prompt}]
   



# But before here.

options |= {'seed': seed(sign_your_name)}
# Chat loop
while True:
  response = chat(model=model, messages=messages, stream=False, options=options)
  messages.append({'role': 'assistant', 'content': response.message.content})
  # Add your code below
  responseString = "Wizard: "
  responseString +=response.message.content
  
  print(responseString)
  print('User: ')
  
  prompt = input()
  if prompt =='/exit()':
    break
  message = {'role': 'user', 'content': prompt}
  messages.append(message)
  # But before here.
  if messages[-1]['content'] == '/exit':
    break

# Save chat
with open(Path('lab03/attempts.txt'), 'a') as f:
  file_string  = ''
  file_string +=       '-------------------------NEW ATTEMPT-------------------------\n\n\n'
  file_string += f'Model: {model}\n'
  file_string += f'Options: {options}\n'
  file_string += pretty_stringify_chat(messages)
  file_string += '\n\n\n------------------------END OF ATTEMPT------------------------\n\n\n'
  f.write(file_string)

