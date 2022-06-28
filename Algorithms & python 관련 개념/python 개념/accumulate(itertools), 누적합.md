### accumulate(itertools), 누적합

```python
from itertools import accumulate

a = [x+1 for x in range(1000000)]
b = list(accumulate(a))
```

|실행코드|값|속도|
|-----|-----|-----|
|for문|10만|0.01894974708557129|
|accumulate|10만|0.004986286163330078|
|for문|100만|1.868004560470581|
|accumulate|100만|0.766948938369751|