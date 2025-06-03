from e_utils.utils import validate_json_schema

class JSONAgent:
    def __init__(self, memory):
        self.memory = memory

    def handle_json(self, entry_id, json_data):
        valid, issues = validate_json_schema(json_data)
        result = {
            "cleaned_data": json_data,
            "validation_issues": issues if not valid else []
        }
        self.memory.store_extracted(entry_id, "json_agent", result)
        return result
