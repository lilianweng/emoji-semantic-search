import numpy as np
from pandas._libs.tslibs import Timestamp as Timestamp
from pandas.tseries.offsets import DateOffset as DateOffset, Tick as Tick, generate_range as generate_range
from typing import Tuple

def generate_regular_range(start: Timestamp, end: Timestamp, periods: int, freq: DateOffset) -> Tuple[np.ndarray, str]: ...
