from .. import Solution, WeightStream
from ..model import Online


class NextFit(Online):

    def _process(self, capacity: int, stream: WeightStream) -> Solution:
        bin_index = 0
        solution = [[]]
        remaining = capacity
        for w in stream:
            if remaining >= w:
                solution[bin_index].append(w)
                remaining = remaining - w
            else:
                bin_index += 1
                solution.append([w])
                remaining = capacity - w
        return solution

class Terrible(Online):

    def _process(self, capacity: int, stream: WeightStream) -> Solution:
        
        solution = []
        for w in stream:
            if capacity >= w:
                solution.append([w])
        return solution

class FirstFit(Online):

    def _process(self, capacity: int, stream: WeightStream) -> Solution:
        
        bin_index = 0
        solution = []
        bin_remaining = []
        for w in stream:
            j = 0
            while j < bin_index:
                if bin_remaining[j] >= w:
                    solution[j].append(w)
                    bin_remaining[j] -= w 
                    break
                j += 1

            if j == bin_index:
                solution.append([w])
                bin_remaining.append(capacity)
                bin_remaining[bin_index] = capacity - w
                bin_index += 1

        return solution

class BestFit(Online):

    def _process(self, capacity: int, stream: WeightStream) -> Solution:
        
        solution = []
        for w in stream:
            if capacity >= w:
                solution.append(w)
        return solution

class WorstFit(Online):

    def _process(self, capacity: int, stream: WeightStream) -> Solution:
        
        solution = []
        for w in stream:
            if capacity >= w:
                solution.append(w)
        return solution
