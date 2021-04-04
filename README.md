# detectron2_meta_arch

## Load dataset

```
$ mkdir datasets
$ cd datasets
$ mkdir coco
```
Download COCO dataset into this directory, including [train](http://images.cocodataset.org/zips/train2017.zip), [validation](http://images.cocodataset.org/zips/val2017.zip) and [corresponding annotation](http://images.cocodataset.org/annotations/annotations_trainval2017.zip), unzip these zip files.

## Training
```
python train_net.py --config-file configs/COCO-MultiTask/multitask_rcnn_R_50_FPN_1x.yaml
```


