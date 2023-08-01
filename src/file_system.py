class File_System:
    def __init__(self, file_descriptor):
        self.file_name = file_descriptor
        self.file = None
    
    def create_file(self): 
        self.file = open(self.file_name, 'x')
        self.file.close()
        
    
    

