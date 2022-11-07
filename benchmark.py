import pyperf
import json
from os import listdir
from os.path import isfile, join, basename
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
    algorithms = [
        'NextFitOnline', 'FirstFitOnline',
        'BestFitOnline', 'WorstFitOnline',
        'NextFitOffline', 'FirstFitOffline',
        'BestFitOffline', 'WorstFitOffline',
        'RefinedFirstFitOnline'
    ]
    # algorithms = ['BestFitOffline']
    kpis = run_bench(cases, algorithms)
    write_json(kpis)


def list_case_files(dir: str) -> list[str]:
    return sorted([f'{dir}/{f}' for f in listdir(dir) if isfile(join(dir, f))])


def write_json(kpis):
    with open("out/plot_data.json", 'w') as output:
        json.dump(kpis, output)


def get_kpis(solution, capacity):

    # number of bins
    bn_used = len(solution)

    # average weight of bins
    avg_weight_per_bin = 0
    for bin in solution:
        avg_weight_per_bin += sum(bin)
    avg_weight_per_bin /= bn_used

    # average space unused
    avg_unused_space = 0
    for bin in solution:
        avg_unused_space += capacity - sum(bin)
    avg_unused_space /= bn_used

    # standard deviation
    standard_deviation = 0
    for bin in solution:
        standard_deviation += (sum(bin) - avg_weight_per_bin)
    standard_deviation = (((standard_deviation)**2)/len(solution))**0.5

    return (bn_used, avg_weight_per_bin, avg_unused_space, standard_deviation)


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
            b_c = basename(case)
            # each key is the current case (e.g. N2C2W4_C.BPP.txt)
            kpis[algo][b_c] = {}
            # name is the case name appended with the
            # algorithm used to evaluate it
            name = b_c + '_' + algo
            data = BinppReader(case).online()
            bench = runner.bench_func(name, binpacker, data)
            if bench is not None and bench.get_nrun() > 1:
                solution = binpacker(data)
                kpi_values = get_kpis(solution, data[0])
                kpis[algo][b_c]['Bins Used'] = kpi_values[0]
                kpis[algo][b_c]['Average Weight Per Bin'] = kpi_values[1]
                kpis[algo][b_c]['Average Unused Space Per Bin'] = kpi_values[2]
                kpis[algo][b_c]['Time'] = bench.mean()
                kpis[algo][b_c]['Standard Deviation'] = kpi_values[3]

    return kpis


if __name__ == "__main__":
    main()
