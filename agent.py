from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.tavily import TavilyTools
from dotenv import load_dotenv

load_dotenv()

model = Groq(
    id="qwen-qwq-32b",
    temperature=0.0,
    top_p=1.0
)

web_agent2 = Agent(
    name="web_agent2",
    model=model,
    tools=[TavilyTools()],
    show_tool_calls=True,
    markdown=True,
    instructions=[
        "Step 1: Use Tavily to find a credible, working source that lists competitors of Infosys.",
        "Step 2: From that source, extract as many competitors as possible — do not limit the number.",
        "Step 3: For each competitor, check if the company has collaborated with 'Virgin Media' using Tavily.",
        "Only include real, verifiable collaborations (e.g., projects, partnerships, co-deployments).",
        "You may use credible social platforms (LinkedIn, Twitter, Facebook) if they explicitly confirm the collaboration.",
        "Ensure each link is complete, working, and not shortened.",
        "Return the output in the following format:\n\n"
        "**Source for Infosys competitors:** <URL>\n\n"
        "| Company | Collaboration | Source Link |\n"
        "|---------|----------------|-------------|\n"
        "Only include rows where the collaboration is clearly confirmed by the source."
    ]
)

web_agent2.print_response(
    "Find competitors of Infosys and then check whether each one of them have collaborated with 'Virgin Media'. If yes, show the company's name and give one working link to a credible source confirming it. Make sure the link is valid and complete. Make sure the source you are referring to very clearly mentions the collaboration. Do not make any assumptions. First mention the source from which you retrieved the top competitors then output the rest in a table format. Check as many competitors as you can.",
    stream=True
)
