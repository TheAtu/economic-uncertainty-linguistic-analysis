"""
zst_to_json.py

Converts a zst compressed file to JSON.

Author: Alfonso Sundblad
Version: 1.0.0
Last Update: 2024-1-13
"""

try:
    import subprocess
    subprocess_available = True
except ImportError:
    subprocess_available = False

def zst_to_json(zst_file: str, output_extension: str = '.json', remove_file: bool = False) -> None:
    """
    Convert a zst compressed file to JSON.

    Parameters:
    - zst_file (str): The input zst file.
    - output_extension (str): The extension for the output file (default is '.json').
    - remove_file (bool): If True, remove the original zst file after conversion (default is False).

    Raises:
    - subprocess.CalledProcessError: If the zstd command fails.

    Returns:
    - None

    Example:
    >>> # This example assumes a valid zst_file exists in the same directory
    >>> import os
    >>> test_zst_file = 'test_file.zst'
    >>> test_output_extension = '.json'
    >>> try:
    ...     zst_to_json(test_zst_file, output_extension=test_output_extension, remove_file=True)
    ...     assert os.path.exists(test_zst_file) == False  # File should be removed
    ...     assert os.path.exists(test_zst_file.replace('.zst', test_output_extension)) == True  # Output file should exist
    ... finally:
    ...     os.remove(test_zst_file.replace('.zst', test_output_extension))  # Clean up created files
    >>> print('Test passed!')

    """
    
    if not subprocess_available:
        raise ImportError("The 'subprocess' module is required for this functionality.")

    try:
        # Extracting the base name of the zst file without extension
        zst_name = zst_file.split('.zst')[0]
        
        # Constructing the output file name
        output_file = zst_name + output_extension
        
        # Run the zstd command to decompress the zst file to JSON
        subprocess.run(['zstd', '-d', '-o', output_file, zst_file], check=True)
        
        # Remove the original .zst file if specified
        if remove_file:
            subprocess.run(['rm', zst_file])
        
        print('Done!')
    except subprocess.CalledProcessError as e:
        print(f'Error during zst_to_json conversion: {e}')
