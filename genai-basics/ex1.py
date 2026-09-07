from google import genai

client=genai.Client(api_key="AQ.Ab8RN6LY9Wdg2jlSvcc7l1pw9n60jRfR-UgjgoDcFJEMr2vsCw")
question=input("Ask a question: ")
resp=client.models.generate_content(model="gemini-2.5-flash", contents=question)
print(resp.text)

