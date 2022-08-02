import pandas as pd

columns_li = ['experience',
              'test_score',
              'interview_score',
              'salary'
              ]

experience_li = [0, 0, 'five', 'two', 'seven', 'three', 'ten', 'eleven']
test_score_li = [9, 6, 7, 10, 6, 10, 7, 8]
interview_score_li = [9, 6, 7, 10, 6, 10, 7, 8]
salary_li = [50_000, 45_000, 60_000, 65_000, 70_000, 62_000, 72_000, 80_000]

assert len(experience_li) == len(test_score_li) ==\
       len(interview_score_li) == len(salary_li), 'Lengths do not match'

data = [experience_li, test_score_li, interview_score_li, salary_li]
hiring_df = pd.DataFrame(data).T
hiring_df.columns = columns_li

print(hiring_df.head(3))

hiring_df.to_csv(
    'hiring.csv',
    index=False
)

print('Table created')