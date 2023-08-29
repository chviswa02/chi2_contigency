# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 11:03:57 2023

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 10:32:54 2023

@author: user
"""

import numpy as np
from scipy.stats import chi2_contingency
A=np.array([[1,2],[7,10]])

chi2_stat, p_value , dof, expected = chi2_contingency(A)
if p_value < 0.05:
    print("Reject the NULL Hypothesis: There is significant association between variable")
else:
    print("Fail to reject NULL Hypothesis")

