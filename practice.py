# 辞書型のkeyカウント方法参照

with open('ranking1.csv', 'r') as f:
    onigiris = f.read().splitlines()
    count = {}
    for onigiri in onigiris:
        count.setdefault(onigiri, 0)
        count[onigiri] += 1
    items = sorted(count.items(), key=lambda x: x[1], reverse=True)
    for key, value in items:
        print(key)
