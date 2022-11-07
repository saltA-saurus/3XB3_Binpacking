from macpacking.reader import DatasetReader, BinppReader
from macpacking.model  import Online, Offline
import macpacking.algorithms.offline as offline
import macpacking.algorithms.online as online
import macpacking.algorithms.baseline as baseline

def test_benmaier_baseline():
    dataset = '_datasets/binpp/N1C1W1/N1C1W1_B.BPP.txt'
    nb_bins = 31
    oracle = [
        [40], [43, 43, 14], [50, 44], [51, 44], [61], [61, 39], [62], 
        [62, 37], [63, 37], [66], [67], [69], [70, 30], [71], [72, 13, 13], 
        [75, 18], [76, 19], [76, 23], [79, 20], [83, 15], [83, 17], [88, 12], 
        [92, 8], [92, 8], [93], [93], [97], [97], [97], [99], [100]
    ]
    reader: DatasetReader = BinppReader(dataset)
    strategy: Offline = baseline.BenMaier()
    result = strategy(reader.offline())
    assert nb_bins == len(result)
    assert oracle == sorted(result)

def test_benmaiermnp_baseline():
    dataset = '_datasets/binpp/N4C1W1/N4C1W1_A.BPP.txt'
    nb_bins = 100
    oracle = [
        [77, 77, 53, 22, 4], [78, 76, 54, 20, 15], [78, 76, 54, 20, 15], 
        [78, 76, 54, 21, 4], [78, 76, 54, 21, 5], [78, 76, 54, 21, 5], 
        [78, 77, 46, 27, 15], [79, 75, 54, 21, 5], [79, 75, 54, 22, 1], 
        [79, 75, 55, 20, 6], [80, 74, 55, 20, 6], [80, 74, 56, 19, 7], 
        [80, 75, 46, 27, 15], [80, 75, 46, 27, 15], [80, 75, 46, 27, 16], 
        [81, 73, 56, 19, 7], [81, 73, 56, 20, 1], [81, 74, 47, 26, 16], 
        [81, 74, 47, 26, 17], [82, 73, 47, 27, 7], [82, 73, 48, 25, 17], 
        [82, 73, 48, 26, 7], [82, 73, 48, 26, 7], [83, 71, 56, 20, 1], 
        [83, 72, 48, 26, 7], [83, 72, 48, 26, 8], [83, 72, 48, 26, 8], 
        [83, 72, 49, 25, 8], [83, 73, 38, 35, 9], [84, 71, 49, 25, 9], 
        [84, 71, 49, 25, 9], [85, 70, 50, 24, 9], [85, 71, 38, 35, 9], 
        [85, 71, 38, 35, 10], [86, 70, 38, 35, 10], [86, 70, 39, 33, 17], 
        [86, 70, 39, 33, 17], [86, 70, 39, 34, 10], [86, 70, 39, 34, 10], 
        [86, 70, 40, 32, 17], [87, 69, 40, 33, 10], [87, 69, 40, 33, 10], 
        [87, 69, 40, 33, 10], [87, 69, 41, 31, 17], [87, 70, 37, 35, 10], 
        [87, 70, 37, 35, 11], [88, 67, 50, 24, 11], [88, 67, 50, 24, 11], 
        [88, 68, 41, 32, 11], [88, 68, 41, 32, 11], [89, 66, 50, 24, 11], 
        [89, 66, 50, 24, 11], [89, 67, 41, 32, 11], [89, 67, 41, 32, 11], 
        [89, 67, 42, 30, 17], [90, 65, 51, 23, 12], [90, 65, 51, 23, 12], 
        [90, 66, 42, 30, 18], [91, 64, 51, 24, 1], [91, 64, 51, 24, 1], 
        [91, 64, 52, 23, 1], [91, 65, 42, 31, 12], [92, 63, 52, 23, 2], 
        [92, 63, 52, 23, 2], [92, 64, 42, 31, 13], [93, 63, 42, 31, 13], 
        [93, 63, 42, 31, 13], [93, 63, 42, 31, 13], [94, 62, 42, 31, 13], 
        [94, 62, 42, 31, 13], [94, 62, 42, 31, 13], [94, 63, 37, 36, 2], 
        [95, 61, 43, 29, 18], [95, 62, 37, 36, 2], [95, 62, 37, 36, 2], 
        [95, 62, 37, 36, 3], [95, 62, 37, 36, 3], [96, 60, 43, 29, 18], 
        [96, 60, 43, 29, 18], [96, 60, 43, 29, 18], [96, 60, 43, 29, 19], 
        [96, 60, 43, 30, 13], [96, 61, 37, 36, 3], [96, 61, 38, 34, 13], 
        [97, 58, 53, 22, 4], [97, 58, 53, 22, 4], [97, 58, 53, 22, 4], 
        [97, 59, 43, 30, 14], [97, 59, 44, 28, 19], [97, 59, 44, 28, 19], 
        [97, 60, 38, 34, 14], [98, 57, 53, 22, 4], [98, 58, 44, 28, 19], 
        [98, 58, 44, 28, 19], [98, 58, 45, 27, 19], [99, 57, 45, 28, 14], 
        [99, 57, 45, 28, 14], [99, 57, 45, 28, 15], [99, 57, 46, 27, 15], 
        [100, 56, 46, 27, 15]
    ]
    reader: DatasetReader = BinppReader(dataset)
    strategy: Offline = baseline.BenMaierMNP()
    result = strategy(reader.offline())
    assert nb_bins == len(result)
    assert oracle == sorted(result)

