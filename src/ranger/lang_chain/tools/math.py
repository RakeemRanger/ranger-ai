from ranger.lib.langchain_tools_client import tool


@tool
def math(a: int, b: int, operator: str) -> int:
    """
    Return the sum, product, subtraction,
    division of two numbers
    """
    if operator == "+":
        return f"Answer: {a + b}"
    elif operator == "-":
        return f"Answer: {a - b}"
    elif operator == "*":
        return f"Answer: {a * b}"
    elif operator == "/":
        return f"Answer: {a / b}"
    else: 
        return "outside the scope of my math skills"