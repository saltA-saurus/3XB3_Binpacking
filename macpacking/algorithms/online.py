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

# class FirstFit(Online):

#     def _process(self, capacity: int, stream: WeightStream) -> Solution:
        
#         bin_index = 0
#         solution = [[]]
#         bin_remaining = [0]*len(stream)
#         for w in stream:
#             j = 0
#             while j < bin_index:
#                 if bin_remaining[j] >= w:
#                     solution[bin_index] = solution[bin_index] - w 
#                     break
#                 j += 1

#             if j == bin_index:


#             if remaining >= w:
#                 solution[bin_index].append(w)
#                 remaining = remaining - w
#             else:
#                 bin_index += 1
#                 solution.append([w])
#                 remaining = capacity - w
#         return solution
    
    # # Create an array to store remaining space in bins
    # # there can be at most n bins
    # bin_rem = [0]*n
     
    # # Place items one by one
    # for i in range(n):
       
    #     # Find the first bin that can accommodate
    #     # weight[i]
    #     j = 0
    #     while( j < res):
    #         if (bin_rem[j] >= weight[i]):
    #             bin_rem[j] = bin_rem[j] - weight[i]
    #             break
    #         j+=1
             
    #     # If no bin could accommodate weight[i]
    #     if (j == res):
    #         bin_rem[res] = c - weight[i]
    #         res= res+1
    # return res

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
