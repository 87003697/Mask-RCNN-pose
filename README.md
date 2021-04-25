# Multi Task RCNN with Refinement

This is the repository of our final project in [EECS6691](https://courseworks2.columbia.edu/courses/125313). We build a multi task system across the domian of *Object Detection*, *Instance Segmentation*, *Keypoint Estimation*. For details please refer to our [presentation slide](https://docs.google.com/presentation/d/1YKi3ZLzx7Ps7KIZYOzZmKffhNW6VDJ8Z2AzeOF6qeYc/edit#slide=id.gcd5ca95077_0_80) and [report](https://github.com/ecbme6040/e6691-2021spring-project-jyzm-jy3114-zm2354).

Our code is built on [Detectron2](https://github.com/facebookresearch/detectron2/tree/72059968a2b2337ab34c86ddcbfc2f22e6914ff3), it's a marvellous framework on top of pytorch in the domain of detection and estimation. It simplifies our code and maintaining the code becomes even clear and comfortable.

## Performance


## Environment
Up-to-date environment requirement (March 2020) is cuda 10.1, python 3.8+, pytorch 1.7.0+. 

## Setup
### Dataset 
Our model uses [COCO 2017](https://cocodataset.org/#home). Under Linux run the following command at the repo root directory.

```
$ mkdir datasets
$ cd datasets
$ mkdir coco
$ cd coco
$ ln -s <your coco path>/train2017 ./
$ ln -s <your coco path>/val2017 ./
$ ln -s <your coco path>/annotations ./
``` 
