from pandas.core.api import DataFrame as DataFrame
from pandas.core.dtypes.inference import is_list_like as is_list_like
from pathlib import Path
from typing import Optional, Sequence, Union

def read_spss(path: Union[str, Path], usecols: Optional[Sequence[str]]=..., convert_categoricals: bool=...) -> DataFrame: ...
