import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain, SequentialChain

os.environ['OPENAI_API_KEY'] = 'sk-wFU2DCcX77PpEVpoxnoAF5R2kg5tf1TIBKrUmr7v7nT3BlbkFJOw-WZED_PidnrmUaEefk4_3d4dh0JbNW0CPa6axUUA'

llm = OpenAI(model_name="gpt-4",temperature=0.6)



def gen(cuisine):
    # chain 1 -> restaurant name
    prompt_template_name = PromptTemplate(
    input_variables = ['cuisine'],
    template = "suggest one {cuisine} restaurant name")
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    # chain 2 -> menu items
    prompt_template_items = PromptTemplate(
    input_variables = ['restaurant_name'],
    template = "suggest some names of 5 comma separated menu items for {restaurant_name}")
    fooditems_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

    seq_chain_output = SequentialChain(
    chains = [name_chain, fooditems_chain],
    input_variables = ['cuisine'],
    output_variables = ['restaurant_name', 'menu_items']
    )

    response = seq_chain_output({'cuisine': cuisine})

    return response

if __name__ == "__main__":
    print(gen("Italian"))


