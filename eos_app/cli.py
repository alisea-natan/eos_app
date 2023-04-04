import click

from eos_app.eos_app import save_list_to_file


@click.command()
@click.argument('file_path', type=str)
@click.argument('two_dim_list', type=str)
def save_list(file_path, two_dim_list):
    """
    Saves a two-dimensional integer list to a JSON or CSV file.

    Args:
        file_path (str): The path to the file to be saved.
        two_dim_list (str): The two-dimensional integer list to be saved in string format.

    Raises:
        ValueError: If the entered file already exists, or the entered path has an unknown extension,
                    or the entered array is not two-dimensional integer.
    """
    save_list_to_file(file_path, two_dim_list)


if __name__ == '__main__':
    save_list()
