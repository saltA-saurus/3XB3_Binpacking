from macpacking.reader import DatasetReader, BinppReader, OracleReader
from macpacking.model  import Online, Offline
from matplotlib.ticker import MaxNLocator
import macpacking.algorithms.offline as offline
import macpacking.algorithms.online as online
import macpacking.algorithms.baseline as baseline
from macpacking.algorithms.factory import BinpackerFactory
import matplotlib.pyplot as plt
from graph import PlotGraph
from os.path import basename

# We consider:
#   - 50 objects (N1)
#   - bin capacity of 100 (C1)
#   - and weight in the [8,100] interval (W1)
dataset_small = '_datasets/binpp/N1C1W1/N1C1W1_B.BPP.txt'
# We consider:
#   - 100 objects (N2)
#   - bin capacity of 120 (C2)
#   - and weight in the [20,99] interval (W2)
dataset_medium = '_datasets/binpp/N2C2W2/N2C2W2_B.BPP.txt'
# We consider:
#   - 500 objects (N4)
#   - bin capacity of 150 (C3)
#   - and weight in the [30,100] interval (W4)
dataset_large = '_datasets/binpp/N4C3W4/N4C3W4_B.BPP.txt'
# We consider:
#   - 200 objects
#   - bin capacity of 100000
#   - and weight in the [20000,34955] interval
dataset_hard = '_datasets/binpp-hard/HARD5.BPP.txt'
# We consider:
#   - 500 objects (N4)
#   - bin capacity of 100 (C1)
#   - and weight in the [30,100] interval (W4)
dataset_smallC_largeN = '_datasets/binpp/N4C1W4/N4C1W4_B.BPP.txt'
# We consider:
#   - 50 objects (N1)
#   - bin capacity of 150 (C3)
#   - and weight in the [2,95] interval (W1)
dataset_smallN_largeC = '_datasets/binpp/N1C3W1/N1C3W1_B.BPP.txt'
oracle_dataset = '_datasets/oracle.csv'
cases = [dataset_small, dataset_medium, dataset_large, dataset_hard, dataset_smallC_largeN, dataset_smallN_largeC]
titles = ['Small Dataset (N1C1W1)', 'Medium Dataset (N2C2W2)', 'Large Dataset (N4C3W4)', 'Hard Dataset (HARD5)', 'Small C & Large N (N4C1W4)', 'Large C & Small N (N1C3W1)']
algorithms = ['BaselineOffline', 'NextFitOnline', 'FirstFitOnline', 'BestFitOnline', 'WorstFitOnline', 'NextFitOffline', 'FirstFitOffline', 'BestFitOffline', 'WorstFitOffline']
basename_cases = [basename(x) for x in cases]

for i in range(len(cases)):

    optimal_solution = OracleReader([i])
    improvement_margin = []

    reader: DatasetReader = BinppReader(cases[i])
    print(f'Dataset: {basename(cases[i])}')
    print(f'Optimal Solution: {optimal_solution._load_data(oracle_dataset)}\n')

    strategy: BinpackerFactory.build('')
    result = strategy(reader.offline())
    improvement_margin.append(len(result) - optimal_solution._load_data(oracle_dataset))

    strategy: Offline = offline.FirstFitDecreasing()
    result = strategy(reader.offline())
    improvement_margin.append(len(result) - optimal_solution._load_data(oracle_dataset))

    strategy: Offline = offline.BestFitDecreasing()
    result = strategy(reader.offline())
    improvement_margin.append(len(result) - optimal_solution._load_data(oracle_dataset))

    strategy: Offline = offline.WorstFitDecreasing()
    result = strategy(reader.offline())
    improvement_margin.append(len(result) - optimal_solution._load_data(oracle_dataset))

    strategy: Online = online.FirstFit()
    result = strategy(reader.online())
    improvement_margin.append(len(result) - optimal_solution._load_data(oracle_dataset))

    strategy: Online = online.BestFit()
    result = strategy(reader.online())
    improvement_margin.append(len(result) - optimal_solution._load_data(oracle_dataset))

    strategy: Online = online.WorstFit()
    result = strategy(reader.online())
    improvement_margin.append(len(result) - optimal_solution._load_data(oracle_dataset))

    # X and Y Axis
    # xAxis = [algo for algo in algorithms]
    # yAxis = [val for val in improvement_margin]

    # # Bar graph
    # fig = plt.figure().gca()
    # plt.bar(xAxis,yAxis, color='maroon')
    # plt.xlabel('Algorithms')
    # plt.ylabel('Improvement Margin')
    # plt.xticks(rotation=90)
    # plt.title(titles[cases.index(cases)])
    # fig.yaxis.set_major_locator(MaxNLocator(integer=True))

    # plt.show()