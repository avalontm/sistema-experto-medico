import collections
import collections.abc

for nombre in ("Mapping", "MutableMapping", "Sequence", "Iterable", "Callable"):
    if not hasattr(collections, nombre):
        setattr(collections, nombre, getattr(collections.abc, nombre))
