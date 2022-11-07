from .online import NextFit as NextFitOnline
from .online import BestFit as BestFitOnline
from .online import FirstFit as FirstFitOnline
from .online import WorstFit as WorstFitOnline
from .online import RefinedFirstFit as RefinedFirstFitOnline
from .offline import NextFit as NextFitOffline
from .offline import FirstFitDecreasing as FirstFitOffline
from .offline import BestFitDecreasing as BestFitOffline
from .offline import WorstFitDecreasing as WorstFitOffline
from .baseline import BenMaier
from .online import ListScheduling as ListSchedulingOnline
from .baseline import BenMaierMNP as BenMaierMNPOffline
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
            case 'ListSchedulingOnline':
                selected = ListSchedulingOnline()
            case 'BaselineMNPOffline':
                selected = BenMaierMNPOffline()
            case _:
                raise ValueError(name)
        return selected
