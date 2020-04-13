@echo off
cls

echo === Default settings ===
python count_words.py < test-in\count_words.txt
echo.

echo === No counts ===
python count_words.py --no-counts < test-in\count_words.txt
echo.

echo === Input from casefold.py, default settings ===
python casefold.py < test-in\count_words.txt | python count_words.py
echo.

echo === Input from casefold.py, no counts ===
python casefold.py < test-in\count_words.txt | python count_words.py --no-counts
echo.

echo === Binary file ===
python count_words.py < test-in\allbytes.dat
echo.

echo === Help text ===
python count_words.py --help
