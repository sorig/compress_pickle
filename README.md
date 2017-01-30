# Functions to read/write to/from gzipped pickle files and tar archives

## Examples

### Pickle, compress and write object to disk

```
compress_pickle.to_gz_pickle(my_obj, 'my_obj.pickle.gz')
```

### Uncompress and load compressed pickle file

```
my_obj = compress_pickle.read_gz_pickle('my_obj.pickle.gz')
```

### List pickle files in a tar archive:

```
import compress_pickle

compress_pickle.list_tar_file_contents('myarchive.tar.gz', '.*pickle')
```

### Extract and unpickle file from tar archive

```
compress_pickle.read_tar_pickle(
    'myarchive.tar.gz', 
    'path/to/file/in/archive/obj.pickle'
)
```

