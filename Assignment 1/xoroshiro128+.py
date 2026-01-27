"""
  xoroshiro128+ : Modern Pseudo-Random Number Generator (PRNG)

  Name meaning:-
  "xoroshiro" = XOR + Rotate + Shift + Random
  "128"       = internal state size = 128 bits
  "+"         = output function uses addition

  Authors:-
  Designed by David Blackman and Sebastiano Vigna
"""


class Xoroshiro128Plus:
    """
    Xoroshiro128+ Random Number Generator

    Internal State:-
    The generator maintains two 64-bit integers as its internal state.
    Together they form a 128-bit memory.

    Every new random number:
        - depends on the previous state
        - modifies the state
        - produces a new output
    """

    def __init__(self, seed1=0x123456789ABCDEF0, seed2=0x0FEDCBA987654321):
        """
        Initialize the generator with two seeds.

        Parameters:-
        seed1 : int
            First 64-bit seed value
        seed2 : int
            Second 64-bit seed value

        These two values together form the 128-bit internal state.
        """
        self.s0 = seed1 & ((1 << 64) - 1)  # force 64-bit
        self.s1 = seed2 & ((1 << 64) - 1)

    def _rotl(self, x, k):
        """
        Rotate-left operation (bitwise rotation).

        This moves bits circularly instead of discarding them.
        It improves randomness and bit mixing.

        Example:
            1011001 rotated left by 2 → 1100101
        """
        return ((x << k) | (x >> (64 - k))) & ((1 << 64) - 1)

    def next(self):
        """
        Generate the next 64-bit pseudo-random number.

        Algorithm steps:-
        1. Take current state values (s0, s1)
        2. Output = s0 + s1
        3. Mix state using XOR, shifts, and rotations
        4. Update internal state
        5. Return output

        Returns:-
        int
            A 64-bit pseudo-random integer
        """

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
        """
        Generate a random integer in the range [0, max_value - 1]. 
        This converts a 64-bit random number into a bounded integer.

        Parameters:-
        max_value : int
            Upper bound (exclusive)

        Returns:-
        int
            Random integer in [0, max_value - 1]
        """
        return self.next() % max_value
