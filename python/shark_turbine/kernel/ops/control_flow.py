from typing import Any, List, Tuple, Optional, Iterator, overload
import typing

if typing.TYPE_CHECKING:
    from ..lang.types import Index

from .base import (
    define_op,
)

__all__ = [
    "cf_range",
]


@define_op
def cf_range(
    start: "Index",
    stop: Optional["Index"] = None,
    step: Optional["Index"] = None,
) -> Iterator["Index"]:
    ...
