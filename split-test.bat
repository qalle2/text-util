@echo off
rem WARNING: This batch file DELETES files. Run at your own risk.

cls
if exist test-out\*.* del /q test-out\*.*

echo === Splitting ===
python split.py test-in\small.dat 20000 test-out\2e4.*
python split.py test-in\large.dat 10000000 test-out\1e7.*
python split.py test-in\large.dat 5000000 test-out\5e6.*
python split.py test-in\large.dat 1400000 test-out\14e5.*
echo.

echo === Listing files ===
dir /a-d test-out | find ":" | find "  "
echo.

echo === Recombining ===
cd test-out
copy /b 2e4.0 + 2e4.1 + 2e4.2 2e4 > nul
copy /b 1e7.0 + 1e7.1 1e7 > nul
copy /b 5e6.0 + 5e6.1 + 5e6.2 5e6 > nul
copy /b 14e5.00 + 14e5.01 + 14e5.02 + 14e5.03 + 14e5.04 + 14e5.05 + 14e5.06 + 14e5.07 + 14e5.08 + 14e5.09 + 14e5.10 14e5 > nul
cd ..
echo.

echo === Comparing ===
fc /b test-in\small.dat test-out\2e4
fc /b test-in\large.dat test-out\1e7
fc /b test-in\large.dat test-out\5e6
fc /b test-in\large.dat test-out\14e5

if exist test-out\*.* del /q test-out\*.*

echo === This should cause the "file already exists" error ===
echo xxx > test-out\already-exists-0.dat
python split.py test-in\small.dat 20000 test-out\already-exists-*.dat
echo.

echo === Help text ===
python split.py --help
