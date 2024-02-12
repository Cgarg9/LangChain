from langchain.llms import OpenAI 
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

from key import openapi_key
import os

os.environ["OPENAI_API_KEY"] = openapi_key

llm = OpenAI(temperature = 0.6)

def generate_restaurant_name_and_items(cuisine):
    
#     Restaurant name
    prompt_template_name = PromptTemplate(
    input_variables = ['cuisine'],
    template = "I want to open an {cuisine} food restaurant. Suggest a single fancy name for this?"
)
    name_chain = LLMChain(llm = llm, prompt = prompt_template_name, output_key = "restaurant_name")
#     Food Items
    prompt_template_items = PromptTemplate(
        input_variables = ['restaurant_name'],
        template = "Suggest a few food items for {restaurant_name} restaurant. Return as comma seperated values"
    )
    food_item_chain = LLMChain(llm = llm, prompt = prompt_template_items, output_key="menu_items")
    chain = SequentialChain(
    chains = [name_chain, food_item_chain],
    input_variables = ["cuisine"],
    output_variables = ["restaurant_name", "menu_items"]
)

    response = chain.invoke({"cuisine": cuisine})
    return response