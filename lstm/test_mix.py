import argparse
import json
import logging
import sys
import time
from functools import partial
from pathlib import Path
import os
import tensorflow as tf

from lstm.inputs import *
# from seq2word_rnn_model import GPT2Model
from lstm.model_for_test import GPT2Model
# This program was designed to function with multiple kinds of models, but currently only GPT2 is supported
# The first element in the tupel is the model function, the second is the function called when predicting

from lstm.config import Config
import config

FLAGS = config.FLAGS

inputs = {
    "openwebtext": openwebtext,  # Standard OpenWebtext input
    "openwebtext_longbiased": openwebtext_longbiased,
    # OpenWebtext with a bias towards showing more long (>512 tokens) examples
    "openwebtext_long": openwebtext_long,  # Openwebtext that only shows long examples
}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--tpu', type=str)  # Name of TPU to train on, if any
    parser.add_argument('--model', type=str)  # JSON file that contains model parameters
    parser.add_argument("--predict_file", type=str)  # File to take as input for predict
    parser.add_argument("--predict_text", type=str)  # Take string directly from args
    parser.add_argument("--top_k", type=int)  # Top K truncation parameter for text generation
    args = parser.parse_args()

    model_mode = 2
    with tf.Graph().as_default():
        gpu_config = tf.ConfigProto()

        with tf.name_scope("Train"):
            # train model on train data
            if model_mode == 0:  # study from gpt2 model from tfrecord soft data
                pass
            elif model_mode == 1:  # train word model
                pass
            elif model_mode == 2 or model_mode == 4:  # train gpt2model
                with tf.variable_scope("GPT2Model", reuse=False):
                    mtrain_word = GPT2Model(is_training=True, past=None)
            elif model_mode == 3:  # study from gpt2 model directly
                pass

        sess = tf.Session()
        print("training language model.")
        init = tf.group(tf.global_variables_initializer(), tf.local_variables_initializer())
        sess.run(init)

        print('train gpt2!!!!!!')
        vocab_path = '/home/pubsrv/data/train_data/en_US/train_data_en_US_user_web_shuf_mapletters_kika'

        mtrain_word.testlitelm(sess, '0727_4.tflite', "en_US_huawei_facebook.txt", vocab_path)
        # mtrain_word.test_mix(sess,'0724.tflite','0722.tflite',"en_US_facebook_kika.txt",vocab_path)
        # mtrain_word.test_letter(sess,'0628.tflite','0722.tflite',"en_US_facebook_kika.txt",vocab_path)
