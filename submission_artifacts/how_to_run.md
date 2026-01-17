# 1. Setup

Clone and enter the repository:

```bash
git pull
cd HR-agent---Alation
```

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Add the Dataset

Create a data directory:

```bash
mkdir -p data
```

Place the HR CSV file into:

```text
HR-agent---Alation/data/
```

## Set OpenAI API Key

Export your OpenAI API key as an environment variable:

```bash
export OPENAI_API_KEY="your_key_here"
```

# 2. Run Data Cleaning and Exploratory Data Analysis

From the project root, run the main script using the command-line interface.

### Run cleaning + EDA only (no clustering)

```bash
python part1.py --data-path data/HR.csv
```

This will:
- Load the uncleaned dataset
- Perform cleaning
- Save a cleaned version of the dataset
- Print preliminary and calculated EDA statistics to the console

### Run cleaning + EDA + clustering

To additionally run KMeans clustering, include the `--cluster` flag:

```bash
python part1.py --data-path data/HR.csv --cluster
```

This will:
- Perform all cleaning and EDA steps
- Run KMeans clustering on the cleaned dataset
- Output cluster summaries to the console


# 3. Run Agent on Clean Data

Run the HR question‑answering agent from the command line.  
By default, the agent assumes the data has already been cleaned.

### Run agent on already‑cleaned data (default)

If you already have a cleaned dataset at the default location:

```bash
python part2.py
```

This will:
- Automatically use `data/Employee_dataset_cleaned.csv`
- Skip the data cleaning step
- Launch the interactive HR agent

No flags or paths are required for this case.

### Run agent and clean data first

If your dataset is messy and needs to be cleaned, provide the path and include the `--clean` flag:

```bash
python part2.py --data-path "data/Employee_dataset.csv" --clean
```

This will:
- Clean the raw dataset located at `--data-path`
- Use the cleaned output for the agent
- Launch the HR agent

