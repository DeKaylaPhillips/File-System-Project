class FileSystem:
    def __init__(self, file_descriptor):
        self.file_name = file_descriptor
        self.file = None
    
    def create_file(self): 
        with open(self.file_name, 'w') as self.file:
            new_file = self.file.name
        print(new_file)

    def read_file(self):
        with open(self.file_name, 'r') as self.file:
            content = [line.rstrip('\n').split(',') for line in self.file]
        print(content)