def test_nextfit_online():
    dataset = '_datasets/binpp/N1C1W1/N1C1W1_B.BPP.txt'
    nb_bins = 36
    oracle = [
        [13, 61], [15, 70], [19], [20, 23], [37, 43, 14], [39], [40, 8, 18], 
        [43], [44], [44, 50], [51, 30], [61], [62], [62, 37], [63, 17, 13], 
        [66], [67], [69], [71], [72], [75], [76], [76, 8, 12], [79], [83], 
        [83], [88], [92], [92], [93], [93], [97], [97], [97], [99], [100]
    ]
    reader: DatasetReader = BinppReader(dataset)
    strategy: Online = online.NextFit()
    result = strategy(reader.online())
    assert nb_bins == len(result)
    assert oracle == sorted(result)

def test_terrible_online():
    dataset = '_datasets/binpp/N1C1W1/N1C1W1_B.BPP.txt'
    nb_bins = 50
    oracle = [
        [8], [8], [12], [13], [13], [14], [15], [17], [18], [19], [20], [23], 
        [30], [37], [37], [39], [40], [43], [43], [44], [44], [50], [51], [61], 
        [61], [62], [62], [63], [66], [67], [69], [70], [71], [72], [75], [76], 
        [76], [79], [83], [83], [88], [92], [92], [93], [93], [97], [97], [97], 
        [99], [100]
    ]
    reader: DatasetReader = BinppReader(dataset)
    strategy: Online = online.Terrible()
    result = strategy(reader.online())
    assert nb_bins == len(result)
    assert oracle == sorted(result)

def test_firstfit_online():
    dataset = '_datasets/binpp/N1C1W1/N1C1W1_B.BPP.txt'
    nb_bins = 31
    oracle = [
        [40, 44], [44, 43, 13], [50, 43], [51, 39], [61, 13, 20], [61, 37], 
        [62, 23, 15], [62, 37], [63], [66, 30], [67], [69, 8, 18], [70], [71], 
        [72, 14, 12], [75], [76], [76], [79, 19], [83], [83, 17], [88, 8], 
        [92], [92], [93], [93], [97], [97], [97], [99], [100]
    ]
    reader: DatasetReader = BinppReader(dataset)
    strategy: Online = online.FirstFit()
    result = strategy(reader.online())
    assert nb_bins == len(result)
    assert oracle == sorted(result)

def test_bestfit_online():
    dataset = '_datasets/binpp/N1C1W1/N1C1W1_B.BPP.txt'
    nb_bins = 31
    oracle = [
        [40, 44, 12], [44, 43, 13], [50, 43], [51], [61], [61, 39], [62], 
        [62, 37], [63, 37], [66], [67, 30], [69, 17, 14], [70, 18, 8], [71], 
        [72, 23], [75], [76], [76, 19], [79, 20], [83, 13], [83, 15], [88, 8], 
        [92], [92], [93], [93], [97], [97], [97], [99], [100]
    ]
    reader: DatasetReader = BinppReader(dataset)
    strategy: Online = online.BestFit()
    result = strategy(reader.online())
    assert nb_bins == len(result)
    assert oracle == sorted(result)

