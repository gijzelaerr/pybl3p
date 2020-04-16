# pybl3p
A Python bl3p API

## installation

```shell script
$ pip install pybl3p
```

## usage

For the public API
```python
from pybl3p.public import orderbook
orderbook()
```

For the private API first set your public and private key as environment variables. This procedure might change in the future, but this way you don't accidentally push your private keys in a notebook or source code:

```shell script
export BL3P_PUB="........-....-....-....-............"
export BL3P_PRIV="(long string with a-z/A-Z/0-9 and =)"
```

Now from python you can access the private API:

```python
from pybl3p.private import depth_full
depth_full()
```
