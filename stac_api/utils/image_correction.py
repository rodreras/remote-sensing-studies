import numpy as np
NAN_VALUE = -9999
def min_max_normalize(arr: np.ndarray) -> np.ndarray:
    """Wyvern L1B data is Top-of-Atmosphere Radiance. These values
    are out of the range that matplotlib is expecting. We need to scale
    our image values to 0-1 or 0-255. This function does this, as well
    as replacing the NaN value (-9999) with an actual NaN value.

    Args:
        arr (np.ndarray): Input array requiring scaling

    Returns:
        np.ndarray: Scaled output array w/ NaN's added
    """
    arr = np.where(arr == NAN_VALUE, np.nan, arr)
    # nanmin/nanmax ignore NaN values within an array while still calculating the value (max, min)
    return (arr - np.nanmin(arr)) / (np.nanmax(arr) - np.nanmin(arr))


