# import MeCab
# mecab = MeCab.Tagger("-Owakati")
# with open("/Users/ff/Desktop/train_data/jp/jp_web.txt",'r',encoding='utf-8') as f_in:
#     with open("/Users/ff/Desktop/train_data/jp/jo_web_split_token2.txt", 'w', encoding='utf-8') as f_out:
#         for sentence in f_in:
#             print(mecab.parse(sentence))
#             f_out.write(str(mecab.parse(sentence)).strip())
#             f_out.write('\n')
# print("Finish line")

from janome.tokenizer import Tokenizer as janome_tokenizer
with open("/Users/ff/Desktop/train_data/jp/jp_web.txt",'r',encoding='utf-8') as f_in:
    with open("/Users/ff/Desktop/train_data/jp/jo_web_split_token3.txt", 'w', encoding='utf-8') as f_out:
        for sentence in f_in:
# sentence = "日本人のものと見られる、延べ２億件のメールアドレスとパスワードが闇サイトで販売されていたことがわかりました。過去に漏えいしたデータを集めたものと見られ、調査に当たったセキュリティー企業は、日本を狙ったサイバー攻撃のきっかけになるおそれがあるとして注意を呼びかけています。"
            token_object = janome_tokenizer()
            alist=[x.surface for x in token_object.tokenize(sentence)]
            print(" ".join(alist))
            f_out.write(" ".join(alist).strip())
            f_out.write('\n')