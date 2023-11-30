class get_db_override:
    def __init__(self, session):
        self.session = session

    def __call__(self):
        return self.session
