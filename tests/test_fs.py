from src.file_system import FileSystem
from src.validator import Validator
from src.formatter import Formatter
import pytest

mock_file_path = 'mockFile.csv'
mock_headers_list = ['Header1', 'Header2', 'Header3']
mock_data_list = [['Column1','Column2','Column3']]
mock_csv_content = 'Header1,Header2,Header3\nColumn1,Column2,Column3\n'

@pytest.fixture
def mock_setup(mocker):
    mock_open_fn = mocker.patch('builtins.open', mocker.mock_open(read_data=mock_csv_content))
    mock_print_fn = mocker.patch('builtins.print')
    mock_file = mock_open_fn.return_value
    return mock_open_fn, mock_print_fn, mock_file

@pytest.fixture
def file_system():
    return FileSystem(mock_file_path, Validator, Formatter)

def test_system_will_create_new_files_with_headers(mock_setup, file_system):
    mock_open_fn, mock_print_fn, mock_file = mock_setup
    fs = file_system
    headers = fs.format.get_csv_formatted_headers(mock_headers_list)
    fs.create_file(mock_headers_list)
    mock_open_fn.assert_called_once_with(mock_file_path, 'w')
    mock_print_fn.assert_called_once_with(mock_file.name)
    mock_file.write.assert_called_once_with(headers)

def test_system_will_read_data_from_a_file(mock_setup, file_system):
    mock_open_fn, mock_print_fn, _ = mock_setup
    fs = file_system
    fs.read_file()
    mock_open_fn.assert_called_once_with(mock_file_path, 'r')
    mock_print_fn.assert_called_once_with([['Header1', 'Header2', 'Header3'], ['Column1', 'Column2', 'Column3']])

def test_system_will_update_data_in_existing_files(mock_setup, file_system):
    mock_open_fn, mock_print_fn, mock_file = mock_setup
    mock_csv_data_list = Formatter().get_csv_formatted_data(mock_data_list)
    fs = file_system
    fs.update_file(mock_data_list)
    for row in mock_csv_data_list:
        mock_file.write.assert_called_with(row)
    mock_open_fn.assert_called_with(mock_file_path, 'a')
    mock_print_fn.assert_called_once_with('File successfully updated.')