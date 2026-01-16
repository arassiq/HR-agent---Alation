from agents import Agent, Runner, function_tool
import pandas as pd
import asyncio


class QueryAgent:
    def __init__(self, cleaned_data="data/Employee_dataset_cleaned.csv"):
        self.data = pd.read_csv(cleaned_data)

        @function_tool
        def query_db(pandas_code: str):
            if "df" not in pandas_code:
                return "Error: pandas code must reference df"

            #print("\n[query_db] Executing:", pandas_code)
            safe = {
                "df": self.data,
                "pd": pd,
            }
            #run pandas code while making sure to switch df and pd to their respective commands
            result = eval(pandas_code, safe, {})

            #format df to string for output to agent
            return result.to_string(index=False)


        self.query_db = query_db

        self.agent = Agent(
            name="Analyst Agent",
            instructions=f"""
                You are a data query agent.
                Your job is to answer user questions by querying a CSV-backed pandas DataFrame.

                The DataFrame is already loaded and available as df
                The DataFrame schema matches the output of: {self.data.head()},
                including column names and data types.

                To answer a question, you must:
                    •	Translate the question into a single valid pandas expression
                    •	Call the provided tool with that expression
                    •	Use only df to reference the data
                    •	Use the tools results to return a valid answer

                Do not import libraries, assign variables, or include explanations.
                Do not make assumptions beyond the DataFrame’s columns and types.
                All data access must occur through the tool call.
                Shortly reference data you used to come to your conclusion and the numbers as a result of your query you used to derive your answer
            """,
            tools=[self.query_db],
        )
    

    async def run_agent(self, question):
        result = await Runner.run(self.agent, input=question)
        return result.final_output
