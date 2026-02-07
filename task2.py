# task2.py
from db import fetch_last_n_turns
# This dictionary stores session-level memory
session_memory = {
    "last_query": None,
    "last_event": None,
    "last_result": None
}
def get_db_context(n=3):
    """
    Fetch last N queries from database
    for multi-turn reasoning
    """
    return fetch_last_n_turns(n)
def update_context(query, event, result):
    """
    Stores the latest query, predicted event,
    and explanation result for multi-turn reasoning.
    """
    session_memory["last_query"] = query
    session_memory["last_event"] = event
    session_memory["last_result"] = result


def get_session_context():
    """
    Returns the stored session memory.
    Used for handling follow-up queries.
    """
    return session_memory