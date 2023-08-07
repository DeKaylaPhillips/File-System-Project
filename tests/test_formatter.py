from src.formatter import Formatter

format = Formatter()
test_headers = ['Header1', 'Header2', 'Header3']
test_data = [['TestData1', 'TestData2', 'TestData3']]

def test_will_return_headers_as_csv_string():
    csv_headers = format.get_csv_formatted_headers(test_headers)
    assert csv_headers == 'Header1,Header2,Header3\n'
    
def test_will_return_data_as_list_of_csv_strings():
    csv_data = format.get_csv_formatted_data(test_data)
    assert csv_data == ['TestData1,TestData2,TestData3\n']