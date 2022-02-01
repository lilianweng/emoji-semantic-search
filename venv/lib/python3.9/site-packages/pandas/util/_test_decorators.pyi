from typing import Any, Callable, Optional

def safe_import(mod_name: str, min_version: Optional[str]=...) -> Any: ...

tables: Any
xfail_non_writeable: Any

def skip_if_installed(package: str) -> Callable[..., Any]: ...
def skip_if_no(package: str, min_version: Optional[str]=...) -> Callable[..., Any]: ...

skip_if_no_mpl: Any
skip_if_mpl: Any
skip_if_32bit: Any
skip_if_windows: Any
skip_if_windows_python_3: Any
skip_if_has_locale: Any
skip_if_not_us_locale: Any
skip_if_no_scipy: Any
skip_if_no_ne: Any

def skip_if_np_lt(ver_str: str, reason: Optional[str]=..., *args: Any, **kwds: Any) -> Callable[..., Any]: ...
def parametrize_fixture_doc(*args: Any) -> Any: ...
def check_file_leaks(func: Any) -> Callable[..., Any]: ...
def async_mark() -> Any: ...
