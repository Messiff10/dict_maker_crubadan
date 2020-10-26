from math import log10

import kenlm
model = kenlm.Model('/home/pubsrv/data/original/en_US/en_US_original2.bin')
sentence='this is a sentence .'


class kenlm_model():
    def __init__(self, save_path='/home/pubsrv/data/original/en_US', project='en_US_original2', \
                 memory='50%', min_count=5, order=5, \
                 skip_symbols='"<unk>"', kenlm_model_path='/home/zhangzhongfang/kenlm/build/bin/'):
        self.memory = memory  # 运行预占用内存
        self.min_count = min_count  # n-grams考虑的最低频率
        self.order = order  # n-grams的数量
        self.kenlm_model_path = kenlm_model_path
        # kenlm模型路径 / 包括：count_ngrams/lmplz等kenlm模块的路径
        self.corpus_file = save_path + '/%s.corpus' % project  # 语料保存的文件名
        self.vocab_file = save_path + '/%s.chars' % project  # 字符集保存的文件名
        self.ngram_file = save_path + '/%s.ngrams' % project  # ngram集保存的文件名
        self.output_file = save_path + '/%s.vocab' % project  # 最后导出的词表文件名
        self.arpa_file = save_path + '/%s.arpa' % project  # 语言模型的文件名arpa
        self.klm_file = save_path + '/%s.klm' % project  # 语言模型的二进制文件名klm,也可以.bin
        self.skip_symbols = '"<unk>"'
        # lm_train训练时候，Treat <s>, </s>, and <unk> as whitespace instead of throwing an exception
        # 这里的转移概率是人工总结的，总的来说，就是要降低长词的可能性。
        trans = {'bb': 1, 'bc': 0.15, 'cb': 1, 'cd': 0.01, 'db': 1, 'de': 0.01, 'eb': 1, 'ee': 0.001}
        self.trans = {i: log10(j) for i, j in trans.items()}
        self.model = None
    def read_ngrams(self):
        """读取思路参考https://github.com/kpu/kenlmtest/issues/201
        """
        # 数据读入
        f = open(self.vocab_file)
        chars = f.read()
        # print(chars)
        f.close()
        chars = chars.split('\x00')
        chars = [i for i in chars]  # .decode('utf-8')
        # print("chars",chars)
        #
        ngrams = [Counter({}) for _ in range(self.order)]
        total = 0
        size_per_item = self.order * 4 + 8
        f = open(self.ngram_file, 'rb')
        filedata = f.read()
        filesize = f.tell()
        f.close()
        for i in range(0, filesize, size_per_item):
            s = filedata[i: i + size_per_item]
            n = self.unpack('l', s[-8:])
            if n >= self.min_count:
                total += n
                c = [self.unpack('i', s[j * 4: (j + 1) * 4]) for j in range(self.order)]
                c = ''.join([chars[j] for j in c if j > 2])
                for j in range(self.order):  # len(c) -> self.order
                    ngrams[j][c[:j + 1]] = ngrams[j].get(c[:j + 1], 0) + n
        # print("ngrams")
        return ngrams, total
if __name__ == '__main__':
    km = kenlm_model(save_path='/home/pubsrv/data/original/en_US', project='en_US_original2', \
                     memory='50%', min_count=2, order=5, \
                     skip_symbols='"<unk>","<s>","</s>"', kenlm_model_path='/home/zhangzhongfang/kenlm/build/bin/')
    ngrams,total = km.read_ngrams()
    ngrams_2 = km.filter_ngrams(ngrams, total, min_pmi=[0, 1, 3, 5])