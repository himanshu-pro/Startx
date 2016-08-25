with open(raw_input('Enter file path: '), 'r') as fileDp:
    # using space delimiting as tokenizer. (Note: Not separating on newlines or periods as not told to do so)
    arr = fileDp.read().split(' ')
    arr_len = len(arr)
    print sum([len(arr[i]) for i in xrange(arr_len)])/float(arr_len)
