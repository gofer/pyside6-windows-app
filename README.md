# PythonでWindows向けのアプリケーションを生成

PySide6とPyinstallerで構成する


## ビルド方法

```sh
pyinstaller -w -i resources\app.ico app.py

Copy-Item -Recurse resources .\dist\app
```
