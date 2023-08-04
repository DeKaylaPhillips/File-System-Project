from src.file_system import FileSystem

mock_file_path = 'mockFile.csv'
mock_csv_data = 'Header1,Header2,Header3\nColumn1,Column2,Column3'
fs = FileSystem(mock_file_path)
mock_open = lambda mocker: mocker.patch('builtins.open', mocker.mock_open(read_data=mock_csv_data))
mock_print = lambda mocker: mocker.patch('builtins.print')

def test_mock_create_file(mocker):
    mock_open_fn = mock_open(mocker)
    mock_print_fn = mock_print(mocker)
    mock_mode = 'w'
    fs.create_file()
    mock_open_fn.assert_called_once_with(mock_file_path, mock_mode)
    mock_print_fn.assert_called_once_with(fs.file.name)

def test_mock_read_file(mocker):
    mock_open_fn = mock_open(mocker)
    mock_print_fn = mock_print(mocker)
    mock_mode = 'r'
    fs.read_file()
    mock_open_fn.assert_called_once_with(mock_file_path, mock_mode)
    mock_print_fn.assert_called_once_with([['Header1', 'Header2', 'Header3'], ['Column1', 'Column2', 'Column3']])