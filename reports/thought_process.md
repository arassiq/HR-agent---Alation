# Description of my process building agent workflow

## 1. data_cleaning

### load_clean.py

- Building the data loading pipeline was straightforward, earlier refresher of pandas was extremeley useful
- Because I want to take this project a bit further, I want to make sure to properly compartmentalize all my functions
- While this isn't a ML problem, I am worried about how many entries we lost when de duping on email
- I had originally tried a vectorized way to change phone numbers before I realized I had to use .apply() which loops over all the data in the file
- Had to look up the correct syntax for splitting Department_Region, had forgotten to add the .str. and therefore string methods were not working
    - Had also forgotten to add expand leading to data to be saved as array and not a column
- Returning cleaned CSV path for later use with finding correct data

## 2. exploratory_analysis

### eda.py

- I want to eventually cluster to learn more about what's affecting performance score, I will have to do more research as it's been a while since i used k-means, but I think it could be insightful
- I ran into some problems when trying to derive the dtype of each column to seperate where we perform mean, median, etc., as well as problems when it came to outputting and formatting the outputs of each statistic in a clean way
- I tried to implement a sorted() portion to output values by uniqueness to show categorical variables last, yet, realized it would have been inneficient at runtime, as there were too many loops when outputted, and if this tool was scaled up to a larger dataset, there would be performance issues
- Decided to output statistics in a table for better visualization, and an easier view in markdown files.
- Had to give myself a quick refresher on how to aggregate in pandas for the calculated aggregates. Also searched on how to change the angle of x labels
- Because there is clear order between poor, average, good, excellent, I changed these to ordinal to use within a bar chart
- To be honest, I'm a bit nervous for using two bar charts, but due to the lack of time series data, I think this is the best choice, and the cleanest way to output our data

### clustering.py

- Looking to use KMeans to find a deeper understanding ofrelation between employee details and performance metrics
- Making sure to only use descriptive features: performance, Salary, date joined, remote work, yet scared about whether we have enough data to be descriptive enough
- Had to figure out how to turn date_joined to tenure, forgot datetime library methods, I feel this would be extremely important in performance to look for performance drop off over time
- Dissapointed to see that there is no clear elbow, yet change does slow down at 4 clusters
- No clear clustering on just performance, salary and tenure seems to affect clusters the largest with performance trailing behind

## 3. Agent creation

### query_agent.py

- Going to create an agent to query the cleaned data using pandas, and a agent to take that data, and an agent to call that agent and answer questions
- Will have to look into getting an agent to run code on my local machine 
- Going to use OpenAI Agents and use the function calling, need to remember to add the >OPENAI_API_KEY environment variable setting to the docs: export OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxx"
- Tool calling is going great, yet, instability when referencing the DB with self.