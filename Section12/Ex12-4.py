# 외부모듈 pandas를 이용하기

import pandas as pd
import numpy as np

# print(np.random.rand(5,5))
print(type(np.random.rand(5,5)))
print('=======')
df = pd.DataFrame(np.random.rand(5, 5))
print(df)
