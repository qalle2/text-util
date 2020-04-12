@echo off
cls

echo === Should print aa, aba, AA, ABA ===
python pygrep.py "^ab?a$" < test-in\pygrep.txt
echo.

echo === Should print aba, abba, ABA, ABBA ===
python pygrep.py "^ab+a$" < test-in\pygrep.txt
echo.

echo === Should print an error message ===
python pygrep.py "[" < test-in\pygrep.txt
echo.

echo === Help ===
python pygrep.py
