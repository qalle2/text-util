@echo off
cls

echo === Default settings ===
python count_words.py < test-in\count_words.txt
echo.

echo === Input from casefold.py ===
python casefold.py < test-in\count_words.txt | python count_words.py
echo.

echo === Binary file ===
python count_words.py < test-in\allbytes.dat
