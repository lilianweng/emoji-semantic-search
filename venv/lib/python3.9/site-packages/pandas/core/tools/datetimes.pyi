from datetime import datetime
from pandas._typing import ArrayLike as ArrayLike, TimestampConvertible
from pandas.core.dtypes.generic import ABCDataFrame as ABCDataFrame, ABCDatetimeIndex as ABCDatetimeIndex, ABCIndex as ABCIndex, ABCIndexClass as ABCIndexClass, ABCSeries as ABCSeries
from typing import Any, Optional, TypeVar, Union, List, Tuple

ArrayConvertible = Union[List[Any], Tuple[Any], ArrayLike, ABCSeries]
Scalar = Union[int, float, str]
DatetimeScalar = TypeVar('DatetimeScalar', Scalar, datetime)
DatetimeScalarOrArrayConvertible = Union[DatetimeScalar, List[Any], Tuple[Any], ArrayLike, ABCSeries]

def should_cache(arg: ArrayConvertible, unique_share: float=..., check_count: Optional[int]=...) -> bool: ...
def to_datetime(arg: Any, errors: str = ..., dayfirst: bool = ..., yearfirst: bool = ..., utc: Optional[Any] = ..., format: Optional[Any] = ..., exact: bool = ..., unit: Optional[Any] = ..., infer_datetime_format: bool = ..., origin: TimestampConvertible = ..., cache: bool = ...) -> Any: ...
def to_time(arg: Any, format: Optional[Any] = ..., infer_time_format: bool = ..., errors: str = ...) -> Any: ...
