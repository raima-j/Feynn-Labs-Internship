import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer
pd.options.mode.chained_assignment = None  # 'warn' or 'raise'
from bioinfokit.visuz import cluster
from sklearn.decomposition import PCA