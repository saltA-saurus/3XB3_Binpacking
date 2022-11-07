import pyperf
import json
from os import listdir
from os.path import isfile, join, basename
from macpacking.algorithms.online import *
from macpacking.algorithms.offline import *
from macpacking.reader import BinppReader
from macpacking.algorithms.factory import BinpackerFactory


# We consider:
#   - 500 objects (N4)
#   - bin capacity of 120 (C2)
#   - and weight in the [20,100] interval (W2)
CASES = './_datasets/binpp/N4C2W2'


def main():
    cases = list_case_files(CASES)
    # list of all algorithms
    algorithms = ['NextFitOnline', 'FirstFitOnline', 'BestFitOnline', 'WorstFitOnline', 'NextFitOffline', 'FirstFitOffline', 'BestFitOffline', 'WorstFitOffline']
    kpis = run_bench(cases, algorithms)
    write_json(kpis)


def list_case_files(dir: str) -> list[str]:
    return sorted([f'{dir}/{f}' for f in listdir(dir) if isfile(join(dir, f))])

def write_json(kpis):
    with open("out/plot_data.json", 'w') as output:
        json.dump(kpis, output)

def get_kpis(solution, capacity):

    # number of bins
    bins_used = len(solution)

    # average weight of bins
    avg_weight_per_bin = 0
    for bin in solution:
        avg_weight_per_bin += sum(bin)
    avg_weight_per_bin /= bins_used
    
    # average space unused
    avg_unused_space = 0
    for bin in solution:
        avg_unused_space += capacity - sum(bin)
    avg_unused_space /= bins_used

    return (bins_used, avg_weight_per_bin, avg_unused_space)

def run_bench(cases: list[str], algorithms):
    # initial dictionary to be converted to json
    kpis = {}
    runner = pyperf.Runner()
    for algo in algorithms:
        # gets algorithm object from the string using a factory
        binpacker = BinpackerFactory.build(algo)
        # each key will be an algorithm, its value will be a new dictionary
        kpis[algo] = {}
        for case in cases:
            # each key is the current case (e.g. N2C2W4_C.BPP.txt)
            kpis[algo][basename(case)] = {}
            # name is the case name appended with the algorithm used to evaluate it
            name = basename(case) + '_' + algo
            data = BinppReader(case).online()
            bench = runner.bench_func(name, binpacker, data)
            if bench != None and bench.get_nrun() > 1:
                solution = binpacker(data)
                kpi_values = get_kpis(solution, data[0])
                kpis[algo][basename(case)]['Bins Used'] = kpi_values[0]
                kpis[algo][basename(case)]['Average Weight Per Bin'] = kpi_values[1]
                kpis[algo][basename(case)]['Average Unused Space Per Bin'] = kpi_values[2]
                kpis[algo][basename(case)]['Time'] = bench.mean()

                # TEST DELETE LATER
                print(kpis)
    return kpis
                

if __name__ == "__main__":
    main()