clear

echo "=== asciify ==="
python3 asciify.py < test/asciify.txt
echo

echo "=== casefold (should print the same word twice) ==="
python3 casefold.py < test/casefold.txt
echo

echo "=== countchars ==="
python3 countchars.py < test/countchars.txt
echo

echo "=== countlines ==="
python3 countlines.py < test/countlines.txt
echo

echo "=== findword ==="
python3 findword.py st--- ro e
echo

echo "=== findword2 ==="
python3 findword2.py 4
echo

echo "=== finsort ==="
python3 finsort.py < test/finsort.txt
echo

echo "=== getwords ==="
python3 getwords.py < test/getwords.txt
echo

echo "=== grouplines ==="
echo "Entire lines:"
python3 grouplines.py 0 < test/grouplines.txt
echo "Prefixes:"
python3 grouplines.py 8 < test/grouplines.txt
echo "Suffixes:"
python3 grouplines.py -8 < test/grouplines.txt
echo

echo "=== lineset ==="
echo "Union:"
python3 lineset.py u test/lineset1.txt test/lineset2.txt
echo "Intersection:"
python3 lineset.py i test/lineset1.txt test/lineset2.txt
echo "Difference:"
python3 lineset.py d test/lineset1.txt test/lineset2.txt
echo

echo "=== rus_iso9 ==="
python3 rus_iso9.py < test/russian.txt
echo

echo "=== uniquelines ==="
python3 uniquelines.py < test/countlines.txt
echo
