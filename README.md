# HR Agent – Results and Usage

This file documents how to run the project and where to find the results that were generated.

## Submission Artifacts

This repository contains all required submission artifacts:

1. *Instructions on how to run the project, how to run the agent* 
   - See `submission_artifacts/how_to_run.md` (How to Run section)

2. *Cleaned output data from Part 1*  
   - `submission_artifacts/cleaned_hr_data.csv`

3. *Output from Part 1 EDA tasks*  
   - `submission_artifacts/part1_results.md`

4. *Output from Part 2 questions*  
   - Included in `submission_artifacts/part2_results.md`

5. *Demo video*  
   - Provided in submission email

## How to Run the Project (main pipeline)

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

## Run the Pipeline

From the project root, run:

```bash
python HR-agent---Alation/run_dataloading_eda.py
```

This script:
- loads the HR dataset
- runs exploratory data analysis (EDA)
- generates summary tables and plots
- runs an OpenAI-powered agent over the data

## Outputs and Analysis

For personal results, read the following file:

- `HR-agent---Alation/reports/thought_process.md`
  - Notes on design decisions and the overall approach used to build the pipeline

