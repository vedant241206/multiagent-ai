import json
from e_utils.utils import detect_format, detect_intent
from c_agents.email_agent import EmailAgent
from c_agents.json_agent import JSONAgent

class ClassifierAgent:
    def __init__(self, memory):
        self.memory = memory
        self.email_agent = EmailAgent(memory)
        self.json_agent = JSONAgent(memory)

    def handle_input(self, entry_id, raw_input):
        format_type = detect_format(raw_input)
        intent = detect_intent(raw_input, format_type)

        self.memory.init_entry(entry_id, source=raw_input)
        self.memory.update_metadata(entry_id, "format", format_type)
        self.memory.update_metadata(entry_id, "intent", intent)

        if format_type == "email":
            return self.email_agent.parse_email(entry_id, raw_input)
        elif format_type == "json":
            return self.json_agent.handle_json(entry_id, json.loads(raw_input))
        else:
            return {"error": f"Unsupported format: {format_type}"}
