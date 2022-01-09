# Compare of two JSON files

Just use it by cmd line like: **app.py pathtofile1 pathtofile2**

### Results you must see in console output

Base algoritm of recursive create field list from dictionary

```  
  def recursive_read(d: dict):
    result = []
    for key, val in d.items():
        if type(val) == dict:
            result += recursive_read(val)
        result.append(str(key))
    return result
```
