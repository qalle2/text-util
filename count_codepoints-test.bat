@echo off
cls

echo === Default settings ===
python count_codepoints.py < test-in\count_codepoints.txt
echo.

echo === NFD ===
python uninorm.py -n nfd < test-in\count_codepoints.txt | python count_codepoints.py
echo.

echo === NFC ===
python uninorm.py -n nfc < test-in\count_codepoints.txt | python count_codepoints.py
