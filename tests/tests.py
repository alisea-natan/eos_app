import os
import json
import csv
import pytest
from tempfile import NamedTemporaryFile

from eos_app.eos_app import save_list_to_file


@pytest.mark.parametrize('data', [[[1, 2], [3, 4]]])
def test_save_list_to_file_json(tmpdir, data):
    # test that the function saves a two-dimensional integer list to a JSON file correctly.
    expected_file_path = os.path.join(tmpdir, "output.json")

    save_list_to_file(expected_file_path, json.dumps(data))

    with open(expected_file_path, "r") as f:
        assert json.load(f) == data


@pytest.mark.parametrize('data', [[[1, 2], [3, 4]]])
def test_save_list_to_file_csv(tmpdir, data):
    # test that the function saves a two-dimensional integer list to a CSV file correctly.
    expected_file_path = os.path.join(tmpdir, "output.csv")

    save_list_to_file(expected_file_path, json.dumps(data))

    with open(expected_file_path, "r") as f:
        reader = csv.reader(f)
        assert [[int(val) for val in row] for row in reader] == data


@pytest.mark.parametrize('data', [[[1, 2], [3, 4]]])
def test_save_list_to_file_file_already_exists(tmpdir, data):
    # test that the function raises a ValueError if the entered file already exists.
    with NamedTemporaryFile(delete=False, dir=tmpdir) as tmp_file:
        tmp_file_path = tmp_file.name

    try:
        save_list_to_file(tmp_file_path, json.dumps(data))
    except ValueError as e:
        assert str(e) == f"The file '{tmp_file_path}' already exists."
    else:
        assert False, "Expected ValueError was not raised."


@pytest.mark.parametrize('data', [[[1, 2], [3, 4]]])
def test_save_list_to_file_invalid_extension(tmpdir, data):
    # test that the function raises a ValueError if the entered path has an unknown extension
    invalid_file_path = os.path.join(tmpdir, "output.txt")

    try:
        save_list_to_file(invalid_file_path, json.dumps(data))
    except ValueError as e:
        assert str(e) == f"The file extension '.txt' is unknown."
    else:
        assert False, "Expected ValueError was not raised."


@pytest.mark.parametrize('output', ["[1, 2, 3]", "[1, 2, [2, 3]]"])
def test_save_list_to_file_invalid_input_dimension(tmpdir, output):
    # Test that the function raises a ValueError if the entered array is one-dimensional or nested.
    with pytest.raises(ValueError, match=r"The entered array is not two-dimensional or in valid JSON format."):
        save_list_to_file(os.path.join(tmpdir, "output.json"), output)


@pytest.mark.parametrize('data', ["not a valid JSON string"])
def test_save_list_to_file_invalid_input_json(tmpdir, data):
    # Test that the function raises a ValueError if the entered array is not in valid JSON format.
    with pytest.raises(ValueError, match=r"The entered array is not in valid JSON format."):
        save_list_to_file(os.path.join(tmpdir, "output.json"), data)


@pytest.mark.parametrize('output', ['[[1, 2], [3, "4"]]', '[[1, 2], [3, 4.5]]'])
def test_save_list_to_file_invalid_input_type(tmpdir, output):
    # Test that the function raises a ValueError if the entered array contains non-integer values (string or float).
    with pytest.raises(ValueError, match="The entered array contains non-integer values."):
        save_list_to_file(os.path.join(tmpdir, "output.json"), output)
