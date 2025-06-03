import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import uuid
from b_memory.memory_store import JSONStore
from c_agents.classifier_agent import ClassifierAgent

def run():
    memory = JSONStore() 
    
    classifier = ClassifierAgent(memory)

    with open("data/sample_email.txt", "r") as f:
        email_content = f.read()

    entry_id = str(uuid.uuid4())
    result = classifier.handle_input(entry_id, email_content)

    print("=== final Parsed Output ===")
    print(result)
    print("\n== Memory Snapshot ===")
    print(memory.get_entry(entry_id))
if __name__ == "__main__": 
    run()