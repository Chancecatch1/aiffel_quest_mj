import deepchem as dc
import numpy as np

tox21_tasks, tox21_datasets, transformers = dc.molnet.load_tox21()
print(tox21_tasks)
