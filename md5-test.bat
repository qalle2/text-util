@echo off
cls

echo === The correct MD5 for the file password.txt is 5f4dcc3b5aa765d61d8327deb882cf99 ===
python md5.py test-in\password.txt
echo.

echo === Help text ===
python md5.py
echo.

echo === This should cause an error ===
python md5.py nonexistent
