import re


MAX_UNI_FREQ = 250
MIN_UNI_FREQ = 1
MAX_BI_FREQ = 15
MIN_BI_FREQ = 1
# INVALID_LETTERS = r'[^\u1200-\u135A\u1380-\u138F\u2D80-\u2DDF\uAB00-\uAB2F]'
INVALID_LETTERS = r'[^a-zA-ZÅåÆæØøЀ-ӿ\'\-]'


def get_freq_from_line_index(lines, index):
    return int(lines[index].strip().split()[-1])


def scale(ori_min, ori_max, new_min, new_max, x):
    return int((new_max - new_min) * (x - ori_min) / (ori_max - ori_min) + new_min)


def build_unigram_dict(in_file_path, out_file_path):
    with open(in_file_path, 'r', encoding='utf-8') as in_file:
        in_lines = in_file.readlines()

    in_lines = [l for l in in_lines if not any(re.match(INVALID_LETTERS, w) for w in l.strip().split()[:-1])]

    ori_max_freq = get_freq_from_line_index(in_lines, 5)
    ori_min_freq = get_freq_from_line_index(in_lines, -1)

    with open(out_file_path, 'w+', encoding='utf-8') as out_file:
        for line in in_lines:
            word, freq = line.strip().split()
            freq = int(freq)
            new_freq = scale(ori_min_freq, ori_max_freq, MIN_UNI_FREQ, MAX_UNI_FREQ, freq)
            new_freq = MAX_UNI_FREQ if new_freq > MAX_UNI_FREQ else new_freq
            out_file.write(f'{word}\t{new_freq}\n')


def build_bigram_dict(in_file_path, out_file_path):
    with open(in_file_path, 'r', encoding='utf-8') as in_file:
        in_lines = in_file.readlines()

    in_lines = [l for l in in_lines if not any(re.match(INVALID_LETTERS, w) for w in l.strip().split()[:-1])]

    ori_max_freq = get_freq_from_line_index(in_lines, 5)
    ori_min_freq = get_freq_from_line_index(in_lines, -1)

    with open(out_file_path, 'w+', encoding='utf-8') as out_file:
        for line in in_lines:
            prev_word, next_word, freq = line.strip().split()
            freq = int(freq)
            new_freq = scale(ori_min_freq, ori_max_freq, MIN_BI_FREQ, MAX_BI_FREQ, freq)
            new_freq = MAX_UNI_FREQ if new_freq > MAX_UNI_FREQ else new_freq
            out_file.write(f'{prev_word}\t{next_word}\t{new_freq}\n')


if __name__ == '__main__':
    unigram_dict_file_input = "/Users/grace/data/dict/it/it-words.txt"
    bigram_dict_file_input = "/Users/grace/data/dict/it/it-wordbigrams.txt"
    unigram_dict_file_output = "/Users/grace/data/dict/it/it_unigram"
    bigram_dict_file_output = "/Users/grace/data/dict/it/it_bigram"
    build_unigram_dict(unigram_dict_file_input, unigram_dict_file_output)
    build_bigram_dict(bigram_dict_file_input, bigram_dict_file_output)
    # print(scale(1, 80, 1, 150, 70))
