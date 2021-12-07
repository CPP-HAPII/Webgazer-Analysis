import pandas as pd
from getAllPageFixations import *

fixationsList = []

for i in range(1, 31):

    allPageFixations = getAllPageFixations('../user5/user5Analysis/page{}/page{}AOI_fixations.csv'.format(i, i))
    fixationsList.append(allPageFixations)

fixationColumns = [
    'AOI1',
    'AOI2',
    'AOI3',
    'AOI4',
    'AOI5',
    'AOI6',
    'NOT AOI'
]
df = pd.DataFrame(fixationsList, columns=fixationColumns)
df.to_csv('../user5/user5Analysis/page_fixations.csv'.format(i, i), index=False)
