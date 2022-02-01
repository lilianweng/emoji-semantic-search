from __future__ import annotations

import datetime
import sys
from decimal import Decimal
from fractions import Fraction
from io import RawIOBase, BufferedIOBase, TextIOBase, TextIOWrapper
from mmap import mmap
from os import PathLike
from numbers import Number

from pandas.core.arrays.base import ExtensionArray as ExtensionArray
from pandas.core.indexes.base import Index as Index
from typing import Any, AnyStr, Callable, Collection, Dict, Hashable, IO, List, Mapping, Optional, TypeVar, Union, \
    ByteString, Pattern

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

import numpy as np

from pandas import Interval as Interval, tseries
from pandas._libs import Period, Timedelta, Timestamp
from pandas.core.frame import DataFrame as DataFrame
from pandas.core.series import Series as Series
from pandas.tseries.offsets import DateOffset

# array-like
ArrayLike = Union[ExtensionArray, np.ndarray]
AnyArrayLike = Union[ArrayLike, 'Index', 'Series']

# scalar
PythonScalar = Union[str, int, float, bool]
DatetimeLikeScalar = Union[Period, Timestamp, Timedelta]
ExtraNumpyScalar = Union[np.object, np.object_, np.bytes, np.bytes_, np.unicode, np.unicode_, np.void]
NumpyBooleans = Union[np.bool, np.bool_, np.bool8, np.ScalarType]
NumpyIntegers = Union[np.byte, np.char, np.intc, np.int, np.int_, np.longlong, np.intp, np.int8, np.int16, np.int32, np.int64]
NumpyUnsignedIntegers = Union[np.ubyte, np.ushort, np.unintc, np.uint, np.ulonglong, np.uintp, np.uint8, np.uint16, np.uint32, np.uint64]
NumpyFloats = Union[np.half, np.double, np.float, np.float_, np.longfloat, np.float16, np.float32, np.float64, np.float128]
NumpyComplex = Union[np.csingle, np.complex, np.complex_, np.clongfloat, np.complex64, np.complex128, np.complex192, np.complex256]
NumpyScalar = Union[NumpyBooleans, NumpyIntegers, NumpyUnsignedIntegers, NumpyFloats, NumpyComplex]
PandasScalar = Union[Period, Timestamp, Timedelta, Interval]
Scalar = Union[PythonScalar, NumpyScalar, Decimal, ByteString, Fraction, DateOffset, Interval, Number, datetime.datetime, datetime.timedelta]

TimestampConvertible = Union[DatetimeLikeScalar, datetime.date, str, int, float]

Orientation = Literal['index', 'columns']
AxisOptionHorizontal = Literal[0, 'index']
AxisOptionVertical = Literal[1, 'columns']
AxisOption = Union[Literal[0, 1], Orientation]
OneDimensionalAxisOption = Literal[0, 'index']
ReplaceMethod = Literal['linear', 'time', 'index', 'values', 'pad', 'nearest', 'zero', 'slinear', 'quadratic', 'cubic', 'spline',
              'barycentric', 'polynomial', 'krogh', 'piecewise_polynomial', 'spline', 'pchip', 'akima', 'from_derivatives']
SortKind = Literal['quicksort', 'mergesort', 'heapsort']
NoneNumpyCompatible = Literal[None] # this is sometimes used to ensure Numpy compatibility
GeneralDuplicatesKeepStrategy = Literal['first', 'last', False]
InterpolationMethod = Literal['linear', 'lower', 'higher', 'midpoint', 'nearest']
NamedCorrelationMethod = Literal['pearson', 'kendall', 'spearman']
SearchSide = Literal['left', 'right']
NaSortPosition = Literal['first', 'last']
JoinType = Literal['left', 'right', 'outer', 'inner']
FillMethod = Literal['backfill', 'bfill', 'pad', 'ffill']
ErrorsStrategy = Literal['ignore', 'raise']
TimestampMethod = Literal['s', 'e', 'start', 'end']

UserCorrelationMethod = Callable[[np.ndarray, np.ndarray], Scalar]
CorrelationMethod = Union[NamedCorrelationMethod, UserCorrelationMethod]

Dtype: Any
T = TypeVar('T')

Buffer = Union[IO[AnyStr], RawIOBase, BufferedIOBase, TextIOBase, TextIOWrapper, mmap]
FileOrBuffer = Union[str, Buffer[T]]
FilePathOrBuffer = Union["PathLike[str]", FileOrBuffer[T]]

FrameOrSeries = Union[DataFrame, Series]
Axis = Union[str, int]
Label = Optional[Hashable]
Level = Union[Label, int]
Ordered = Optional[bool]
JSONSerializable = Union[PythonScalar, List, Dict]
Axes = Collection
Renamer = Union[Mapping[Label, Any], Callable[[Label], Label], Dict[Any, Any]]

FillValue = Union[Scalar, Dict[Any, Any], FrameOrSeries]

# Any plain Python or numpy function
Function = Union[np.func, Callable[..., Any]]
# Also including function names e.g. np.exp. 'sqrt'
FunctionOrName = Union[Function, str]
# Used in SelectionMixin and inheriting classes
AggregationFunction = Union[FunctionOrName, List[FunctionOrName], Dict[Axis, Union[FunctionOrName, List[FunctionOrName]]]]

F = TypeVar("F", bound=Function)

Column = Union[int, str]


# types of vectorized key functions for DataFrame::sort_values and
# DataFrame::sort_index, among others
ValueKeyFunc = Optional[Callable[["Series"], Union["Series", AnyArrayLike]]]
IndexKeyFunc = Optional[Callable[["Index"], Union["Index", AnyArrayLike]]]

# Actually google.auth.credentials.Credentials
GoogleCredentials = Any

# Replacement
RegexElement = Union[str, Pattern]
RegexArgument = Union[RegexElement, List[RegexElement], Dict[Column, RegexElement], Dict[Column, Dict[RegexElement, RegexElement]]]
ToReplace = Union[Scalar, Dict[Column, Scalar], Dict[Column, Dict[Scalar, Scalar]], List[Scalar], RegexArgument]
ReplaceValue = Union[Scalar, Dict[Column, Scalar], List[Scalar], RegexArgument]


Frequency = Union[DateOffset, tseries.offsets.liboffsets.BaseOffset, datetime.timedelta, str]

GroupByObject = Union[Label, List[Label], Function, Series, np.ndarray, Mapping[Label, Any]]
