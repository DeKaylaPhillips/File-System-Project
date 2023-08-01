from src.file_system import File_System

mock_file_path = 'mockFile.csv'
fs = File_System(mock_file_path)

def test_mock_create_file(mocker):
    mock_open_fn = mocker.patch('builtins.open', mocker.mock_open())
    mock_mode = 'x'
    fs.create_file()
    mock_open_fn.assert_called_once_with(mock_file_path, mock_mode)
    
