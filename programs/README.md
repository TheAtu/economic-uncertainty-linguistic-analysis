## Program Folder 

The `programs` folder is structured to maintain a clean and organized environment for your project. Here are the main directories:

- **00-utilities:** Utility scripts and modules that provide common functions and helpers. Take into account that there is also a package been done just for this thesis.

- **01-data_processing:** Scripts related to the processing of raw data, both including economic factors and NLP or general data handling.

- **02-analysis:** Programs for in-depth analysis, utilizing the preprocessed data.

- **98-tests:** Unit tests and validation scripts to ensure the correctness of your code.

- **99-tmp:** Temporary scripts, experiments, or work in progress that hasn't been categorized yet. Naming convention is essential here.

### FileType: when to use JupyterNotebook(.ipynb) vs Pure Python(.py)

- **Jupyter Notebooks (.ipynb):**
  - Use for exploratory analysis, visualization, and iterative development.
  - Ideal for interactive data exploration, data visualization, and step-by-step code execution.
  - Well-suited for sharing analyses with visualizations and narrative explanations.
  - +Compatible: Analysis, Test, Tmp.
  - -Compatible: Data Processing, Utilities.


- **Pure Python Scripts (.py):**
  - Use for modular, automation and reusable code. Or generic code just run once.
  - Recommended for functions, classes, and scripts that are part of the overall project structure.
  - Suitable for running scripts from the command line or integrating into larger workflows.
  - +Compatible: Data Processing, Utilities, Test.
  - -Compatible: Analysis, Tmp.

Choose the file type based on the nature of the task, keeping in mind the benefits of each for specific stages of your project.

### Naming Convention:
• Always use **lower case** </br>
• Try using non-conjugated words and their singular version.</br>
• Try to avoid, but if space is needed, use: `_`_(underline)_</br>
• Separate each of the following sections with a `-`_(hyphen)_:</br>
- `{date}`: Date of processing (helpful for versioning, format yyyymmdd).
- `{process}`: Brief description of the process applied.
- `{version_number}`: [OPTIONAL] Sequential version number, useful for tracking changes over time. (format: v001)
- `{data_application}`: Note `u` for universal if is irrelevant the source of data. If it is important to note that is applied to reddit(`r`), youtube(`y`), or newspapers(`n`), or a combination of them.
- `{extension}`: File extension (e.g., ipynb, py, .txt). This section is not separated by `-`_(hypen)_, as it is the extension it uses `.`_(dot)_.

Composition:
```
{date}-{process}-{version_number}-{data_application}.{extension}
```
Example:
```
20240101-zst_to_json-v001-r.py
```
### Other Considerations
 - Write a brief summary at the start of the file, explaining it.
 - Use notes to explain functions and processes. 
 - Take into account that this programs will likely be needed linked to the data to explain the processes applied to them.