from .online import NextFit as NextFitOnline, BestFit as BestFitOnline, FirstFit as FirstFitOnline, WorstFit as WorstFitOnline, RefinedFirstFit as RefinedFirstFitOnline
from .offline import NextFit as NextFitOffline, FirstFitDecreasing as FirstFitOffline, BestFitDecreasing as BestFitOffline, WorstFitDecreasing as WorstFitOffline
from .baseline import BenMaier
from ..model import BinPacker

class BinpackerFactory():

    def build(name: str) -> BinPacker:
        selected = None
        match name:
            case 'NextFitOnline':
                selected = NextFitOnline()
            case 'FirstFitOnline':
                selected = FirstFitOnline()
            case 'BestFitOnline':
                selected = BestFitOnline()
            case 'WorstFitOnline':
                selected = WorstFitOnline()
            case 'NextFitOffline':
                selected = NextFitOffline()
            case 'FirstFitOffline':
                selected = FirstFitOffline()
            case 'BestFitOffline':
                selected = BestFitOffline()
            case 'WorstFitOffline':
                selected = WorstFitOffline()
            case 'BaselineOffline':
                selected = BenMaier()
            case 'RefinedFirstFitOnline':
                selected = RefinedFirstFitOnline()
            case _:
                raise ValueError(name)
        return selected