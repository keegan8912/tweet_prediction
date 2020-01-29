import gpt_2_simple as gpt2
from datetime import datetime
import tensorflow as tf
import time




tf.reset_default_graph()
#restore_from='latest'
sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, run_name='trump_clean_small')

for loop_idx in range(0,5):
    started = time.time()

    gpt2.generate(sess,
                length=50,
                temperature=0.8,
                nsamples=1,
                run_name = 'trump_clean_small',
                prefix = 'Your mum'
                # truncate = '.',
                # include_prefix = True,
                #batch_size=1
                )
    ended = time.time()
    print('Per iteration time: {} seconds'.format(ended-started))