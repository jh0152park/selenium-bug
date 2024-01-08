# Occurred below errors

```
PS C:\Users\박재현\Desktop\Instead_of_me\blogpay> & C:/Users/박재현/AppData/Local/Programs/Python/Python310/python.exe c:/Users/박재현/Desktop/Instead_of_me/blogpay/main.py
Traceback (most recent call last):
  File "c:\Users\박재현\Desktop\Instead_of_me\blogpay\main.py", line 16, in <module>
    from webdriver_manager.chrome import ChromeDriverManager
  File "C:\Users\박재현\AppData\Local\Programs\Python\Python310\lib\site-packages\webdriver_manager\chrome.py", line 4, in <module>
    from webdriver_manager.core.download_manager import DownloadManager
  File "C:\Users\박재현\AppData\Local\Programs\Python\Python310\lib\site-packages\webdriver_manager\core\download_manager.py", line 5, in <module>
    from webdriver_manager.core.http import WDMHttpClient
  File "C:\Users\박재현\AppData\Local\Programs\Python\Python310\lib\site-packages\webdriver_manager\core\http.py", line 4, in <module>
    from webdriver_manager.core.config import ssl_verify
  File "C:\Users\박재현\AppData\Local\Programs\Python\Python310\lib\site-packages\webdriver_manager\core\config.py", line 3, in <module>
    from dotenv import load_dotenv
ImportError: cannot import name 'load_dotenv' from 'dotenv' (C:\Users\박재현\AppData\Local\Programs\Python\Python310\lib\site-packages\dotenv\__init__.py)
```

# Solution
```
pip uninstall dotenv
pip uninstall python-dotenv
pip install python-dotenv
```