def test_worstfit_online():
    dataset = '_datasets/binpp/N1C1W1/N1C1W1_B.BPP.txt'
    nb_bins = 33
    oracle = [
        [37, 43], [39, 19], [40, 8, 18, 13], [44, 43], [44, 50], [51, 30], 
        [61, 13], [61, 20], [62, 23], [62, 37], [63, 17], [66, 15], [67, 14], 
        [69, 8], [70, 12], [71], [72], [75], [76], [76], [79], [83], [83], [88], 
        [92], [92], [93], [93], [97], [97], [97], [99], [100]
    ]
    reader: DatasetReader = BinppReader(dataset)
    strategy: Online = online.WorstFit()
    result = strategy(reader.online())
    assert nb_bins == len(result)
    assert oracle == sorted(result)

def test_refinedfirstfit_online():
    dataset = '_datasets/binpp/N1C1W1/N1C1W1_B.BPP.txt'
    nb_bins = 36
    oracle = [
        [13, 20, 23, 15, 8, 18], [17, 13, 14, 8, 12, 30], [19], [37, 39], 
        [37, 40], [43], [44, 43], [44, 50], [51], [61], [61], [62], [62], [63], 
        [66], [67], [69], [70], [71], [72], [75], [76], [76], [79], [83], [83], 
        [88], [92], [92], [93], [93], [97], [97], [97], [99], [100]
    ]
    reader: DatasetReader = BinppReader(dataset)
    strategy: Online = online.RefinedFirstFit()
    result = strategy(reader.online())
    assert nb_bins == len(result)
    assert oracle == sorted(result)

def test_listscheduling_online():
    dataset = '_datasets/binpp/N4C1W1/N4C1W1_A.BPP.txt'
    nb_bins = 100
    oracle = [
        [5, 49, 36, 4, 94, 99], [8, 26, 83, 81, 10], [9, 48, 58, 63, 61], 
        [10, 27, 85, 87], [12, 32, 42, 54, 37, 35], [12, 80, 13, 42, 23, 95], 
        [13, 20, 3, 34, 22, 42, 3, 87], [13, 62, 13, 68, 1, 17, 39], 
        [15, 34, 33, 18, 35, 14, 55, 87], [15, 66, 11, 23, 42, 92], [16, 91, 90, 40], 
        [17, 20, 69, 15, 7, 19, 24, 92], [18, 76, 19, 31, 12, 80], 
        [18, 84, 30, 19, 63], [19, 28, 29, 23, 86, 62], [20, 2, 98, 28, 70], 
        [20, 14, 44, 76, 9, 32, 53], [20, 65, 76, 58], [21, 94, 45, 60], 
        [22, 46, 90, 31, 36], [24, 4, 38, 10, 47, 43, 11, 70], [24, 42, 33, 51, 73], 
        [25, 43, 86, 39, 35], [25, 48, 73, 48, 89], [27, 19, 13, 97, 41, 90], 
        [28, 57, 89, 91], [29, 71, 76, 48], [31, 32, 15, 52, 71, 83], 
        [31, 32, 77, 22, 81], [31, 99, 42, 59], [33, 96, 87], [34, 42, 2, 95, 33], 
        [36, 7, 18, 43, 86, 31], [36, 27, 6, 58, 10, 95], 
        [37, 11, 9, 56, 27, 15, 18, 32, 31], [37, 60, 62, 29, 17], [38, 70, 17, 51, 86], 
        [40, 69, 24, 57, 3, 97], [43, 40, 79, 59], [45, 8, 48, 24, 82], [45, 54, 49, 93], 
        [46, 41, 56, 7, 94], [46, 69, 35, 64], [50, 11, 21, 6, 68, 13, 74], 
        [50, 96, 31, 17, 97], [51, 96, 25, 37], [53, 37, 2, 73, 10, 58], 
        [53, 38, 37, 13, 37, 60], [53, 71, 14, 89], [54, 22, 11, 86, 15, 69], 
        [54, 30, 11, 9, 81, 9, 75], [54, 56, 73, 21, 97], [54, 67, 19, 84], 
        [56, 19, 37, 73, 27], [58, 16, 22, 97, 73], [59, 87, 30, 24, 23], 
        [60, 39, 27, 1, 31, 7, 88], [60, 83, 41, 82], [60, 91, 28, 57], 
        [61, 10, 50, 33, 27, 4, 4, 75], [62, 54, 41, 35, 38], [62, 61, 79, 72], 
        [63, 7, 15, 63, 38, 81], [63, 85, 75], [64, 57, 67, 11, 1, 88], [64, 78, 70], 
        [65, 29, 42, 82], [66, 38, 40, 2, 44, 26], [66, 72, 43, 2, 75], 
        [67, 46, 65, 13, 77], [70, 42, 94], [70, 44, 97], [71, 1, 74, 56, 74], 
        [71, 1, 96, 67], [72, 52, 99], [73, 26, 42, 52, 43], [77, 13, 11, 28, 98], 
        [78, 4, 17, 64, 49], [78, 7, 19, 46, 4, 1, 48, 23], [78, 26, 86, 25], 
        [78, 80, 28, 21], [79, 95, 67], [80, 35, 100], [80, 63, 72], [82, 51, 36, 30, 28], 
        [83, 24, 45, 8, 75], [83, 76, 70], [85, 47, 47, 89], [87, 46, 57, 53], 
        [88, 5, 93, 17, 70], [88, 50, 44, 62], [89, 15, 26, 39, 20, 50], 
        [91, 75, 5, 26, 36], [92, 62, 70], [95, 27, 43, 11, 96], [96, 22, 58, 41], 
        [97, 29, 14, 55, 96], [98, 26, 10, 10, 83], [98, 74, 78], [99, 34, 93]
    ]
    reader: DatasetReader = BinppReader(dataset)
    strategy: Online = online.ListScheduling()
    result = strategy(reader.online())
    assert nb_bins == len(result)
    assert oracle == sorted(result)

