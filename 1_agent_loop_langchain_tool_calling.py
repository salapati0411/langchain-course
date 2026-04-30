from dotenv  import load_dotenv
load_dotenv()  # Load environment variables from .env file

from langchain.chat_models import init_chat_model
from langchain.tools import tool
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage, ToolMessage
from langsmith import traceable


MAX_ITERATIONS = 10
MODEL = "qwen3:1.7b"

@tool
def get_product_price(product_name: str) -> str:
    """ Look up the price of a product in the catalog. """
    print(f"Looking up price for: {product_name}")    
    # Simulate a tool that retrieves product price
    prices = {
        "laptop": "$999",
        "smartphone": "$499",
        "headphones": "$199"
    }
    return prices.get(product_name.lower(), "Product not found")

@tool
def apply_discount(price: str, discount_tier: str) -> float:
    """ Apply a discount to a price based on the discount tier. """
    print(f"Applying {discount_tier} discount to price: {price}")
    # Simulate a tool that applies a discount
    try:
        price_value = float(price.strip('$'))
        if discount_tier == "silver":
            discounted_price = price_value * 0.9  # 10% off
        elif discount_tier == "gold":
            discounted_price = price_value * 0.8  # 20% off
        elif discount_tier == "platinum":
            discounted_price = price_value * 0.7  # 30% off
        else:
            return "Invalid discount tier"
        return f"${discounted_price:.2f}"
    except ValueError:
        return "Invalid price format"
    

    # ----- AGENT LOOP ---------
@traceable(name="agent_loop_with_tool_calling")
def run_agent(question: str):
    tools = [get_product_price, apply_discount]
    tool_dict = {tool.name: tool for tool in tools}

    llm= init_chat_model(f"ollama:{MODEL}", temperature=0)
    

if __name__ == "__main__":
    print("Welcome to the LangChain Agent Loop with Tool Calling!")
    print()
    result = run_agent("What is the price of a laptop with a gold discount?")
    print()