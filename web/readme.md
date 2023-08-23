1. js部分代码转为Python版本

   ```javascript
   n = JSON.stringify(n);
   n = encodeURIComponent(n);
   ```

   ```python
   import json
   from urllib.parse import quote
   
   encrypt_info = {}
   n = json.dumps(encrypt_info, separators=(",", ":"))
   n = quote(n).replace("%28", "(").replace("%27", "'").replace("%29", ")").replace("/", "%2F")
   ```

2. 