def test_nextfit_offline():
    dataset = '_datasets/binpp/N1C1W1/N1C1W1_B.BPP.txt'
    nb_bins = 35
    oracle = [
        [14, 13, 13, 12, 8, 8], [20, 19, 18, 17, 15], [37, 30, 23], [39, 37], 
        [43, 40], [44, 43], [50, 44], [51], [61], [61], [62], [62], [63], [66], [67], 
        [69], [70], [71], [72], [75], [76], [76], [79], [83], [83], [88], [92], [92], 
        [93], [93], [97], [97], [97], [99], [100]
    ]
    reader: DatasetReader = BinppReader(dataset)
    strategy: Offline = offline.NextFit()
    result = strategy(reader.online())
    assert nb_bins == len(result)
    assert oracle == sorted(result)

def test_firstfitdecreasing_offline():
    dataset = '_datasets/binpp/N1C1W1/N1C1W1_B.BPP.txt'
    nb_bins = 31
    oracle = [
        [40], [43, 43], [50, 44], [51, 44], [61], [61, 39], [62], [62, 37], [63, 37], 
        [66], [67], [69], [70, 30], [71, 13], [72, 14, 13], [75, 18], [76, 19], 
        [76, 23], [79, 20], [83, 15], [83, 17], [88, 12], [92, 8], [92, 8], [93], [93], 
        [97], [97], [97], [99], [100]
    ]
    reader: DatasetReader = BinppReader(dataset)
    strategy: Offline = offline.FirstFitDecreasing()
    result = strategy(reader.online())
    assert nb_bins == len(result)
    assert oracle == sorted(result)

def test_bestfitdecreasing_offline():
    dataset = '_datasets/binpp/N1C1W1/N1C1W1_B.BPP.txt'
    nb_bins = 31
    oracle = [
        [40], [43, 43, 14], [50, 44], [51, 44], [61], [61, 39], [62], [62, 37], 
        [63, 37], [66], [67], [69], [70, 30], [71], [72, 13, 13], [75, 18], [76, 19], 
        [76, 23], [79, 20], [83, 15], [83, 17], [88, 12], [92, 8], [92, 8], [93], [93], 
        [97], [97], [97], [99], [100]
    ]
    reader: DatasetReader = BinppReader(dataset)
    strategy: Offline = offline.BestFitDecreasing()
    result = strategy(reader.online())
    assert nb_bins == len(result)
    assert oracle == sorted(result)

def test_worstfitdecreasing_offline():
    dataset = '_datasets/binpp/N1C1W1/N1C1W1_B.BPP.txt'
    nb_bins = 31
    oracle = [
        [40, 39], [43, 43], [50, 44], [51, 44], [61, 37], [61, 37], [62, 23], [62, 30], 
        [63, 20], [66, 19], [67, 18], [69, 17], [70, 15], [71, 14], [72, 13], [75, 13], 
        [76, 8], [76, 12], [79, 8], [83], [83], [88], [92], [92], [93], [93], [97], 
        [97], [97], [99], [100]
    ]
    reader: DatasetReader = BinppReader(dataset)
    strategy: Offline = offline.WorstFitDecreasing()
    result = strategy(reader.online())
    assert nb_bins == len(result)
    assert oracle == sorted(result)