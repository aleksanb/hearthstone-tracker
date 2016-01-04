def p(msg):
	print(str(msg).encode('cp1252'))


def ppad(s):
	len_pad = len(s) + 4
	print('#' * len_pad)
	print('# ' + s + ' #')
	print('#' * len_pad)
