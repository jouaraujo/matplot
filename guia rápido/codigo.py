#%% 

import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl

# %%
fig, ax = plt.subplots() # Cria uma figura contendo apenas eixos

#%%
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [1, 4, 2, 3]) # plota alguns dados nos eixos

#%%
# A maneira mais fácil de criar uma nova figura é com pyplot
fig = plt.figure() # uma figura vazia sem eixos
fig, ax = plt.subplots() # uma figura só com eixos
fig, axs = plt.subplots(2, 2) # uma figura 2x2
fig, axs = plt.subplot_mosaic([["left", "right_top"],
                               ["left", "right_bottom"]]) # uma figura na esquerda e duas a direita

#%%
b = np.matrix([[1, 2], [3, 4]])
b_asarray = np.asarray(b)

#%%
np.random.seed(19680801)  # seed the random number generator.
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.scatter('a', 'b', c='c', s='d', data=data)
ax.set_xlabel('entry a')
ax.set_ylabel('entry b')