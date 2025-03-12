
import google.generativeai as genai

genai.configure(api_key="AIzaSyC1ouq4haT3O-1ksEtpyxJq6uwuef0lcLQ") 


model = genai.GenerativeModel('gemini-pro')  

prompt_parts = [
    "What is the capital of following country?",
    "India"
]

response = model.generate_content(prompt_parts)


print(response.text)