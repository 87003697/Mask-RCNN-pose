# Copyright (c) Facebook, Inc. and its affiliates.
from detectron2.layers import ShapeSpec

from .meta_arch import (
    Multi_MetaArch,
)

from .roi_heads import (
    KRCNNConvDeconvUpsampleHead_custom,
)

_EXCLUDE = {"ShapeSpec"}
__all__ = [k for k in globals().keys() if k not in _EXCLUDE and not k.startswith("_")]

