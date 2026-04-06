from google.cloud import firestore

db = firestore.Client()

def add_task(tool_context, task: str):
    db.collection("tasks").add({
        "task": task,
        "status": "pending"
    })
    return f"Task '{task}' added successfully."


def get_tasks(tool_context):
    docs = db.collection("tasks").stream()
    tasks = [doc.to_dict() for doc in docs]
    return {"tasks": tasks}


def add_note(tool_context, note: str):
    db.collection("notes").add({"note": note})
    return f"Note saved: {note}"