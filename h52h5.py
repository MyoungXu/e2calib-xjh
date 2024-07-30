import h5py
from pathlib import Path
import hdf5plugin
import numpy as np


def copy_events_datasets_to_new_h5(source_h5_path: Path, target_h5_path: Path):
    assert source_h5_path.is_file(), f"Source HDF5 file {source_h5_path} does not exist."
    with h5py.File(source_h5_path, 'r') as source_h5f:
        # Ensure the 'events' group exists in the source file
        if 'events' in source_h5f:
            events_group = source_h5f['events']
            with h5py.File(target_h5_path, 'w') as target_h5f:
                # Iterate through items in the 'events' group
                for name, dataset in events_group.items():
                    data = dataset[...]
                    # Check if the dataset is of type <u4 and convert it to <i8
                    if data.dtype == np.dtype('<u4'):
                        data = data.astype('<i8')
                        print(f"Converted dataset '{name}' from <u4 to <i8>")
                    else:
                        print(f"Dataset '{name}' is of type {data.dtype} and was copied without conversion.")

                    # Copy the dataset to the root of target file
                    target_h5f.create_dataset(name=name, data=data)

        else:
            print(f"No 'events' group found in the source file {source_h5_path}.")


# Example usage
source_h5_file = Path(r"C:\Users\11093\Desktop\events.h5")  # Replace with your source file path
target_h5_file = Path('h5data/event.h5')  # Replace with your target file path
copy_events_datasets_to_new_h5(source_h5_file, target_h5_file)







