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
So far your coco has been tracked by Detectron2.

### Training
We placed multiple training configuration files in the `configs` directory, choose one and start up your training. Take our final config `configs/COCO-MultiTask/multitask_rcnn_DR_50_FPN_1x_chead.yaml` as the example, run
```
python train_net.py --config-file configs/COCO-MultiTask/multitask_rcnn_DR_50_FPN_1x_chead.yaml --num-gpus <your number of gpus>
```

### Testing
After the training, the framework turns directly into testing mode, but if you want to test yourself, run the following command, take the same config as example
```
python train_net.py --config-file configs/COCO-MultiTask/multitask_rcnn_DR_50_FPN_1x_chead.yaml --num-gpus <your number of gpus> --eval-only
```
You will see the result displayed on your terminal.

### Visualization
Our code also support visualize your model performance. After the testing is all set, there will be a `visualization` directory in the root directory. Check the model performance through the images there!

