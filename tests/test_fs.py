from src.file_system import FileSystem

mock_file_path = 'mockFile.csv'
fs = FileSystem(mock_file_path)

def test_mock_create_file(mocker):
    mock_open_fn = mocker.patch('builtins.open', mocker.mock_open())
    mock_print_fn = mocker.patch('builtins.print')
    mock_mode = 'w'
    fs.create_file()
    mock_open_fn.assert_called_once_with(mock_file_path, mock_mode)
    mock_print_fn.assert_called_once_with(fs.file.name)
