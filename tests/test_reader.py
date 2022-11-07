import pytest
from macpacking.reader import DatasetReader
from macpacking.reader import BinppReader
from macpacking.reader import JburkardtReader
from macpacking.reader import OracleReader


@pytest.mark.parametrize("reader", [BinppReader, OracleReader])
def test_domain(reader):
    with pytest.raises(ValueError):
        reader('unknown.txt')


# jburkardt format reads two files instead of one
@pytest.mark.parametrize("reader", [JburkardtReader])
def test_jburkardt_domain(reader):
    with pytest.raises(ValueError):
        reader('unknown_1.txt', 'unknown_2.txt')


def test_binpp_reader():
    dataset = '_datasets/binpp/N1C1W1/N1C1W1_B.BPP.txt'
    capacity = 100
    oracle = [
        8, 8, 12, 13, 13, 14, 15, 17, 18, 19, 20, 23, 30, 37, 37, 39, 40,
        43, 43, 44, 44, 50, 51, 61, 61, 62, 62, 63, 66, 67, 69, 70, 71,
        72, 75, 76, 76, 79, 83, 83, 88, 92, 92, 93, 93, 97, 97, 97, 99, 100
    ]
    reader: DatasetReader = BinppReader(dataset)
    assert capacity == reader.offline()[0]
    assert oracle == sorted(reader.offline()[1])


def test_jburkardt_reader():
    dataset_c = '_datasets/jburkardt/p01_c.txt'
    dataset_w = '_datasets/jburkardt/p01_w.txt'
    capacity = 100
    oracle = [
        3, 7, 11, 33, 33, 33, 50, 60, 70
    ]
    reader: DatasetReader = JburkardtReader(dataset_c, dataset_w)
    assert capacity == reader.offline()[0]
    assert oracle == sorted(reader.offline()[1])


def test_oracle_reader():
    dataset = '_datasets/binpp/N1C1W1/N1C1W1_B.BPP.txt'
    oracle_dataset = '_datasets/oracle.csv'
    optimal_solution = 31
    reader = OracleReader(dataset)
    assert optimal_solution == reader._load_data(oracle_dataset)
