# https://colab.research.google.com/github/google/eng-edu/blob/main/ml/cc/exercises/numpy_ultraquick_tutorial.ipynb?utm_source=mlcc&utm_campaign=colab-external&utm_medium=referral&utm_content=mlcc-prework&hl=en#scrollTo=tG8ao9CsNqw8

import numpy as np

feature = np.arange(6, 21)
print(feature)
label = (3)*(feature) + 4
print(label)

floats = np.random.random([15])
integers = np.random.randint(low=-2, high=2, size=(15))
noise = floats + integers
print(noise)
label = label + noise
print(label)