from e_utils.utils import extract_email_info

class EmailAgent:
    def __init__(self, memory):
        self.memory = memory

    def parse_email(self, entry_id, email_text):
        sender, urgency, intent = extract_email_info(email_text)
        result = {
            "sender": sender,
            "urgency": urgency,
            "intent": intent,
        }
        self.memory.store_extracted(entry_id, "email_agent", result)
        return result
