from collections import abc
from pandas._typing import ArrayLike, FilePathOrBuffer as FilePathOrBuffer, Scalar
from pandas.core.frame import DataFrame as DataFrame
from typing import Any, Callable, Dict, List, Literal, Optional, AnyStr, overload, Sequence, Union

# not checking types in Callable params for read_csv, the documentation is too ambiguous
AnyCallable = Callable[[Any], Any]

@overload
def read_csv(filepath_or_buffer: Any, sep: str = ..., delimiter: Optional[str] = ..., header: Optional[Union[int, List[int], str]] = ...,
             names: Optional[ArrayLike] = ..., index_col: Optional[Union[int, str, Sequence[int], Sequence[str], bool]] = None,
             usecols: Optional[Union[ArrayLike, AnyCallable]] = ..., squeeze: bool = ..., prefix: str = ..., mangle_dupe_cols: bool = ...,
             dtype: Any = ..., engine: Optional[Literal['c', 'python']] = ..., converters: Optional[Dict[Any, Any]] = ...,
             true_values: Optional[List[Any]] = ..., false_values: Optional[List[Any]] = ..., skipinitialspace: bool = ...,
             skiprows: Optional[Union[ArrayLike, int, AnyCallable]] = ..., skipfooter: int = ..., nrows: Optional[int] = ...,
             na_values: Optional[Union[Scalar, str, ArrayLike, Dict[Any, Any]]] = ..., keep_default_na: bool = ...,
             na_filter: bool = ..., verbose: bool = ..., skip_blank_lines: bool = ...,
             parse_dates: Union[bool, List[int], List[str], List[List[Any]], Dict[Any, Any]] = ..., infer_datetime_format: bool = ...,
             keep_date_col: bool = ..., date_parser: Optional[AnyCallable] = ..., dayfirst: bool = ..., cache_dates: bool = ...,
             *, iterator: Literal[True], chunksize: Optional[int] = ..., **kwargs: Any) -> TextFileReader: ...

@overload
def read_csv(filepath_or_buffer: Any, sep: str = ..., delimiter: Optional[str] = ..., header: Optional[Union[int, List[int], str]] = ...,
             names: Optional[ArrayLike] = ..., index_col: Optional[Union[int, str, Sequence[int], Sequence[str], bool]] = None,
             usecols: Optional[Union[ArrayLike, AnyCallable]] = ..., squeeze: bool = ..., prefix: str = ..., mangle_dupe_cols: bool = ...,
             dtype: Any = ..., engine: Optional[Literal['c', 'python']] = ..., converters: Optional[Dict[Any, Any]] = ...,
             true_values: Optional[List[Any]] = ..., false_values: Optional[List[Any]] = ..., skipinitialspace: bool = ...,
             skiprows: Optional[Union[ArrayLike, int, AnyCallable]] = ..., skipfooter: int = ..., nrows: Optional[int] = ...,
             na_values: Optional[Union[Scalar, str, ArrayLike, Dict[Any, Any]]] = ..., keep_default_na: bool = ...,
             na_filter: bool = ..., verbose: bool = ..., skip_blank_lines: bool = ...,
             parse_dates: Union[bool, List[int], List[str], List[List[Any]], Dict[Any, Any]] = ..., infer_datetime_format: bool = ...,
             keep_date_col: bool = ..., date_parser: Optional[AnyCallable] = ..., dayfirst: bool = ..., cache_dates: bool = ...,
             *, iterator: Literal[False] = ..., chunksize: int, **kwargs: Any) -> TextFileReader: ...

@overload
def read_csv(filepath_or_buffer: Any, sep: str = ..., delimiter: Optional[str] = ..., header: Optional[Union[int, List[int], str]] = ...,
             names: Optional[ArrayLike] = ..., index_col: Optional[Union[int, str, Sequence[int], Sequence[str], bool]] = None,
             usecols: Optional[Union[ArrayLike, AnyCallable]] = ..., squeeze: bool = ..., prefix: str = ..., mangle_dupe_cols: bool = ...,
             dtype: Any = ..., engine: Optional[Literal['c', 'python']] = ..., converters: Optional[Dict[Any, Any]] = ...,
             true_values: Optional[List[Any]] = ..., false_values: Optional[List[Any]] = ..., skipinitialspace: bool = ...,
             skiprows: Optional[Union[ArrayLike, int, AnyCallable]] = ..., skipfooter: int = ..., nrows: Optional[int] = ...,
             na_values: Optional[Union[Scalar, str, ArrayLike, Dict[Any, Any]]] = ..., keep_default_na: bool = ...,
             na_filter: bool = ..., verbose: bool = ..., skip_blank_lines: bool = ...,
             parse_dates: Union[bool, List[int], List[str], List[List[Any]], Dict[Any, Any]] = ..., infer_datetime_format: bool = ...,
             keep_date_col: bool = ..., date_parser: Optional[AnyCallable] = ..., dayfirst: bool = ..., cache_dates: bool = ...,
             *, iterator: Literal[False] = ..., chunksize: None = ..., **kwargs: Any) -> DataFrame: ...

read_table: Any

def read_fwf(filepath_or_buffer: FilePathOrBuffer[AnyStr], colspecs: Any = ..., widths: Any = ..., infer_nrows: Any = ..., **kwds: Any) -> Any: ...

class TextFileReader(abc.Iterator[Any]):
    f: Any = ...
    orig_options: Any = ...
    engine: Any = ...
    chunksize: Any = ...
    nrows: Any = ...
    squeeze: Any = ...
    def __init__(self, f: Any, engine: Optional[Any] = ..., **kwds: Any) -> None: ...
    def close(self) -> None: ...
    def __next__(self) -> Any: ...
    def read(self, nrows: Optional[Any] = ...) -> Any: ...
    def get_chunk(self, size: Optional[Any] = ...) -> Any: ...

def TextParser(*args: Any, **kwds: Any) -> Any: ...