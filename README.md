# HR Agent – Results and Usage

This file documents how to run the project and where to find the results that were generated.

## How to Run the Project

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

For personal results, read the following files:

- `HR-agent---Alation/reports/agent_results.md`
  - Results and outputs returned by the agent

- `HR-agent---Alation/reports/eda_results.md`
  - EDA tables, plots, and high-level observations

- `HR-agent---Alation/reports/thought_process.md`
  - Notes on design decisions and the overall approach used to build the pipeline

These files together document both the analysis results and the reasoning behind the implementation.
