import pytest
# from tests.data.preprocessing_helpers import row_to_list, convert_to_int
from data.preprocessing_helpers import convert_to_int, row_to_list

class TestRowToList(object):
            
    def test_on_no_tab_no_missing_value(self):
        
        actual = row_to_list('123\n')
        assert actual is None, "Expected: None, Actual: {0}".format(actual)
        
    def test_on_two_tabs_no_missing_value(self):
        
        actual = row_to_list("123\t4,57\t89\n")
        
        assert actual is None, "Expected: None, Actual: {0}".format(actual)
        
    def test_on_one_tab_with_missing_value(self):
        
        actual = row_to_list("\t4,567\n")
        
        assert actual is None, "Expected: None, Actual: {0}".format(actual)
        
    def test_on_no_tab_with_missing_value(self):
        
        actual = row_to_list('\n')
        assert actual is None, "Expected: None, Actual {0}".format(actual)
        
        
    def test_on_two_tabs_with_missing_value(self):
        
        actual = row_to_list('123\t\t89\n')
        assert actual is None, "Expected: None, Actual {0}".format(actual)

    def test_on_normal_argument_1(self):
        
        actual = row_to_list('123\t4,567\n')
        expected = ['123', '4,567']
        
        assert actual == expected, 'Expected: {0}, Actual: {1}'.format(expected, actual)
        
class TestConvertToInt(object):

    def test_on_string_with_one_comma(self):
        
        test_argument = "2,081"
        expected = 2081
        actual = convert_to_int(test_argument)
        
        message = "convert_to_int('2,081') should return the int 2081, but it actually returned {0}".format(actual)
        
        assert isinstance(actual, int), 'actual value is not of type int'
        assert actual == expected, message
        
    def test_with_no_comma(self):
        actual = convert_to_int("756")
        # Complete the assert statement
        assert actual == 756, "Expected: 756, Actual: {0}".format(actual)
        
    def test_with_one_comma(self):
        actual = convert_to_int("2,081")
        # Complete the assert statement
        assert actual == 2081, "Expected: 2081, Actual: {0}".format(actual)
        
    def test_with_two_commas(self):
        actual = convert_to_int("1,034,891")
        # Complete the assert statement
        assert actual == 1034891, "Expected: 1034891, Actual: {0}".format(actual)
