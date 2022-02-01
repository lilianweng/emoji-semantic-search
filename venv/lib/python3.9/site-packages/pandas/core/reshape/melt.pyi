from pandas.core.arrays import Categorical as Categorical

from pandas.core.dtypes.generic import ABCMultiIndex as ABCMultiIndex
from pandas.core.dtypes.missing import notna as notna
from pandas.core.frame import DataFrame as DataFrame
from pandas.core.indexes.base import Index as Index
from pandas.core.reshape.concat import concat as concat
from pandas.core.tools.numeric import to_numeric as to_numeric
from pandas.util._decorators import Appender as Appender, deprecate_kwarg as deprecate_kwarg
from typing import Any

def melt(frame: DataFrame, id_vars: Any = ..., value_vars: Any = ..., var_name: Any = ..., value_name: Any = ..., col_level: Any = ..., ignore_index: bool = ...) -> DataFrame: ...
def lreshape(data: DataFrame, groups: Any, dropna: bool=..., label: Any = ...) -> DataFrame: ...
def wide_to_long(df: DataFrame, stubnames: Any, i: Any, j: Any, sep: str=..., suffix: str=...) -> DataFrame: ...
