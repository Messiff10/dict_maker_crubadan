import os
import time

import numpy as np
import tensorflow as tf
import data_feeder as data_feeder

output_dir = '/home/sunquan/data/gpt2new/gpt2data/engbout'
data_path = '/home/sunquan/data/gpt2new/lstm/engb/'
minimum_size = 30


def _int64_feature(value):
    """Returns an int64_list from a bool / enum / int / uint."""
    return tf.train.Feature(int64_list=tf.train.Int64List(value=value))

def _bytes_feature(value):
  """Returns a bytes_list from a string / byte."""
  return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))


def create_file(output_dir,data,name):
    s = name + ".tfrecord"

    with tf.python_io.TFRecordWriter(os.path.join(output_dir, s)) as writer:
        good_files = 0
        current = None
        count = 0
        shufflesize = 1
        repeatnum = 1
        batch_size = 1
        dataset = data_feeder.tfrecordnormal_fn(data,batch_size,shufflesize,repeatnum)
        iterator = dataset.make_one_shot_iterator()
        next_element = iterator.get_next()
        step = 1
        epochs = 2000
        sess = tf.Session()
        while(step<epochs):
            
            epoch_size, lm_data_x,lm_data_y,lm_mask,sequence_length= sess.run(next_element)
            epochs = epoch_size[0]/batch_size*repeatnum
            #print(epochs)
            step = step + 1
            #print(lm_data_x[0])
            temp = 0
            for x in enumerate(lm_data_x[0]):
                if x==0:
                    break
                temp+=1
            if temp<6:
                print('!!!!!!!!!!!!!!!!')
                print(temp)
            # print(len(lm_data_x))
            # if len(lm_data_x[0])< minimum_size:
            #     continue
            # print(len(lm_data_x[0]))
            #print(lm_data_x[0][:temp])
            print(count)
            count+=1
            hash = name
            feature = {
                "hash": _bytes_feature(hash.encode()),
                "text": _int64_feature(lm_data_x[0][:temp])
            }
            tf_example = tf.train.Example(features=tf.train.Features(feature=feature))
            writer.write(tf_example.SerializeToString())
    writer.close()
    print('ok!!!!!!!!!!!!!!!!!!!!!!!')

train_dataword = [data_path+"train_%d.tfrecord"%i for i in range(19)]
valid_dataword = [data_path+"dev_0.tfrecord"]
print('create!')
create_file(output_dir,train_dataword,'gpt2train')
create_file(output_dir,valid_dataword,'gpt2valid')
