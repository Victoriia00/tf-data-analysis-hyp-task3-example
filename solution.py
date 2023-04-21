import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

chat_id = 1099505768 # Ваш chat ID, не меняйте название переменной
## Воспользуемся T-test (дисперсия и матожидания конечны)
def solution(x, y):
    res = ttest_ind(x, y, equal_var=False, alternative='two-sided')
    return res.pvalue < 0.06
