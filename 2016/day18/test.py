row = '.^^^^^.^^^..^^^^^...^.^..^^^.^^....^.^...^^^...^^^^..^...^...^^.^.^.......^..^^...^.^.^^..^^^^^...^.'
L = len(row)
ct = row.count('.')
for i in xrange(1, 400000):
    row = [row[1]] + ['^' if ((row[j - 1] == '^') ^ (row[j + 1] == '^')) else '.' for j in range(1, L - 1)] + [row[-2]]
    ct += row.count('.')
print ct