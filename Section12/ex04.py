# 외부 모듈
# pip 명령어는 명령프롬프트 창에서 실행해야 한다.
'''
pip --help
pip list
pip show numpy
pip install numpy
'''

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.rand(5, 5))
print(df)
