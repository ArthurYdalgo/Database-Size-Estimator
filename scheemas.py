class Scheema():
    def __init__(self, name, tables=[]):
        self.name = name
        self.tables = tables

    def insertTable(self, table):
        self.tables.append(table)

    def insertTables(self, tables):
        self.tables = self.tables + tables

    def removeTable(self, table_index):
        del self.tables[table_index]

    def printTables(self):
        print("Tables")
        print([{"Name": table.name, "Min": table.calculateMinSize(), "Average": table.calculateAverageSize(
        ), "Max": table.calculateMaxSize()} for table in self.tables])

    def calculateMaxSize(self, unit='GB', raw=False):
        unit_converter = {'GB': 2**30, 'MB': 2**20, 'KB': 2**10}
        if not(unit in unit_converter):
            unit = 'GB'

        denominator = unit_converter[unit]

        print("Tables")
        tables = [table.calculateMaxSize(unit=unit)
              for table in self.tables]
        for table in tables:
            print(table)  

        size = sum([table.calculateMaxSize(raw=True)
                   for table in self.tables])
        if(raw):
            return size
        print("=======")
        return "{} -> {} {}".format(self.name, round(size/denominator, 3), unit)

    def calculateMinSize(self, unit='GB', raw=False):
        unit_converter = {'GB': 2**30, 'MB': 2**20, 'KB': 2**10}
        if not(unit in unit_converter):
            unit = 'GB'

        denominator = unit_converter[unit]

        print("Tables")
        tables = [table.calculateMinSize(unit=unit)
              for table in self.tables]
        for table in tables:
            print(table)  

        size = sum([table.calculateMinSize(raw=True)
                   for table in self.tables])
        if(raw):
            return size
        print("=======")
        return "{} -> {} {}".format(self.name, round(size/denominator, 3), unit)

    def calculateAverageSize(self, unit='GB', raw=False):
        unit_converter = {'GB': 2**30, 'MB': 2**20, 'KB': 2**10}
        if not(unit in unit_converter):
            unit = 'GB'
        
        denominator = unit_converter[unit]

        print("Tables")
        tables = [table.calculateAverageSize(unit=unit)
              for table in self.tables]
        for table in tables:
            print(table)        

        size = sum([table.calculateAverageSize(raw=True)
                   for table in self.tables])
        if(raw):
            return size
        print("=======")
        return "{} -> {} {}".format(self.name, round(size/denominator, 3), unit)
