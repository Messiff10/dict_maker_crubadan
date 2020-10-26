# coding=utf-8
# Copyright 2018 The Google AI Language Team Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Create masked LM/next sentence masked_lm TF examples for BERT."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
import tensorflow as tf



def main(_):

  count = 0
  docs = []
  with tf.gfile.GFile('/home/pubsrv/data/en_US_train_data/en_US.txt', "r") as reader:
    while True:
      line = reader.readline()
      docs.append(line)
      count +=1
      print(count)
      if count%5000000==0:
        f = open(('/home/sunquan/data/gpt2/us_%d.txt'%(count/5000000)),'w+')
        for l in docs:
          f.write(l)
        f.close()
        docs = []
        #break


if __name__ == "__main__":

  tf.app.run()
