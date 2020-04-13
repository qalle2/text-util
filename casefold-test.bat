@echo off
cls

echo === Original file ===
type test-in\casefold.txt
echo.

echo === Fold the letter case ===
python casefold.py < test-in\casefold.txt
