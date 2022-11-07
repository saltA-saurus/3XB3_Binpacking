from .. import Solution
from ..model import Offline
import binpacking as bp


class BenMaier(Offline):

    def _process(self, capacity: int, weights: list[int]) -> Solution:
        return bp.to_constant_volume(weights, capacity)


class BenMaierMNP(Offline):

    def _process(self, bin_num: int, weights: list[int]) -> Solution:
        return bp.to_constant_bin_number(weights, bin_num)
