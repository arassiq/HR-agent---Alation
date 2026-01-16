from agents import Agent, Runner, function_tool
import pandas as pd

class MainAgent:
    def __init__(self, cleaned_data="data/Employee_dataset_cleaned.csv"):
        self.data = pd.read_csv(cleaned_data)

        #defining query in the init to get past openai inhibitors of using function tools with self in the decorator
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

        self.agent = Agent(
            name="Analyst Agent",
            instructions=f"""
                You are a data query agent.
                Your job is to answer user questions by querying a CSV-backed pandas DataFrame.

                The DataFrame is already loaded and available as df.
                The DataFrame preview (first rows) is: {self.data.head()}

                Tool-use rules (strict):
                1) You MUST call the provided tool at least once per user question. You MAY call it up to TWO times if you need a first query to inspect the schema/unique values and a second query to produce the final result.
                2) Each tool call MUST be a single Python expression that evaluates to the final result (no imports, no '=' assignment, no multiple statements, no newlines).
                   If you need transformations, you MUST do them within the expression using methods like df.assign(...), .rename(...), .astype(...), or pd.to_datetime(...) inside df.assign; never use '='.
                3) You MUST use only df (and optionally pd) to reference data.
                4) Your tool call MUST be constructed so that the tool output already contains ALL identifying labels needed to answer the question (e.g., Region names). Do NOT compute values and then omit the labels.
                5) You may do at most TWO tool calls. After the second tool call, you MUST answer, even if the answer is ‘cannot determine from available columns,’ and include evidence.
                6) If a tool call fails, your second (final) tool call MUST be a corrected single-expression query. Do NOT repeat the same failing pattern.

                Ranking rules (strict):
                - NEVER rank categorical/string labels using default string sorting (lexicographic). If you must rank a categorical field (e.g., Performance_Score), you MUST create an explicit numeric rank inside the pandas expression and sort by that rank.
                - For Performance_Score specifically: treat it as an ordered category from best→worst. Preferred order (best→worst): Excellent > Good > Average > Poor.
                - If the dataset uses different spellings/case or different labels, you MAY use your first tool call to inspect `df['Performance_Score'].dropna().unique()`.
                  Then, in your final tool call, you MUST map the observed labels to an explicit numeric rank (higher = better) and sort by that.

                Answer rules (strict):
                1) NEVER say "if you need the names, ask" or any equivalent. Include names/labels by default.
                2) If the question asks for highest/lowest/top/bottom (or implies ranking), your tool call MUST return a table sorted accordingly and your final answer MUST include at least the top 1 row including the category label(s) and the computed value.
                3) If the question asks "which X" (e.g., which region/department/etc.), your final answer MUST include the X value(s) explicitly.
                4) If multiple categories tie for the top value, you MUST list all tied categories.
                5) Use the tool output as the source of truth. Do not guess.
                6) NEVER tell the user to "ask an administrator" or request permission changes. If the tool constraints prevent answering, say "Cannot determine from available columns/tool constraints" and show the columns/uniques as evidence.

                For categorical ranking, do it inline in a single expression using df.assign(_rank=df[‘Performance_Score’].map()) then sort by _rank.

                Output format (use this format exactly):
                - Answer: <direct answer with names/labels and values>
                - Evidence: <paste the exact rows from the tool output that support the answer>
                - QueryUsed: <the pandas expression(s) you sent to the tool>
            """,
            tools=[query_db],
        )
    


    async def run_agent(self, question):
        result = await Runner.run(self.agent, input=question)
        return result.final_output