class Validator:
    def is_valid_data_input(self, amount_of_columns, data_list):
        invalid_data_list = list(
            filter(lambda row: len(row) != amount_of_columns, data_list)
        )
        return len(invalid_data_list) == 0