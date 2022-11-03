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
            # if there is enough capacity for the weight
            # create a bin and add the weight to the bin
            if capacity >= w:
                solution.append([w])
        return solution

class FirstFit(Online):

    def _process(self, capacity: int, stream: WeightStream) -> Solution:
        
        bin_index = 0
        solution = []
        # create a list of remaining capacities for each bin
        # created
        bin_remaining = []
        for w in stream:
            j = 0
            # iterate from the first to last bin
            # to find a bin with space remaining for the weight
            while j < bin_index:
                if bin_remaining[j] >= w:
                    solution[j].append(w)
                    bin_remaining[j] -= w 
                    break
                j += 1

            # if no space remaining in previous bins,
            # create a new bin for the weight as well
            # as a corresponding remaining capacity
            if j == bin_index:
                solution.append([w])
                bin_remaining.append(capacity)
                bin_remaining[bin_index] = capacity - w
                bin_index += 1

        return solution

class BestFit(Online):

    def _process(self, capacity: int, stream: WeightStream) -> Solution:
        
        bin_index = 0
        solution = []
        bin_remaining = []
        for w in stream:
            j = 0
            # minimum space left in bin and index of best bin
            min = capacity + 1
            bi = 0 

            # locate a bin with space remaining and fill it up
            # as much as possible, until no other weights can fit in it
            for j in range(bin_index):
                if (bin_remaining[j] >= w and (bin_remaining[j] - w) < min):
                    
                    bi = j
                    min = bin_remaining[j] - w 

            # create a new bin if no other bins have 
            # remaining capacity
            if min == (capacity + 1):
                solution.append([w])
                bin_remaining.append(capacity)
                bin_remaining[bin_index] = capacity - w
                bin_index += 1
            # assign weight to best bin
            else:
                solution[bi].append(w)
                bin_remaining[bi] -= w

        return solution

class WorstFit(Online):

    def _process(self, capacity: int, stream: WeightStream) -> Solution:
        
        solution = []

        # Initialize result (Count of bins)
        bin_index = 0
        bin_remaining = []
        
        # Place items one by one
        for w in stream:
            # Find the best bin that can accommodate
            # w
    
            # Initialize maximum space left and index
            # of worst bin
            mx,wi = -1,0
    
            for j in range(bin_index):
                if (bin_remaining[j] >= w and bin_remaining[j] - w > mx):
                    wi = j
                    mx = bin_remaining[j] - w
                
    
            # If no bin could accommodate w[i],
            # create a new bin
            if (mx == -1):
                solution.append([w])
                bin_remaining.append(capacity)
                bin_remaining[bin_index] = capacity - w
                bin_index += 1
            
            else: # Assign the item to best bin
                solution[wi].append(w)
                bin_remaining[wi] -= w
        
        return solution
