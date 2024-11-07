import os

# Update the FILEPATH to an absolute path
FILEPATH = os.path.join(os.path.dirname(__file__), 'todos.txt')

def get_todos(filepath=None):
    """
    Reads the contents of a file and returns a list of todos.

    Args:
        filepath (str): The path to the file.

    Returns:
        list: A list of todos read from the file.
    """
    if filepath is None:
        filepath = FILEPATH

    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return []
    
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_local, filepath=None):
    """
    Write the given todos to the specified file.

    Args:
        filepath (str): The path of the file to write the todos to.
        todos_local (list): A list of todos to write to the file.

    Returns:
        None
    """
    if filepath is None:
        filepath = FILEPATH

    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_local)

if __name__ == '__main__':
    '''makes sure that the code is only run when the file is run directly'''
    print('hello from functions')