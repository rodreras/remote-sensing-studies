def ndvi_calc(red, nir):
    '''Normalized Difference Vegetation Index'''
    return (nir - red) / (nir + red)

def ndbi_calc(swir, nir):
    '''Normalized Difference Build Up Index'''
    return (swir - nir) / (swir + nir)