import glob

positions = []
counts = {}
for file in glob.glob("./inputs/*.txt"):
    with open(file) as f:
        game = []
        answer = []
        for _ in range(4):
            game += (list(map(str, f.readline().strip().split(" "))))
        f.readline()
        for _ in range(4):
            answer.append(list(map(str, f.readline().strip().split(" "))))

        for sol in answer:
            pos = []

            for w in sol:
                hor = game.index(w) // 4
                ver = game.index(w) % 4
                ver = {0: "a", 1: "b", 2: "c", 3: "d"}[ver]
                pos.append(f'{hor+1}{ver}')
            key = ''.join(sorted(pos))
            counts[key] = counts.get(key, 0) + 1

for c in counts:
    if counts[c] > 1:
        print(c, counts[c])
