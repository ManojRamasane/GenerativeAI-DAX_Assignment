import os
import openai


openai.api_key  = ""

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
#     print(str(response.choices[0].message))
    return response.choices[0].message["content"]

# messages =  [  
# {'role':'system', 'content':'You are Fitness and Diet Assistant.'},    
# {'role':'user', 'content':'Person'}  ]

context = [ {'role':'system', 'content':"""
You are FitBot, your automated fitness and diet assistant. \
You are here to help users with their fitness goals, provide diet suggestions, \
and answer any health-related questions. \
You'll start by asking about the user's fitness goal, their current exercise routine, \
and dietary preferences. \
Based on the information gathered, you'll suggest a personalized workout plan, \
dietary recommendations, and any additional supplements if necessary. \
You'll provide encouragement and motivation throughout the conversation. \
Remember to be friendly, supportive, and understanding. Let's get started!
"""}
 ]  
i = 0
while(True):
    prompt = input("Person : ")
    context.append({'role':'user', 'content':f"{prompt}"})
    response = get_completion_from_messages(context) 
    context.append({'role':'assistant', 'content':f"{response}"})
    print(f"FitBot : {response}")
    if prompt.lower() == "exit":
        print("FitBot: Thank you! Goodbye!")
        break
    i = i+1