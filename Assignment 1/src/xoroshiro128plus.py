class Xoroshiro128Plus:
    def __init__(self, seed1=0x123456789ABCDEF0, seed2=0x0FEDCBA987654321):
        self.s0 = seed1 & ((1 << 64) - 1)  # force 64-bit
        self.s1 = seed2 & ((1 << 64) - 1)

    def _rotl(self, x, k):
        return ((x << k) | (x >> (64 - k))) & ((1 << 64) - 1)

    def next(self):
        s0 = self.s0
        s1 = self.s1

        # Output function (the actual random number)
        result = (s0 + s1) & ((1 << 64) - 1)

        # State transition (bit mixing and diffusion)
        s1 ^= s0
        self.s0 = self._rotl(s0, 55) ^ s1 ^ ((s1 << 14) & ((1 << 64) - 1))
        self.s1 = self._rotl(s1, 36)

        return result

    def random_int(self, max_value):
        return self.next() % max_value
