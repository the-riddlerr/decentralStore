class State:
    def __init__(self, ledger_entries):
        self.ledger_entries = ledger_entries

    def get_ledger_entries(self):
        return self.ledger_entries

    def set_ledger_entries(self, ledger_entries):
        self.ledger_entries = ledger_entries
