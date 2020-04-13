@echo off
cls

echo === Default settings ===
python count_words.py < test-in\count_words.txt
echo.

echo === Fold the letter case ===
python count_words.py --case-fold < test-in\count_words.txt
echo.

echo === No counts ===
python count_words.py --no-counts < test-in\count_words.txt
echo.

echo === No counts, fold the letter case ===
python count_words.py --case-fold --no-counts < test-in\count_words.txt
echo.

echo === Binary file ===
python count_words.py < test-in\allbytes.dat
echo.

echo === Help text ===
python count_words.py --help
