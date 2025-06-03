import uuid
from b_memory.memory_store import MemoryStore
#import memory
from c_agents.classifier_agent import ClassifierAgent

class Orchestrator:
    def __init__(self):
        self.memory = MemoryStore()
        self.classifier = ClassifierAgent(self.memory)

    def process_input(self, raw_input):
        entry_id = str(uuid.uuid4())
        output = self.classifier.handle_input(entry_id, raw_input)
        full_memory = self.memory.get_entry(entry_id)
        return {
            "output": output,
            "memory": full_memory
        }
