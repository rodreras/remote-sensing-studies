from scipy import stats
from skimage.measure import regionprops_table, perimeter
import numpy as np
import pandas as pd

# Define custom features
def std(regionmask, intensity_img):
    vals = intensity_img[regionmask]
    std = np.std(vals)
    return std

def rectangularity(regionmask):
    return regionmask.sum()/regionmask.size

def compactness(regionmask):
    return 4*np.pi*regionmask.sum()/(perimeter(regionmask)**2 + 1e-6)  # small value added to avoid division by zero

def entropy_ndvi(regionmask, intensity_img):
    vals = intensity_img[regionmask]
    arr = stats.relfreq(vals, 100, defaultreallimits=(-1,1))[0]
    return stats.entropy(arr)

# Calculate set of various features for each segment
def calc_all_feats(seg_arr, img_arr):
    seg_arr = seg_arr.astype(np.int32)
    spectral_feats = pd.DataFrame(
        regionprops_table(
            label_image = seg_arr,
            intensity_image = img_arr,
            properties = ["label", "intensity_mean"],
            extra_properties=(std,)
        )
    )
    shape_feats = pd.DataFrame(
        regionprops_table(
            label_image = seg_arr,
            properties = ["solidity"],
            extra_properties=(rectangularity, compactness)
        )
    )

    textural_feats = pd.DataFrame(
        regionprops_table(
            label_image = seg_arr,
            intensity_image =img_arr[:, :, -1],  # Use only the NDVI band
            properties = [],
            extra_properties=(entropy_ndvi,)
        )
    )

    all_feats = pd.concat([spectral_feats, shape_feats, textural_feats], axis=1)

    return all_feats