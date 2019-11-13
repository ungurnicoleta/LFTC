class PIF:
    def __init__(self):
        self.content = []

    def add(self, code, identifier):
        self.content.append((code, identifier))

    def __str__(self):
        return str(self.content)
