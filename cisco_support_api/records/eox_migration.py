class EoxMigration:
    def __init__(self):
        self.information = None
        self.option = None
        self.product_id = None
        self.product_information_url = None
        self.product_name = None
        self.strategy = None
        self.pid_active_flag = None

    def __str__(self):
        strategy = self.strategy or 'n/a'
        return f'{strategy}'

    def __repr__(self):
        return f'<{self.__class__} {self.__str__()}>'