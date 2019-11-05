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

For the private API first set your public and private key as environment variables:
```shell script
export BL3P_PUB="........-....-....-....-............"
export BL3P_PRIV="(long string with a-z/A-Z/0-9 and =)"
```

```python
from pybl3p.private import depth_full
depth_full()
```
