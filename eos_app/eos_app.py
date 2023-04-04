import os
import json
import csv


def save_list_to_file(file_path: str, two_dim_list: str) -> None:
    # Convert the input string to a Python list using the JSON format
    try:
        two_dim_list = json.loads(two_dim_list)
    except json.JSONDecodeError:
        raise ValueError("The entered array is not in valid JSON format.")

    # Check if the output file already exists
    if os.path.exists(file_path):
        raise ValueError(f"The file '{file_path}' already exists.")

    # Validate that the input is a two-dimensional list of integers
    if not isinstance(two_dim_list, list) or not all(isinstance(row, list) for row in two_dim_list):
        raise ValueError("The entered array is not two-dimensional or in valid JSON format.")
    if not all(isinstance(val, int) for row in two_dim_list for val in row):
        raise ValueError("The entered array contains non-integer values.")

    # Determine the file format based on the file extension
    file_ext = os.path.splitext(file_path)[1].lower()
    if file_ext not in [".json", ".csv"]:
        raise ValueError(f"The file extension '{file_ext}' is unknown.")

    # Save the list to the output file using the appropriate format
    if file_ext == ".json":
        with open(file_path, "w") as f:
            json.dump(two_dim_list, f)
    elif file_ext == ".csv":
        with open(file_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(two_dim_list)
