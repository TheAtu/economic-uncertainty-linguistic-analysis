"""
json_split_to_chunks.py

Converts a JSON file into chunks.

Author: Alfonso Sundblad
Version: 1.0.0
Last Update: 2024-1-13
"""
required_packages = ['json', 'os']  # Add more package names as needed
def check_package(required_packages=[]):
  package_availability = {}
  missing = []
  for package in required_packages:
      try:
          __import__(package)
          package_availability[package] = True
      except ImportError:
          package_availability[package] = False

  for package, available in package_availability.items():
    if not available:
      missing.append(package)

  if len(missing) == 1:
    raise ImportError(f'Package "{missing[0]}" is not installed. It is required for this functionality. \n To help debug the variable "package_availability" was created with the abveilable and missing packages')
  elif len(missing) >= 1:
    missing_packages_str = '", "'.join(missing)
    raise ImportError(f'Package "{missing_packages_str}" are not installed. They are required for this functionality \n To help debug the variable "package_availability" was created with the abveilable and missing packages')

def json_split_to_chunks(input_file, output_folder=None, lines_per_chunk = 1000, output_folder_format='{input_file_name}-split',chunk_format='chunk-{nro}'):
  '''
  comment
  '''
  
  input_file_name, input_file_extension = os.path.splitext(input_file)
  if input_file_extension != '.json':
    raise ValueError('Input file must have a ".json" extension, but got:'+input_file_extension)

  # Check if there is a specific output folder determined, if not default
  if not output_folder:
    OUTPUT_FOLDER_PATH = os.path.join(input_file_name, '-split')
  else:
      OUTPUT_FOLDER_PATH = output_folder

  # Check if the output folder exists, create if not
  os.makedirs(OUTPUT_FOLDER_PATH, exist_ok=True)

  with open(input_file, "r") as infile:
    data = []
    chunk_count = 1
    CHUNK_NAME = chunk_format #incomplete

    def save_chunk():
      with open(os.path.join(OUTPUT_FOLDER_PATH, CHUNK_NAME), "w") as outfile:
        for item in data:
          json.dump(item, outfile)
          outfile.write("\n")

    for line in infile:
      data.append(json.loads(line))

      if len(data) == lines_per_chunk:
        save_chunk() 
        data = []
        chunk_count += 1

    # Write the last chunk
    save_chunk()


#test if packages are imported
  #open file input
    #check if its json file and other common errors
  #read line by line
  #when =1000 save to outputfolder
    #check output folder exists, if not make it.
  #return paths/ comment

