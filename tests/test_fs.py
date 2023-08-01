from src.file_system import FileSystem

mock_file_path = 'mockFile.csv'
fs = FileSystem(mock_file_path)
mockOpen = lambda mocker: mocker.patch('builtins.open', mocker.mock_open())
mockPrint = lambda mocker: mocker.patch('builtins.print')

def test_mock_create_file(mocker):
    mock_open_fn = mockOpen(mocker)
    mock_print_fn = mockPrint(mocker)
    mock_mode = 'w'
    fs.create_file()
    mock_open_fn.assert_called_once_with(mock_file_path, mock_mode)
    mock_print_fn.assert_called_once_with(fs.file.name)

def test_mock_read_file(mocker):
    mock_open_fn = mockOpen(mocker)
    mock_print_fn = mockPrint(mocker)
    mock_mode = 'r'
    fs.read_file()
    mock_open_fn.assert_called_once_with(mock_file_path, mock_mode)
    mock_print_fn.assert_called_once_with(fs.file.read())