from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.tavily import TavilyTools
from dotenv import load_dotenv

load_dotenv()

model = Groq(
    id="meta-llama/llama-4-scout-17b-16e-instruct",
    temperature=0.0,  # Most deterministic
    top_p=1.0         # Do not truncate high-probability tokens
)

web_agent2 = Agent(
    name="web_agent2",
    model=model,
    tools=[TavilyTools()],
    show_tool_calls=True,
    markdown=True,
    instructions=[
        "Find competitors of Infosys and then check whether each one of them have collaborated with 'Virgin Media'.",
        "If yes, show the company's name and give one working link to a credible source confirming it.",
        "Ensure the link is not shortened or truncated, and must open to a valid page.",
        "You can also refer to credible social media websites like linkedin, facebook, twitter.",
        "Return the output in the following format:\n\n"
        "First, show the source used to identify the top competitors.\n\n"
        "Then return a table:\n\n"
        "| Company | Collaboration | Source Link |\n"
        "|---------|----------------|-------------|\n"
        "Only include rows where you have a valid working source link (not shortened) that confirms a collaboration."
    ]
)

web_agent2.print_response(
    "Find competitors of Infosys and then check whether each one of them have collaborated with 'Virgin Media'. If yes, show the company's name and give one working link to a credible source confirming it. Make sure the link is valid and complete. Make sure the source you are referring to very clearly mentions the collaboration. Do not make any assumptions. First mention the source from which you retrieved the top competitors then output the rest in a table format.",
    stream=True
)