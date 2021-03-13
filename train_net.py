#!/usr/bin/env python3
# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved

"""
TridentNet Training Script.

This script is a simplified version of the training script in detectron2/tools.
"""

import os

from detectron2.checkpoint import DetectionCheckpointer
from detectron2.config import get_cfg
from detectron2.engine import DefaultTrainer, default_argument_parser, default_setup, launch
# from fewx.config import get_cfg
# from fewx.data.dataset_mapper import DatasetMapperWithSupport
from detectron2.data import DatasetMapper
# from fewx.data.build import build_detection_train_loader, build_detection_test_loader
from detectron2.data import build_detection_train_loader, build_detection_test_loader
# from fewx.solver import build_optimizer
from detectron2.solver.build import build_optimizer
# from fewx.evaluation import 
from detectron2.evaluation import COCOEvaluator
from detectron2.config import CfgNode as CN

import bisect
import copy
import itertools
import logging
import numpy as np
import operator
import pickle
import torch.utils.data

import detectron2.utils.comm as comm
from detectron2.utils.logger import setup_logger

import pdb


class Trainer(DefaultTrainer):

    @classmethod
    def build_train_loader(cls, cfg):
        """
        Returns:
            iterable
        It calls :func:`detectron2.data.build_detection_train_loader` with a customized
        DatasetMapper, which adds categorical labels as a semantic mask.
        """
        mapper = DatasetMapper(cfg)
        # data[0].keys() = dict_keys(['file_name', 'height', 'width', 'support_images', 'support_bboxes', 'support_cls', 'image', 'instances'])
        return build_detection_train_loader(cfg, mapper)

    @classmethod
    def build_test_loader(cls, cfg, dataset_name):
        """
        Returns:
            iterable
        It now calls :func:`detectron2.data.build_detection_test_loader`.
        Overwrite it if you'd like a different data loader.
        """
        return build_detection_test_loader(cfg, dataset_name)

    @classmethod
    def build_optimizer(cls, cfg, model):
        """
        Returns:
            torch.optim.Optimizer:
        It now calls :func:`detectron2.solver.build_optimizer`.
        Overwrite it if you'd like a different optimizer.
        """
        return build_optimizer(cfg, model)

    @classmethod
    def build_evaluator(cls, cfg, dataset_name, output_folder=None):
        if output_folder is None:
            output_folder = os.path.join(cfg.OUTPUT_DIR, "inference")
        return COCOEvaluator(dataset_name, cfg, True, output_folder)

# by Zhiyuan Ma #######
def add_our_config(cfg):
    _C = cfg
    _C.OURS = CN()
    _C.OURS.IMG_PERINS = 3 #args.img_perins
    _C.OURS.IOU_THRES = 0.8 #args.iou_thres
    _C.OURS.CAR_BOX = 'heaviside'
    _C.SOLVER.IMS_PER_BATCH = 4
    #_C.SOLVER.MAX_ITER: 3000
    # _C.SOLVER.CLIP_GRADIENTS.ENABLED = True
    # _C.CLIP_VALUE = 1000

###############

def setup(args):
    """
    Create configs and perform basic setups.
    """
    cfg = get_cfg()
    cfg.merge_from_file(args.config_file)
    # add_our_config(cfg)
    # cfg.merge_from_list(args.opts)
    cfg.freeze()
    default_setup(cfg, args)

    rank = comm.get_rank()
    setup_logger(cfg.OUTPUT_DIR, distributed_rank=rank, name="fewx")

    return cfg


def main(args):
    cfg = setup(args)

    if args.eval_only:
        model = Trainer.build_model(cfg)
        DetectionCheckpointer(model, save_dir=cfg.OUTPUT_DIR).resume_or_load(
            cfg.MODEL.WEIGHTS, resume=args.resume
        )
        res = Trainer.test(cfg, model)
        return res

    trainer = Trainer(cfg)
    trainer.resume_or_load(resume=args.resume)
    return trainer.train()


if __name__ == "__main__":
    args = default_argument_parser().parse_args()
    print("Command Line Args:", args)
    
    
    launch(
        main,
        args.num_gpus,
        num_machines=args.num_machines,
        machine_rank=args.machine_rank,
        dist_url=args.dist_url,
        args=(args,),
    )
