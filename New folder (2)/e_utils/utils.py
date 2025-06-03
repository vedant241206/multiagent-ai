import re
import json

def detect_format(data):
    try:
        json.loads(data)
        return "json"
    except json.JSONDecodeError:
        if "From:" in data and "@" in data:
            return "email"
    return "unknown"

def detect_intent(data, format_type):
    lower_data = data.lower()
    if "quote" in lower_data:
        return "RFQ"
    elif "invoice" in lower_data:
        return "Invoice"
    elif "regulation" in lower_data:
        return "Regulation"
    elif "complaint" in lower_data:
        return "Complaint"
    return "General"

def extract_email_info(email):
    sender_match = re.search(r"From:\s*(.*)", email)
    sender = sender_match.group(1).strip() if sender_match else "Unknown"
    urgency = "high" if "urgent" in email.lower() else "normal"
    intent = detect_intent(email, "email")
    return sender, urgency, intent

def validate_json_schema(data):
    required = ["id", "type", "payload"]
    missing = [field for field in required if field not in data]
    return len(missing) == 0, missing
