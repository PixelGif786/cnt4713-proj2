class CwndControl:
    '''Interface for the congestion control actions'''

    def __init__(self):
        self.cwnd = 1.0 * MTU
        self.ssthresh = INIT_SSTHRESH
        self.last_acked = 0
        self.dup_acks = 0

    def on_ack(self, ackedDataLen):
        if ackedDataLen > 0:
            self.dup_acks = 0
            self.last_acked = ackedDataLen
            if self.cwnd < self.ssthresh:
                self.cwnd += ackedDataLen
            else:
                self.cwnd += MTU * ackedDataLen / self.cwnd
        else:
            self.dup_acks += 1
            if self.dup_acks == DUP_ACK_THRESHOLD:
                self.ssthresh = max(self.cwnd / 2, 2 * MTU)
                self.cwnd = self.ssthresh
                self.dup_acks = 0

    def on_timeout(self):
        #
        self.ssthresh = max(int(self.cwnd / 2), 2 * MTU)
        self.cwnd = 1.0 * MTU

    def __str__(self):
        return f"cwnd:{self.cwnd} ssthresh:{self.ssthresh}"
