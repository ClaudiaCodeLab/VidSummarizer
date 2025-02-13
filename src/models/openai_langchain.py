import os
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def summarize_openai(text):
    # Use the correct model name
    llm = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))

    # Construct messages
    messages = [
        SystemMessage(content="""
        You are a helpful assistant who provides concise and accurate summaries of text. Your task is to:
        
        - Capture the key points of the content.
        - Keep the summary brief and easy to understand.
        - Avoid summarizing overly lengthy texts or breaking them into excessively short summaries.
        - Use bullet points where appropriate to enhance clarity and structure.
        """),
        HumanMessage(content=f"Summarize the following text: {text}")
    ]

    # Invoke the model
    response = llm.invoke(messages)
    return response.content


# Test the function
# if __name__ == "__main__":
#     sample_text = "This is a test transcript of a YouTube video explaining LangChain and OpenAI."
    
#     summary = summarize_openai(sample_text)
#     print(summary)