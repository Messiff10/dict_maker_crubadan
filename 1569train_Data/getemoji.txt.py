import emoji
# a=emoji.get_emoji_regexp()
# print(type(a),len(a))
emoji_path = "/Users/ff/Desktop/train_data/emojis"
emojiset=set()
# print(file_path)
with open(emoji_path, 'r', encoding='utf-8') as f_emoji:
    for line in f_emoji:
        emojis = line.strip().split('\t')
        # alist_all = [ch for ch in emojis[0].strip()]
        # for allll in alist_all:
        if emojis[0].strip() not in emojiset:
            emojiset.add(emojis[0].strip())
all_emojis=emoji.unicode_codes.EMOJI_UNICODE.values()
for e in all_emojis:
    # alist = [ch for ch in e.strip()]
    # for a in alist:
    if e.strip() not in emojiset:
        emojiset.add(e.strip())
with open("/Users/ff/Desktop/train_data/emojis_new.txt",'a',encoding='utf-8') as f_out:
    for em in emojiset:
        print(em)
        f_out.write(em.strip())
        f_out.write('\n')
print("Finish line")