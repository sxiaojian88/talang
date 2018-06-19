#!/usr/bin/env python
"""Simple example of publish/subscribe illustrating topics.

Publisher and subscriber can be started in any order, though if publisher
starts first, any messages sent before subscriber starts are lost.  More than
one subscriber can listen, and they can listen to  different topics.

Topic filtering is done simply on the start of the string, e.g. listening to
's' will catch 'sports...' and 'stocks'  while listening to 'w' is enough to
catch 'weather'.
"""

#-----------------------------------------------------------------------------
#  Copyright (c) 2010 Brian Granger, Fernando Perez
#
#  Distributed under the terms of the New BSD License.  The full license is in
#  the file COPYING.BSD, distributed as part of this software.
#-----------------------------------------------------------------------------

import sys
import time
import zmq
import numpy

def main():

    connect_to ='tcp://119.28.51.224:5001'
    ctx = zmq.Context()
    s = ctx.socket(zmq.SUB)
    s.connect(connect_to)
    s.setsockopt_string(zmq.SUBSCRIBE,'')

    try:
        while True:
            msg = s.recv_string()
            print(' msg:%s' % msg)
            time.sleep(1.0)
    except KeyboardInterrupt:
        pass
    print("Done.")

if __name__ == "__main__":
    main()
