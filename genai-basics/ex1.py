from google import genai

client=genai.Client(api_key="")
question=input("Ask a question: ")
resp=client.models.generate_content(model="gemini-2.5-flash", contents=question)
print(resp.text)

