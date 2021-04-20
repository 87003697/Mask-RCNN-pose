
# -*- coding: utf-8 -*-
# Copyright (c) Facebook, Inc. and its affiliates.

# import the custom roi head, so they will be registered
from .keypoint_head import KRCNNConvDeconvUpsampleHead_custom

__all__ = list(globals().keys())