import json
import os
from datetime import datetime

class JSONStore:
    def __init__(self, data__dir="data"):
        self.data__dir = data__dir
        os.makedirs(data__dir, exist_ok=True)
    
    def _get_file_path(self, entry_id):
        return os.path.join(self.data__dir, f"{entry_id}.json")
    
    def init_entry(self, entry_id, source):
        data = {
            "source": source,
            "timestamp": datetime.utcnow().isoformat(),
            "metadata": {},
            "extracted_field": {}
        }
        file_path = self._get_file_path(entry_id)
        with open(file_path, 'w') as f:
            json.dump(data, f)
    
    def update_metadata(self, entry_id, key, value):
        file_path = self._get_file_path(entry_id)
        if not os.path.exists(file_path):
            self.init_entry(entry_id, "unknown")
        with open(file_path, 'r+') as f:
            data = json.load(f)
            data['metadata'][key] = value
            f.seek(0)
            json.dump(data, f)
            f.truncate()
    
    def store_extracted(self, entry_id, agent, data):
        file_path = self._get_file_path(entry_id)
        if not os.path.exists(file_path):
            self.init_entry(entry_id, "unknown")
        with open(file_path, 'r+') as f:
            entry_data = json.load(f)
            entry_data['extracted_field'][agent] = data
            f.seek(0)
            json.dump(entry_data, f)
            f.truncate()
    
    def get_entry(self, entry_id):
        file_path = self._get_file_path(entry_id)
        if not os.path.exists(file_path):
            return {}
        with open(file_path, 'r') as f:
            return json.load(f)