from abc import ABC, abstractmethod
from os import path
from random import shuffle, seed
from . import WeightSet, WeightStream


class DatasetReader(ABC):

    def offline(self) -> WeightSet:
        '''Return a WeightSet to support an offline algorithm'''
        (capacity, weights) = self._load_data_from_disk()
        seed(42)          # always produce the same shuffled result
        shuffle(weights)  # side effect shuffling
        return (capacity, weights)

    def online(self) -> WeightStream:
        '''Return a WeighStream, to support an online algorithm'''
        (capacity, weights) = self.offline()

        def iterator():  # Wrapping the contents into an iterator
            for w in weights:
                yield w  # yields the current value and moves to the next one

        return (capacity, iterator())

    @abstractmethod
    def _load_data_from_disk(self) -> WeightSet:
        '''Method that read the data from disk, depending on the file format'''
        pass


class BinppReader(DatasetReader):
    '''Read problem description according to the BinPP format'''

    def __init__(self, filename: str) -> None:
        if not path.exists(filename):
            raise ValueError(f'Unknown file [{filename}]')
        self.__filename = filename

    def _load_data_from_disk(self) -> WeightSet:
        with open(self.__filename, 'r') as reader:
            nb_objects: int = int(reader.readline())
            capacity: int = int(reader.readline())
            weights = []
            for _ in range(nb_objects):
                weights.append(int(reader.readline()))
            return (capacity, weights)


class JburkardtReader(DatasetReader):
    '''Read problem description according to the Jburkardt format'''

    def __init__(self, filename_c: str, filename_w: str) -> None:
        if not path.exists(filename_c):
            raise ValueError(f'Unknown file [{filename_c}]')
        if not path.exists(filename_w):
            raise ValueError(f'Unknown file [{filename_w}]')
        self.__filename_c = filename_c
        self.__filename_w = filename_w

    def _load_data_from_disk(self) -> WeightSet:
        with open(self.__filename_c, 'r') as reader:
            capacity: int = int(reader.readline())
        with open(self.__filename_w, 'r') as reader:
            weights = []
            for line in reader:
                line = line.strip()
                if line == '':
                    continue
                weights.append(int(line))
            return (capacity, weights)


class OracleReader:
    '''Read optimal nb_bins according to the Oracle format'''

    def __init__(self, filename: str) -> None:
        if not path.exists(filename):
            raise ValueError(f'Unknown file [{filename}]')
        self.__filename = filename

    def _load_data(self, filename: str) -> int:
        optimal = []
        oracle = filename
        with open(oracle, 'r') as file:
            next(file)
            for line in file:
                row = line.split(",")
                optimal.append((row[0], row[1].replace("\n", "")))

        for problem in optimal:
            if problem[0] in self.__filename:
                optimal_solution = int(problem[1])

        return optimal_solution
