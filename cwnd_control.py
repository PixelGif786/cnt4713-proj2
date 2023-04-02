from common import *


class CwndControl:
    '''Interface for the congestio control actions'''

    def __init__(self):
        self.cwnd = 1.0 * MTU
        self.ssthresh = INIT_SSTHRESH

    def on_ack(self, ackedDataLen):
        if self.cwnd < self.ssthresh:
            # Slow start
            self.cwnd += ackedDataLen
        else:
            # Congestion avoidance
            self.cwnd += (MTU * ackedDataLen) / self.cwnd

    def on_timeout(self):
        self.ssthresh = max(self.cwnd / 2, 2 * MTU)
        self.cwnd = 1.0 * MTU

    def __str__(self):
        return f"cwnd:{self.cwnd} ssthreash:{self.ssthresh}"
