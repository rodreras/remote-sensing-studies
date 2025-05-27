'''
Functions to improve image visualization 
'''
import numpy as np

def normalize(band):
    band_min, band_max = (band.min(), band.max())
    return ((band - band_min)/((band_max - band_min)))

def brighten(band, alpha = 0.13, beta = 0):
    alpha=0.13
    beta=0
    return np.clip(alpha*band+beta, 0,255)

def gammacorr(band, gamma = 2):
    gamma=2
    return np.power(band, 1/gamma)

def stretch_histogram(band, min_out=0, max_out=255):
    min_in, max_in = np.percentile(band, (2, 98))  # Considerando 2% - 98% para evitar outliers
    stretched = (band - min_in) * ((max_out - min_out) / (max_in - min_in)) + min_out
    stretched = np.clip(stretched, min_out, max_out)
    return stretched