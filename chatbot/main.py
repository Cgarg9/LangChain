from langchain_community.llms import OpenAI
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage
OpenAI.API_KEY = 'sk-'
chat = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0.2, api_key = 'sk')

print("Welcome to the chatbot!")
inputLangugae = input("Please type in a language ")
def chat_with_bot():
    print("Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        ans = chat.invoke(
            [
                HumanMessage(
                    content=f"You are a helpful coding assistant.The user has given a language of his preference : `{inputLangugae}`. Give you answers in this language only. The user has also given `{user_input}` as the question that needs to be answered. Please provide a detailed theoretical explanation. Do not give code for the query.If you do not know the asnwer please reply with 'This is beyond my scope'. Also return this answer if the question is unrelated to computer fundamentals. The following must be provided in the answer : 'definiton', 'use-case'. provide atleast 500 words of explanation"
                )
            ]
        )
        print(ans)

# Run the chat function
chat_with_bot()