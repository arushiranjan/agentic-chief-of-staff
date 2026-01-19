from dotenv import load_dotenv
from langgraph.graph import StateGraph

from memory import save_memory, get_all_memory

# Load environment variables
load_dotenv()

def chat_node(state):
    user_id = "default_user"
    user_text = state["message"]

    # 1️⃣ MEMORY EXTRACTION (from chat)
    lowered = user_text.lower()
    if "hate" in lowered and "meeting" in lowered:
        save_memory(
            user_id=user_id,
            key="meeting_preference",
            value=user_text
        )

    # 2️⃣ MEMORY RETRIEVAL
    memory = get_all_memory(user_id)

    # 3️⃣ RESPONSE (prove memory works)
    return {
        "reply": f"I remember these about you: {memory}"
    }

# LangGraph setup
graph = StateGraph(dict)
graph.add_node("chat", chat_node)
graph.set_entry_point("chat")
graph.set_finish_point("chat")

app = graph.compile()
