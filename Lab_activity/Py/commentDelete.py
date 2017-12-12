with open("in", 'r') as f:
    with open("out", 'w') as w:
        for line in f:
            if not line.startswith('/*'):
                w.write(line[:line.find('//')])
                w.write('\n')