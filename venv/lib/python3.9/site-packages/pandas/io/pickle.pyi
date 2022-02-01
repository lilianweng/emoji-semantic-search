from pandas._typing import FilePathOrBuffer as FilePathOrBuffer
from pandas.io.common import get_filepath_or_buffer as get_filepath_or_buffer, get_handle as get_handle
from typing import Any, Optional, AnyStr


def to_pickle(obj: Any, filepath_or_buffer: FilePathOrBuffer[AnyStr], compression: Optional[str]=..., protocol: int=...) -> Any: ...
def read_pickle(filepath_or_buffer: FilePathOrBuffer[AnyStr], compression: Optional[str]=...) -> Any: ...
