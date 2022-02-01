from pandas._typing import FilePathOrBuffer as FilePathOrBuffer
from typing import Any, IO, Optional, Tuple, AnyStr

s3fs: Any

def get_file_and_filesystem(filepath_or_buffer: FilePathOrBuffer[AnyStr], mode: Optional[str]=...) -> Tuple[IO[Any], Any]: ...
def get_filepath_or_buffer(filepath_or_buffer: FilePathOrBuffer[AnyStr], encoding: Optional[str]=..., compression: Optional[str]=..., mode: Optional[str]=...) -> Tuple[IO[Any], Optional[str], Optional[str], bool]: ...
