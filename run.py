from src.file_system import FileSystem 
from src.validator import Validator
from src.formatter import Formatter

fs = FileSystem('myFile.csv', Validator, Formatter)
fs.create_file(['ID', 'Program', 'Month', 'Budget'])
fs.update_file([['1', 'Program A', 'August', '30000'], ['2', 'Program B', 'August', '25000']])
