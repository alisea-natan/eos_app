# eos_app
`eos_app` is a Python package that provides the ability to store 
a two-dimensional integer list to a JSON or CSV file. 
It also includes a CLI interface that allows the user to enter 
the output file path and the two-dimensional list in string format.

## Installation
To install the package, you can use pip:
`pip install .`

## Usage

Using the CLI interface, you can easily use package from the command line:

`python3 -m eos_app.cli output.csv "[[1, 2], [3, 4, 5], [1]]"` - if package not installed

`eos-app output.json "[[1, 2], [3, 4]]"` - after the installation

## Options
The CLI interface accepts the following command line options:

* file_path: The path to the output file. This must be a string in the format "/path/to/output/file.csv" or "/path/to/output/file.json".
* two_dim_list: The two-dimensional integer list to be saved in string format. This must be a string in the format "[[1, 2], [3, 4]]".

## Exceptions
The save_list_to_file function raises a ValueError exception in the following cases:

* The entered file already exists.
* The entered file has an unknown extension.
* The entered array is not two-dimensional or in valid JSON format.
* The entered array contains non-integer values.

## Tests
For the tests is used pytest testing framework.
Command for launching tests:
`python3 -m pytest tests/tests.py ` 




### Additional Information and Future Improvements
The package is currently designed only for use with the `eos_app` command line tool and not for testing. Therefore, only the required packages for usage are included in the setup.py file.

If the project is expanded to include more functionality in the future, it may be beneficial to create separate configuration and utility files. These files would contain default values for the application and tests, as well as any repeated functions or code snippets. However, as the project is currently small in scope, there is no pressing need to separate this information.

While using type annotations is helpful, there are other checks that can provide additional opportunities for improving code quality. Separating these checks from the typing check also allows for clearer error messages to be displayed to the user.



