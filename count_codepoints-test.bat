@echo off
cls

echo === Default settings ===
python count_codepoints.py test-in\count_codepoints.txt
echo.

echo === NFD ===
python count_codepoints.py --normalization nfd test-in\count_codepoints.txt
echo.

echo === NFC ===
python count_codepoints.py --normalization nfc test-in\count_codepoints.txt
echo.

echo === Help text ===
python count_codepoints.py --help
