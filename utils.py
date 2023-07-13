# Prints Shape and Dtype For List Of Variables
def print_shape_dtype(l, names):
    for e, n in zip(l, names):
        print(f'{n} shape: {e.shape}, dtype: {e.dtype}')
        
        
# Get complete file path to file
def get_file_path(path):
    return f'{your_dataset_path}'