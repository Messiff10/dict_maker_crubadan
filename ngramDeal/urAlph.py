import re
import sys
"""
替换字母
特殊语言 unicode不同导致
ur
"""
# file = sys.argv[1]
# file_out = sys.argv[2]
file = "/Users/ff/Desktop/data/dict/input/ur/ur_bigram.txt"
file_out = "/Users/ff/Desktop/data/dict/input/ur/ur_bigram_out.txt"
f_in = open(file, 'r', encoding='utf-8')
f_out = open(file_out, 'w', encoding="utf-8")
vocab_set=set()
regex = re.compile(r"[^ےیءھہونملگکقفغعظطضصشسژڑرذڈدخحچجثٹتپباآ……']")
for l in f_in:
    # if re.search(regex, l.strip()) is None:
    # print(l.strip())
    l = l.strip()
    l = l.replace('\uFBAE', '\u06D2').replace('\uFBAF', '\u06D2') \
        .replace('\uFBFC', '\u06CC').replace('\uFBFD', '\u06CC').replace('\uFBFE', '\u06CC').replace('\uFBFF', '\u06CC') \
        .replace('\uFE80', '\u0621') \
        .replace('\uFBAA', '\u06BE').replace('\uFBAB', '\u06BE').replace('\uFBAC', '\u06BE').replace('\uFBAD', '\u06BE') \
        .replace('\uFBA6', '\u06C1').replace('\uFBA7', '\u06C1').replace('\uFBA8', '\u06C1').replace('\uFBA9', '\u06C1') \
        .replace('\uFBEE', '\u0648').replace('\uFBEF', '\u0648').replace('\uFBA8', '\u0648').replace('\uFBA9', '\u0648') \
        .replace('\uFEE5', '\u0646').replace('\uFEE6', '\u0646').replace('\uFEE7', '\u0646').replace('\uFEE8', '\u0646') \
        .replace('\uFEE1', '\u0645').replace('\uFEE2', '\u0645').replace('\uFEE3', '\u0645').replace('\uFEE4', '\u0645') \
        .replace('\uFEDD', '\u0644').replace('\uFEDE', '\u0644').replace('\uFEDF', '\u0644').replace('\uFEE0', '\u0644') \
        .replace('\uFB92', '\u06AF').replace('\uFB93', '\u06AF').replace('\uFB94', '\u06AF').replace('\uFB95', '\u06AF') \
        .replace('\uFB8E', '\u06A9').replace('\uFB8F', '\u06A9').replace('\uFB90', '\u06A9').replace('\uFB91', '\u06A9') \
        .replace('\uFED5', '\u0642').replace('\uFED6', '\u0642').replace('\uFED7', '\u0642').replace('\uFED8', '\u0642') \
        .replace('\uFED1', '\u0641').replace('\uFED2', '\u0641').replace('\uFED3', '\u0641').replace('\uFED4', '\u0641') \
        .replace('\uFECE', '\u063A').replace('\uFECF', '\u063A').replace('\uFED0', '\u063A') \
        .replace('\uFEC9', '\u0639').replace('\uFECA', '\u0639').replace('\uFECB', '\u0639').replace('\uFECC', '\u0639') \
        .replace('\uFEC5', '\u0638').replace('\uFEC6', '\u0638').replace('\uFEC7', '\u0638').replace('\uFEC8', '\u0638') \
        .replace('\uFEC1', '\u0637').replace('\uFEC2', '\u0637').replace('\uFEC3', '\u0637').replace('\uFEC4', '\u0637') \
        .replace('\uFEBD', '\u0636').replace('\uFEBE', '\u0636').replace('\uFEBF', '\u0636').replace('\uFEC0', '\u0636') \
        .replace('\uFEB9', '\u0635').replace('\uFEBA', '\u0635').replace('\uFEBB', '\u0635').replace('\uFEBC', '\u0635') \
        .replace('\uFEB5', '\u0634').replace('\uFEB6', '\u0634').replace('\uFEB7', '\u0634').replace('\uFEB8', '\u0634') \
        .replace('\uFEB1', '\u0633').replace('\uFEB2', '\u0633').replace('\uFEB3', '\u0633').replace('\uFEB4', '\u0633') \
        .replace('\uFB8A', '\u0698').replace('\uFB8B', '\u0698') \
        .replace('\uFB8C', '\u0691').replace('\uFB8D', '\u0691') \
        .replace('\uFEAD', '\u0631').replace('\uFEAE', '\u0631') \
        .replace('\uFEAB', '\u0630').replace('\uFEAC', '\u0630') \
        .replace('\uFB88', '\u0688').replace('\uFB89', '\u0688') \
        .replace('\uFEA9', '\u062F').replace('\uFEAA', '\u062F') \
        .replace('\uFEA5', '\u062E').replace('\uFEA6', '\u062E').replace('\uFEA7', '\u062E').replace('\uFEA8', '\u062E') \
        .replace('\uFEA1', '\u062D').replace('\uFEA2', '\u062D').replace('\uFEA3', '\u062D').replace('\uFEA4', '\u062D') \
        .replace('\uFB7A', '\u0686').replace('\uFB7B', '\u0686').replace('\uFB7C', '\u0686').replace('\uFB7D', '\u0686') \
        .replace('\uFE9D', '\u062C').replace('\uFE9E', '\u062C').replace('\uFE9F', '\u062C').replace('\uFEA0', '\u062C') \
        .replace('\uFE99', '\u062B').replace('\uFE9A', '\u062B').replace('\uFE9B', '\u062B').replace('\uFE9C', '\u062B') \
        .replace('\uFB66', '\u0679').replace('\uFB67', '\u0679').replace('\uFB68', '\u0679').replace('\uFB69', '\u0679') \
        .replace('\uFE95', '\u062A').replace('\uFE96', '\u062A').replace('\uFE97', '\u062A').replace('\uFE98', '\u062A') \
        .replace('\uFB56', '\u067E').replace('\uFB57', '\u067E').replace('\uFB58', '\u067E').replace('\uFB59', '\u067E') \
        .replace('\uFE8F', '\u0628').replace('\uFE90', '\u0628').replace('\uFE91', '\u0628').replace('\uFE92', '\u0628') \
        .replace('\uFE8D', '\u0627').replace('\uFE8E', '\u0627') \
        .replace('\uFE81', '\u0622').replace('\uFE82', '\u0622')
    if l.strip().split('\t')[0] not in vocab_set:
        vocab_set.add(l.strip().split('\t')[0])
        if re.search(regex, l.strip().split('\t')[0]) is None:
            f_out.write(l.strip())
            f_out.write('\n')
f_in.close()
