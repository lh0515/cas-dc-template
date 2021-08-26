_base_ = [
    '../_base_/models/mask_rcnn_r50_fpn.py',
    '../_base_/datasets/coco_instance_kaggle.py',
    '../_base_/schedules/schedule_1x.py', '../_base_/default_runtime.py'
]
#
# test_cfg = dict(
#     rcnn=dict(
#         score_thr=0.05,
#         nms=dict(type='soft_nms', iou_threshold=0.5),
#         # nms=dict(type='soft_nms', iou_threshold=0.5, method='naive'),
#         max_per_img=500,
#         mask_thr_binary=0.5))
