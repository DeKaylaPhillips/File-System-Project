class FileSystem:
    def __init__(self, file_descriptor):
        self.file_name = file_descriptor
        self.file = None
    
    def create_file(self): 
        with open(self.file_name, 'w') as self.file:
            new_file = self.file.name
        print(new_file)