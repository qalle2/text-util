clear

echo "=== casefold (should print the same word twice) ==="
python3 casefold.py < test-in/casefold.txt
echo

echo "=== countchars ==="
python3 countchars.py < test-in/countchars.txt
echo

echo "=== countlines ==="
python3 countlines.py < test-in/countlines.txt
echo

echo "=== finsort ==="
python3 finsort.py < test-in/finsort.txt
echo

echo "=== getwords ==="
python3 getwords.py < test-in/getwords.txt
echo

echo "=== grouplines ==="
echo "Entire lines:"
python3 grouplines.py 0 < test-in/grouplines.txt
echo "Prefixes:"
python3 grouplines.py 8 < test-in/grouplines.txt
echo "Suffixes:"
python3 grouplines.py -8 < test-in/grouplines.txt
echo

echo "=== lineset ==="
echo "Union:"
python3 lineset.py u test-in/lineset1.txt test-in/lineset2.txt
echo "Intersection:"
python3 lineset.py i test-in/lineset1.txt test-in/lineset2.txt
echo "Difference:"
python3 lineset.py d test-in/lineset1.txt test-in/lineset2.txt
echo

echo "=== uniquelines ==="
python3 uniquelines.py < test-in/countlines.txt
echo
