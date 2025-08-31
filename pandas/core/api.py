from pandas._libs import (
    NaT,
    Period,
    Timedelta,
    Timestamp,
)
# from pandas._libs.missing import NA

from pandas.core.dtypes.dtypes import (
    ArrowDtype,
    CategoricalDtype,
    DatetimeTZDtype,
    IntervalDtype,
    PeriodDtype,
)
from pandas.core.dtypes.missing import (
    isna,
    isnull,
    notna,
    notnull,
)

from pandas.core.algorithms import (
    factorize,
    unique,
)
from pandas.core.arrays import Categorical
from pandas.core.arrays.boolean import BooleanDtype
from pandas.core.arrays.floating import (
    Float32Dtype,
    Float64Dtype,
)
from pandas.core.arrays.integer import (
    Int8Dtype,
    Int16Dtype,
    Int32Dtype,
    Int64Dtype,
    UInt8Dtype,
    UInt16Dtype,
    UInt32Dtype,
    UInt64Dtype,
)
from pandas.core.arrays.string_ import StringDtype
from pandas.core.construction import array  # noqa: ICN001
from pandas.core.flags import Flags
from pandas.core.groupby import (
    Grouper,
    NamedAgg,
)
from pandas.core.indexes.api import (
    CategoricalIndex,
    DatetimeIndex,
    Index,
    IntervalIndex,
    MultiIndex,
    PeriodIndex,
    RangeIndex,
    TimedeltaIndex,
)
from pandas.core.indexes.datetimes import (
    bdate_range,
    date_range,
)
from pandas.core.indexes.interval import (
    Interval,
    interval_range,
)
from pandas.core.indexes.period import period_range
from pandas.core.indexes.timedeltas import timedelta_range
from pandas.core.indexing import IndexSlice
from pandas.core.series import Series
from pandas.core.tools.datetimes import to_datetime
from pandas.core.tools.numeric import to_numeric
from pandas.core.tools.timedeltas import to_timedelta

from pandas.io.formats.format import set_eng_float_format
from pandas.tseries.offsets import DateOffset

# DataFrame needs to be imported after NamedAgg to avoid a circular import
from pandas.core.frame import DataFrame  # isort:skip

__all__ = [
    "NA",
    "ArrowDtype",
    "BooleanDtype",
    "Categorical",
    "CategoricalDtype",
    "CategoricalIndex",
    "DataFrame",
    "DateOffset",
    "DatetimeIndex",
    "DatetimeTZDtype",
    "Flags",
    "Float32Dtype",
    "Float64Dtype",
    "Grouper",
    "Index",
    "IndexSlice",
    "Int8Dtype",
    "Int16Dtype",
    "Int32Dtype",
    "Int64Dtype",
    "Interval",
    "IntervalDtype",
    "IntervalIndex",
    "MultiIndex",
    "NaT",
    "NamedAgg",
    "Period",
    "PeriodDtype",
    "PeriodIndex",
    "RangeIndex",
    "Series",
    "StringDtype",
    "Timedelta",
    "TimedeltaIndex",
    "Timestamp",
    "UInt8Dtype",
    "UInt16Dtype",
    "UInt32Dtype",
    "UInt64Dtype",
    "array",
    "bdate_range",
    "date_range",
    "factorize",
    "interval_range",
    "isna",
    "isnull",
    "notna",
    "notnull",
    "period_range",
    "set_eng_float_format",
    "timedelta_range",
    "to_datetime",
    "to_numeric",
    "to_timedelta",
    "unique",
]

def count_to_1000_divisible_by_7():
    """
    Counts to 1000, including only numbers divisible by 7.
    """
    count = 0
    for i in range(1, 1001):
        if i % 7 == 0:
            count += 1
    return count
from pandas.core.my_func import count_to_1000_divisible_by_7
from pandas.core.my_func import count_to_1000_divisible_by_7

def count_to_1000_divisible_by_7():
    """
    Counts to 1000, including only numbers divisible by 7.
    """
    count = 0
    for i in range(1, 1001):
        if i % 7 == 0:
            count += 1
    return count
NA = None
