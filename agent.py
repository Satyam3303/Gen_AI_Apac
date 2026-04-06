from google.adk.agents import Agent, SequentialAgent
from tools import add_task, get_tasks, add_note

MODEL = "gemini-2.5-flash"

task_agent = Agent(
    name="task_agent",
    model=MODEL,
    instruction="Handle task operations",
    tools=[add_task, get_tasks]
)

notes_agent = Agent(
    name="notes_agent",
    model=MODEL,
    instruction="Handle notes",
    tools=[add_note]
)

workflow = SequentialAgent(
    name="workflow",
    sub_agents=[task_agent, notes_agent]
)

root_agent = Agent(
    name="root_agent",
    model=MODEL,
    instruction="Route user queries",
    sub_agents=[workflow]
)

def process_query(user_input: str):
    user_input = user_input.lower()

    # ADD TASK
    if "add task" in user_input:
        task = user_input.replace("add task", "").strip()
        return {
            "response": add_task(None, task),
            "agent": "Task Agent"
        }

    # SHOW TASKS
    elif "show tasks" in user_input or "list tasks" in user_input:
        return {
            "response": get_tasks(None),
            "agent": "Task Agent"
        }

    # ADD NOTE
    elif "note" in user_input or "add note" in user_input:
        note = user_input.replace("note", "").strip()
        return {
            "response": add_note(None, note),
            "agent": "Notes Agent"
        }

    # PLAN DAY
    elif "plan" in user_input:
        tasks = get_tasks(None)["tasks"]

        return {
            "response": f"You have {len(tasks)} tasks. Focus on important ones first.",
            "tasks": tasks,
            "agent": "Planner Agent"
        }

    # GREETING
    elif "hello" in user_input or "hi" in user_input:
        return {
            "response": "Hi! I can manage tasks, notes, and planning.",
            "agent": "Root Agent"
        }

    return {
        "response": "Try: add task, show tasks, note, plan my day",
        "agent": "Root Agent"
    }
    user_input = user_input.lower()

    if "add task" in user_input:
        return {
            "response": add_task(None, user_input),
            "agent": "Task Agent"
        }

    elif "show" in user_input:
        return {
            "response": get_tasks(None),
            "agent": "Task Agent"
        }

    elif "note" in user_input:
        return {
            "response": add_note(None, user_input),
            "agent": "Notes Agent"
        }

    return {
        "response": "Handled via ADK architecture",
        "agent": "Root Agent"
    }