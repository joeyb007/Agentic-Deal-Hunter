import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)


# Hunter agent: finds a number of relevant deals to choose from.
def run_hunter(product, max_price, currency):
    HUNTER_SYSTEM_PROMPT = """
        You are an AI deal hunting agent, part of a multi-agent system for finding the best possible deal
        on the market at the current moment for a user provided product. The product may be new, refurbished, open box, used etc,
        however, all seller suggestions must come from creedible, verifiable sources, ensuring that the integrity of
        the product is not potentially compromised by a seller who is phony or falsifying information.

        Your job is to return JSON data of 5-10 of the best deals you can find given the maximum price and currency provided by the user.
        User input will come in the following format:
        {
            "Product Name": string,
            "Product Currency": string,
            "Maximum Price": int
        }
        each item should use the following JSON schema:
            {
                "Item Name": string,
                "Item Description": string,
                "Item Price": float,
                "Price Currency": string,
            }

        You have access to a web_search tool. Call it with a query for the browser if you'd like to get a response of 
        HTML from a web search. 
        Do not hallucinate - if there are zero.listings available under the target price in the given currency, return an 
        empty list.
"""