class Column():
    def __init__(self, name, type, min_size = None, max_size=None):
        self.name = name
        self.min_size = min_size
        self.max_size = max_size
        self.type = type

        self.default_type_sizes = {
            'text' : 65535,
            'longText': 4294967295,
            'tinyInteger': 1,
            'string' : 255,
            'timestamp' : 19,
            'timestamps' : 19 * 2,
            'json' : 4294967295,
            'increments' : 4,
            'id' : 8,
            'foreignId': 8,
            'bool': 1,
            'boolean': 1,
            'enum': 255,
            'softDeletes': 19,
            'rememberToken': 100,
            'dateTime': 19
        }
        pass

    def maxSize(self):
        if(self.max_size and isinstance(self.max_size,int)):
            return self.max_size
        if(self.max_size and self.max_size == 'default' and self.type in self.default_type_sizes):
            return self.max_size
        if(self.type in self.default_type_sizes):
            return self.default_type_sizes[self.type]
        return 0

    def minSize(self):
        if(self.min_size and isinstance(self.min_size,int)):
            return self.min_size
        if(self.min_size and self.min_size == 'default' and self.type in self.default_type_sizes):
            return self.min_size
        if(self.type in self.default_type_sizes):
            return self.default_type_sizes[self.type]
        return 0

    def averageSize(self):
        return (self.maxSize() + self.minSize()) / 2

    
