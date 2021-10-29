class Table():
    def __init__(self, name, min_size=None, max_size=None, columns=[]):
        self.name = name
        self.columns = columns
        self.min_size = min_size
        self.max_size = max_size
        pass

    def insertColumn(self, column):
        self.columns.append(column)

    def insertColumns(self, columns):
        self.columns = self.columns + columns

    def removeColumn(self, column_index):
        del self.columns[column_index]

    def calculateMaxSize(self, rows=None, unit='GB', raw=False):
        unit_converter = {'GB': 2**30, 'MB': 2**20, 'KB': 2**10}
        if not(unit in unit_converter):
            unit = 'GB'

        denominator = unit_converter[unit]

        if(rows is None):
            rows = self.max_size

        size = (rows * (sum(column.maxSize()
                for column in self.columns)))
        if(raw):
            return size
        return "{} -> {} {}".format(self.name, round(size/denominator, 3), unit)

    def calculateMinSize(self, rows=None, unit='GB', raw=False):
        unit_converter = {'GB': 2**30, 'MB': 2**20, 'KB': 2**10}
        if not(unit in unit_converter):
            unit = 'GB'

        denominator = unit_converter[unit]

        if(rows is None):
            rows = self.min_size

        size = (rows * (sum(column.minSize()
                for column in self.columns)))
        if(raw):
            return size
        return "{} -> {} {}".format(self.name, round(size/denominator, 3), unit)

    def calculateAverageSize(self, rows=None, unit='GB', raw=False):
        unit_converter = {'GB': 2**30, 'MB': 2**20, 'KB': 2**10}
        if not(unit in unit_converter):
            unit = 'GB'

        denominator = unit_converter[unit]

        if(rows is None):
            rows = (self.max_size + self.min_size) / 2

        size = (rows * (sum(column.averageSize()
                for column in self.columns)))
        if(raw):
            return size
        return "{} -> {} {}".format(self.name, round(size/denominator, 3), unit)
