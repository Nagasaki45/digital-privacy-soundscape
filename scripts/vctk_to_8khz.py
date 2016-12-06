"""
The VCTK corpus comes in 48KHz sample rate. This is too much for this
application. This script convert it to 8KHz.
"""

import os
from subprocess import call
import sys

corpus_dir = sys.argv[1]
source_dir = os.path.join(corpus_dir, 'wav48')
target_dir = os.path.join(corpus_dir, 'wav8')

for speaker in os.listdir(source_dir):
     source_speaker_dir = os.path.join(source_dir, speaker)
     target_speaker_dir = os.path.join(target_dir, speaker)
     os.mkdir(target_speaker_dir)
     for filename in os.listdir(source_speaker_dir):
         source = os.path.join(source_speaker_dir, filename)
         target = os.path.join(target_speaker_dir, filename)
         call(['sox', source, '-r 8000', target])
