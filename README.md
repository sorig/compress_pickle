# Functions to read/write to/from gzipped pickle files and tar archives

## Examples

Firstly, import the module

```
>>> import compress_pickle
```

### Pickle, compress and write object to disk

```
>>> compress_pickle.to_gz_pickle(my_obj, 'my_obj.pickle.gz')
```

### Decompress and load compressed pickle file

```
>>> my_obj = compress_pickle.read_gz_pickle('my_obj.pickle.gz')
```

### List pickle files in a tar archive:

```
>>> compress_pickle.list_tar_file_contents('myarchive.tar.gz', '.*pickle')
['path/to/file/in/archive/obj.pickle']
```

### Extract and unpickle file from tar archive

```
>>> obj_from_tar = compress_pickle.read_tar_pickle(
    'myarchive.tar.gz', 
    'path/to/file/in/archive/obj.pickle'
)
```

