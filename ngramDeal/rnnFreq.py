file_rnn = "/Users/ff/Desktop/vocab_in_words"
unigram_file = "/Users/ff/Downloads/de_unigram.txt"
file_out = "/Users/ff/Desktop/vocab_freq"
f_in = open(file_rnn, 'r', encoding='utf-8')
f_uni = open(unigram_file, 'r', encoding='utf-8')
f_out = open(file_out, 'w', encoding='utf-8')

rnn = {}
for l in f_uni:
    word, freq = l.split('\t')
    rnn[word] = freq

f_uni.close()
for l_u in f_in:
    word = l_u.split('##')[0]
    if word in rnn.keys():
        result = l_u.strip() + '##' + str(rnn[word])
        f_out.write(result.strip())
        f_out.write('\n')
    else:
        print(l_u.strip())
        f_out.write(l_u.strip())
        f_out.write('\n')

f_in.close()
