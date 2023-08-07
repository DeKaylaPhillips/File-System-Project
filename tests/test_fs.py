from src.file_system import FileSystem
from src.validator import Validator
from src.formatter import Formatter

mock_file_path = 'mockFile.csv'
mock_headers_list = ['Header1', 'Header2', 'Header3']
mock_data_list = [['Column1','Column2','Column3']]
mock_csv_content = 'Header1,Header2,Header3\nColumn1,Column2,Column3\n'
fs = FileSystem(mock_file_path, Validator, Formatter)
mock_open = lambda mocker: mocker.patch('builtins.open', mocker.mock_open(read_data=mock_csv_content))
mock_print = lambda mocker: mocker.patch('builtins.print')

def test_system_will_create_new_files_with_headers(mocker):
    mock_open_fn = mock_open(mocker)
    mock_file = mock_open_fn.return_value
    mock_print_fn = mock_print(mocker)
    mock_mode = 'w'
    headers = fs.format.get_csv_formatted_headers(mock_headers_list)
    fs.create_file(mock_headers_list)
    mock_open_fn.assert_called_once_with(mock_file_path, mock_mode)
    mock_print_fn.assert_called_once_with(mock_file.name)
    mock_file.write.assert_called_once_with(headers)

def test_system_will_read_data_from_a_file(mocker):
    mock_open_fn = mock_open(mocker)
    mock_print_fn = mock_print(mocker)
    mock_mode = 'r'
    fs.read_file()
    mock_open_fn.assert_called_once_with(mock_file_path, mock_mode)
    mock_print_fn.assert_called_once_with([['Header1', 'Header2', 'Header3'], ['Column1', 'Column2', 'Column3']])

def test_system_will_update_data_in_existing_files(mocker):
    mock_open_fn = mock_open(mocker)
    mock_file = mock_open_fn.return_value
    mock_mode = 'a'
    mock_csv_data_list = Formatter().get_csv_formatted_data(mock_data_list)
    fs.update_file(mock_data_list)
    mock_open_fn.assert_called_with(mock_file_path, mock_mode)
    with mock_open_fn(mock_file_path, 'a') as mock_file:
        for row in mock_csv_data_list:
            mock_file.write.assert_called_with(row)