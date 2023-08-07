from src.validator import Validator

amount_of_columns = 4
validate = Validator()

def test_returns_true_bool_if_data_input_is_valid():
    valid_data_input = [['TestColumn1', 'TestColumn2', 'TestColumn3', 'TestColumn4']]
    results = validate.is_valid_data_input(amount_of_columns, valid_data_input)
    assert results == True

def test_returns_false_bool_if_data_input_is_invalid():
    invalid_data_input = [['TestColumn1', 'TestColumn2', 'TestColumn3']]
    results = validate.is_valid_data_input(amount_of_columns, invalid_data_input)
    assert results is False