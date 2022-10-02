import pytest
import numpy as np

# from src.models.train import split_into_training_and_testing_sets
from models.train import split_into_training_and_testing_sets

class TestSplitIntoTrainingAndTestingSets(object):

    def test_on_six_rows(self):
        
        example_argument = np.array([[2081.0, 314942.0], [1059.0, 186606.0],
                                    [1148.0, 206186.0], [1506.0, 248419.0],
                                    [1210.0, 214114.0], [1697.0, 277794.0]]
                                    )
        
        expected_training_array_num_rows = 4
        expected_testing_array_num_rows = example_argument.shape[0] - int(0.75*example_argument.shape[0])
        
        actual = split_into_training_and_testing_sets(example_argument)
        
        assert actual[0].shape[0] == expected_training_array_num_rows, f"The actual number of rows in the training array is not {expected_training_array_num_rows}"
        assert actual[1].shape[0] == expected_testing_array_num_rows, f"The actual number of rows in the testing array is not {expected_testing_array_num_rows}"
        
    def test_value_error_on_one_dimensional_argument(self):
        
        example_argument = np.array([2081, 314952, 1045, 1239185, 230353])
        
        with pytest.raises(ValueError) as exception_info:
            split_into_training_and_testing_sets(example_argument)
            
        assert exception_info.match("Argument data_array must be two dimensional. Got 1 dimensional array instead!")
        
    def test_on_one_row(self):
        
        test_argument = np.array([[1392.0, 123125.0]])
        
        with pytest.raises(ValueError) as exc_info:
            split_into_training_and_testing_sets(test_argument)
            
        expected_error_message = "Argument data_array must have at least 2 rows, it actually has just 1"
        
        assert pytest.raises(ValueError)