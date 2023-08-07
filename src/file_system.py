from src.validator import Validator
class FileSystem: 
    def __init__(self, file_descriptor, Validator, Formatter):
        self.file_name = file_descriptor
        self.validate = Validator()
        self.format = Formatter()
    
    def create_file(self, headers_list): 
        with open(self.file_name, 'w') as file:
            new_file = file.name
            headers = self.format.get_csv_formatted_headers(headers_list)
            file.write(headers)
        print(new_file)

    def read_file(self):
        with open(self.file_name, 'r') as file:
            content = [line.rstrip('\n').split(',') for line in file]
        print(content)
    
    def update_file(self, data_list):
        if self.validate.is_valid_data_input(self.__get_column_count(), data_list):
            data = self.format.get_csv_formatted_data(data_list)
            with open(self.file_name, 'a') as file:
                for row in data:
                    file.write(row)
                print('File successfully updated.')

    def __get_column_count(self):
        with open(self.file_name, 'r') as file:
            headers = file.readline().split(',')
            return len(headers)
