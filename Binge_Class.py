class DrinkingInfo:
    def __init__(self, category, year, term, metric, group, time, percentage):
        self.category = category
        self.year = year
        self.term = term
        self.metric = metric
        self.group = group
        self.time = time
        self.percentage = percentage
    def __repr__(self):
        return ('Category: {}\n'
                'Year: {} \n'
                'Term: {} \n'
                'Metric: {} \n'
                'Group: {} \n'
                'Number of times: {} \n'
                'Percentage: {} \n'
                '\n').format(self.category,self.year, self.term, self.metric, self.group, self.time, self.percentage)