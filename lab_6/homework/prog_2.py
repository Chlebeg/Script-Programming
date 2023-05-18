# Oneliner:
import sys; from collections import Counter; print(dict(Counter(len(elem) for elem in sys.stdin.read().split())))