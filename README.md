# cas-dc-template
A Region-based Convolutional Network for Nuclei Detection and Segmentation in Microscopy Images
## Introduction
The installation of MMDetection can be found from the official github(https://github.com/open-mmlab/mmdetection/blob/v2.5.0/docs/install.md).<br>

In this paper, we propose a region-based convolutional network for a more accurate nuclei detection. <br>
![IoUPred](https://user-images.githubusercontent.com/54254748/130955492-6aafd176-bb4a-4248-8859-5257e217e883.png)

## Configuration
Our method is improved on the basis of Mask-RCNN, including GA-RPN,FBS and SoftNMS modules. The corresponding configuration can be found in(Ours\GARPN_FBS_SoftNMS-r50_fpn_1x_coco.py).

## Preparing Data
The mmdetection supports the coco dataset, but the DSB and monuseg datasets we use are not in the coco format. So we need to convert them to the coco format.<br>

The dataset that we processed can be downloaded from

## Get Started
```
./tools/train 
```

## Experiments Result
### DSB Dataset
The Detection Results are as follows

