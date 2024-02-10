'''
check_package_availability.py

A utility script to check the availability of required Python packages.

Author: Alfonso Sundblad
Version: 1.0.0
Last Update: 2024-1-13
'''

def check_package_availability(required_packages:list):
    '''
    Check the availability of required Python packages.

    Parameters:
    - required_packages (list): List of package names to check.

    Raises:
    - ImportError: If any of the required packages is not installed.

    Returns:
    - package_availability (dict): Dictionary indicating the availability of each package.
    '''
    global package_availability
    package_availability = {}
    missing = []

    # Check the availability of each required package
    for package in required_packages:
        try:
            __import__(package)
            package_availability[package] = True
        except ImportError:
            package_availability[package] = False
            missing.append(package)

    # Raise ImportError if any required package is missing
    if len(missing) == 1:
        raise ImportError(f'Package "{missing[0]}" is not installed. It is required for this functionality. \n To help debug, the variable "package_availability" was created with the available and missing packages')
    elif len(missing) >= 1:
        missing_packages_str = '", "'.join(missing)
        raise ImportError(f'Packages "{missing_packages_str}" are not installed. They are required for this functionality. \n To help debug, the variable "package_availability" was created with the available and missing packages')
    return True