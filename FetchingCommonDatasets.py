# Source: Mueller, John Paul,"Functional Programming", for dummies, 2019

from sklearn.datasets import fetch_olivetti_faces
data = fetch_olivetti_faces()
print(data.images.shape)

import matplotlib.pyplot as plt
#%matplotlib inline
plt.imshow(data.images[1], cmap="gray")
plt.show()