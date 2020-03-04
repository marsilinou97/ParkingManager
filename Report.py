class Report:
    def __init__(self, issued_on, start_range, end_range, revenue_categories):
        self.issue_on = issued_on
        self.start_range = start_range
        self.end_range = end_range
        self._revenue_categories = revenue_categories

    def get_issued_on(self):
        return self.issued_on

    def get_start_range(self):
        return self.start_range

    def get_issue_date(self):
        return self.issue_on

    def get_revenue_categories(self):
        return self._revenue_categories

    def set_issue_date(self, value):
        self.issue_on = value

    def set_revenue_categories(self, value):
        self._revenue_categories = value

    def __repr__(self):
        return "Issued date: " + str(self.issue_on) + "\tCategories: " + str(self._revenue_categories)
