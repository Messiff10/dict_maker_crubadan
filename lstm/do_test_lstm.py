import os

import model_for_test_lstm
import tensorflow as tf
import json
from collections import OrderedDict

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
model = model_for_test_lstm.LSTMModel(is_training=False)
sess = tf.Session()
vocab_path = '/home/pubsrv/data/train_data/en_US/train_data_en_US_user_web_shuf_case_nomap'
records = model.testlite_lstm(sess, 'lm_enus.tflite', 'kc_enus.tflite', "en_US_huawei_facebook.txt", vocab_path)

# print(records)
# json.dump(outputs,open("en_US_huawei_facebook_res.json","w",encoding="utf-8"),ensure_ascii=False)
# def judge_equal(list1,list2):
#     if len(list1)!= len(list2):
#         return False
#     for ele in list1:
#         if ele not in list2:
#             return False
#     return True
# """
# outputs = json.load(open("en_US_huawei_facebook_res.json","r",encoding="utf-8"))
# """
# items = list(outputs.items())
#
# counter = 0
# j_test = []
# j_targets = []
# with open("log_en_US_huawei_facebook.txt_temp","r") as f_jtest:
#     last_target = ""
#     lines = f_jtest.readlines()
#     for index,line in enumerate(lines):
#         line = line.strip()
#         if line.startswith("target:"):
#             last_target = line.split("target:")[-1].strip()
#             continue
#         if not line.startswith("target:") and last_target!="":
#             j_targets.append(last_target)
#             last_target = ""
#             line_arr = line.replace("[", "").replace("]", "").replace("'", "").replace(" ", "").split(",")
#             j_test.append(line_arr)
#             continue
#         if line == "hit!":
#             continue
#
#
# for index in range(len(targets)):
#     if j_targets[index]!=targets[index]:
#         print(index,j_targets[index],targets[index])
# for index in range(len(items)):
#     if items[index][-1] != j_test[index]:
#         print(index,items[index][-1],j_test[index])
#
#
#
