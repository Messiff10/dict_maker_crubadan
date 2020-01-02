import codecs

language = "en_US"
unigram_path = '/Users/ff/Desktop/train_data/' + language + '/' + language + '_unigram'
file_path = '/Users/ff/Desktop/train_data/' + language + '/' + language + '_user_web_train/vocab_words_head'
file_path2 = '/Users/ff/Desktop/train_data/' + language + '/' + language + '_user_web_train/vocab_words_false'
unigram=set()
false_words = {}
with codecs.open(file_path, 'r', encoding='utf-8') as f_false:
    for line in f_false:
        words = line.strip().split('\t')
        false_words[words[0]] = words[1]

with codecs.open(unigram_path, 'r', encoding='utf-8') as f_unigram:
    for line in f_unigram:
        words = line.strip().split('\t')
        if words[0].strip() not in unigram:
            unigram.add(words[0].strip())

with codecs.open(file_path2, 'r', encoding='utf-8') as f_head:
    with codecs.open(file_path2.replace('_false', '_percent'), 'w', encoding='utf-8') as f_per:
        for line in f_head:
            words = line.strip().split('\t')
            lm = 0
            if words[0].lower() in unigram:
                if words[0] in false_words.keys():
                    a = false_words[words[0]]
                    lm = int(words[1]) - int(a)
                    # print(lm)
                    print(words[0], lm, float(int(lm) / int(a)))
                    s = str(words[0]) + '\t' + str(lm) + '\t' + str(float(int(lm) / int(words[1])))
                    f_per.write(s)
                    f_per.write('\n')
