def all_variants(text):
    for b in range(len(text)):
        for c in range(len(text)-b):
            yield text[c:c+b+1]
a = all_variants("abc")
for i in a:
    print(i)