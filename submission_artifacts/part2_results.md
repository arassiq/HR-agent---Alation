# Agent Queries and Results:

## 1.
### Query:

#### *Which Region(s) offer the highest salary to employees on average?*

### Agent Output:
Answer: Illinois offers the highest average salary to employees, with an average salary of 94,400.11.

Evidence:
| Region      | Salary        |
|-------------|---------------|
| Illinois    | 94400.111111  |
| Texas       | 87022.666667  |
| Florida     | 86901.666667  |
| Nevada      | 81318.666667  |
| New York    | 79266.363636  |
| California  | 78385.153846  |

QueryUsed: df.groupby('Region', as_index=False)['Salary'].mean().sort_values('Salary', ascending=False) 


## 2.
### Query:

#### *Show me a list of top performers in each department?*

### Agent Output:

Answer: The top performers in each department are:
Admin: Frank Davis (Excellent)
Cloud Tech: Charlie Garcia (Excellent)
DevOps: Charlie Johnson (Excellent)
Finance: Bob Brown (Excellent)
HR: Heidi Williams (Excellent)
Sales: Bob Williams (Excellent)

Evidence:

  | Department   | First_Name | Last_Name | Performance_Score |
|--------------|------------|-----------|-------------------|
| Admin        | Frank      | Davis     | Excellent         |
| Cloud Tech   | Charlie    | Garcia    | Excellent         |
| DevOps       | Charlie    | Johnson   | Excellent         |
| Finance      | Bob        | Brown     | Excellent         |
| HR           | Heidi      | Williams  | Excellent         |
| Sales        | Bob        | Williams  | Excellent         |

QueryUsed: df.assign(_rank=df['Performance_Score'].map({'Excellent': 4, 'Good': 3, 'Average': 2, 'Poor': 1})).sort_values(['Department','_rank'], ascending=[True,False]).groupby('Department').head(1)[['Department','First_Name','Last_Name','Performance_Score']].reset_index(drop=True) 

## 3.
### Query:

#### *Show me a list of the most tenured employees in each department?*

### Agent Output:

Answer: The most tenured employees in each department are:
Admin: Charlie Williams (Join Date: 2020-01-02)
Cloud Tech: David Miller (Join Date: 2020-04-30)
DevOps: Eva Miller (Join Date: 2020-01-21)
Finance: Eva Brown (Join Date: 2020-07-08)
HR: Bob Miller (Join Date: 2021-05-08)
Sales: Alice Garcia (Join Date: 2020-06-10)

Evidence:

| Department   | First_Name | Last_Name | Join_Date   |
|--------------|------------|-----------|-------------|
| Admin        | Charlie    | Williams  | 2020-01-02  |
| Cloud Tech   | David      | Miller    | 2020-04-30  |
| DevOps       | Eva        | Miller    | 2020-01-21  |
| Finance      | Eva        | Brown     | 2020-07-08  |
| HR           | Bob        | Miller    | 2021-05-08  |
| Sales        | Alice      | Garcia    | 2020-06-10  |

QueryUsed: df.assign(Join_Date=pd.to_datetime(df['Join_Date'])).sort_values('Join_Date').groupby('Department').first().reset_index()[['Department', 'First_Name', 'Last_Name', 'Join_Date']].sort_values('Department')