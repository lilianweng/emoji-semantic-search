from typing import Any

def create_pandas_abc_type(name: Any, attr: Any, comp: Any) -> Any: ...

ABCIndex: Any
ABCInt64Index: Any
ABCUInt64Index: Any
ABCRangeIndex: Any
ABCFloat64Index: Any
ABCMultiIndex: Any
ABCDatetimeIndex: Any
ABCTimedeltaIndex: Any
ABCPeriodIndex: Any
ABCCategoricalIndex: Any
ABCIntervalIndex: Any
ABCIndexClass: Any
ABCSeries: Any
ABCDataFrame: Any
ABCSparseArray: Any
ABCCategorical: Any
ABCDatetimeArray: Any
ABCTimedeltaArray: Any
ABCPeriodArray: Any
ABCPeriod: Any
ABCDateOffset: Any
ABCInterval: Any
ABCExtensionArray: Any
ABCPandasArray: Any

class _ABCGeneric(type):
    def __instancecheck__(cls: Any, inst: Any) -> bool: ...

ABCGeneric: Any
