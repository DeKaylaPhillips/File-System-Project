class Formatter:
    def get_csv_formatted_data(self, data_list):
        return list(map(lambda row: self.__csv_formatter(row), data_list))
    
    def get_csv_formatted_headers(self, headers_list):
        return self.__csv_formatter(headers_list)

    def __csv_formatter(self, data):
        return ','.join(data) + '\n'