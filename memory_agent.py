class MemoryAgent:
    def __init__(self):
        self.memory = {}

    def save(self, session_id, key, value):
        if session_id not in self.memory:
            self.memory[session_id] = {}

        self.memory[session_id][key] = value

    def load(self, session_id, key):
        return self.memory.get(session_id, {}).get(key)

    def get_all(self, session_id):
        return self.memory.get(session_id, {})