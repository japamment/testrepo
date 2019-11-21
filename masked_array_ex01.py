import numpy.ma as MA

# Create a masked array with a fill value of 999
marr=MA.masked_array(range(10), fill_value =999)

print(marr, marr.fill_value)
# [0 1 2 3 4 5 6 7 8 9] 999

# Mask third element of array
marr[2] = MA.masked

print(marr)
# [0 1 -- 3 4 5 6 7 8 9]

# Print the (Boolean) mask
print(marr.mask)
# [False False  True False False False False False False False]

# Make an array same as marr, but masked where VALUES are 7 or more
narr = MA.masked_where(marr > 6, marr)
print(narr)
# [0 1 -- 3 4 5 6 -- -- --]

print(narr.fill_value)
# 999
# So fill value has been copied from original array, along with masked values

x = MA.filled(narr)
print(x)
type(x)
# [  0   1 999   3   4   5   6 999 999 999]
# <class 'numpy.ndarray'>

