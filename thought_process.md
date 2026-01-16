# Description of my process building agent workflow

## 1. data_cleaning
### load_clean.py
- Building the data loading pipeline was straightforward, earlier refresher of pandas was extremeley useful
- Because I want to take this project a bit further, I want to make sure to properly compartmentalize all my functions
- I had originally tried a vectorized way to change phone numbers before I realized I had to use .apply() which loops over all the data in the file
- Had to look up the correct syntax for splitting Department_Region, had forgotten to add the .str. and therefore string methods were not working
    - Had also forgotten to add expand leading to data to be saved as array and not a column
- Returning cleaned CSV path for later use with finding correct data

### exploratory_analysis.py