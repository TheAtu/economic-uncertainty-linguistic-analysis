## Data

This directory contains raw and processed data fo this proyetct. The data is organized into folders based on source and processing stages.

### Folder Structure

- **00-Raw:** Contains the raw data from different sources.
  - `Reddit/`: Raw data from Reddit.
  - `News/`: Raw data from news sources.
  - `YouTube/`: Raw data from YouTube.

- **01-NLP_Preprocessing:** _Intermediate processing for NLP and general data handling._ <br/> 
It Contains each significant step of the processing using the naming condition, if the data is dissagregated (for the characteristic of the step) it will contain tree subfolders for the three sources stated above, otherwise if not needed then it will be obviated.

- **02-Economics_Preprocessing:** Intermediate processing specific to economic analysis.<br/>
  It follows the same rules as the section above

- **03-Final:** Contains only data that is relevant and will not be further processed or analysed.

- **99-Auxiliar:** Contains data that is not categorizable to the previous distribution, mainly auxiliary files or data. i.e: dictionary of Spanish LIWC. It should not be data that will be processed.  

### Naming Convention
• Always use **lower case** </br>
• Try using non-conjugated words and their singular version.</br>
• Try to avoid, but if space is needed, use: `_`_(underline)_</br>
• Separate each of the following sections with a `-`_(hyphen)_:</br>
- `{source}`: Identifier for the data source(reddit, etc.)
- `{date}`: Date of processing (helpful for versioning, format yyyymmdd).
- `{process_applied}`: Brief description of the process applied.
- `{step_number}`: [OPTIONAL] Sequential step number during processing, only if there are more than one version.
- `{extension}`: File extension (e.g., csv, json). This section is not separated by `-`_(hypen)_, as it is the extension it uses `.`_(dot)_.

Composition:
```
{source}-{date}-{process_applied}-{step_number}.{extension}
```
Example:
```
reddit-20240101-zst_to_json.json
```

### Applied Processes:
| Process ID | Process Name | Description | Useful IntraLinks |
|---|---|---|---|
| filetype_conversion_01 | Zst to JSON File Type Convertion | It is self-explanotory, conversion of zst compressed file to json for ease of use later on. | ../programs/yt.ipynb#zst_to_json |
|  |  |  |  |
|  |  |  |  |