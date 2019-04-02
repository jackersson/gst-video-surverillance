import os

from core.structures import VideoSourceConfig

from core.modules import ObjectDetectionOverlayAdapter, ObjectDetectorAdapter
from core.modules.tf_object_detection import tf_object_detection_model_from_file
from core.modules.object_detection_overlay import ColorPicker

colors = ColorPicker()

object_detection_model = tf_object_detection_model_from_file(os.path.abspath("configs/cfg.yml"))

object_detection_adapter = ObjectDetectorAdapter(object_detection_model, batch_size=2)


video_source_config_1 = VideoSourceConfig(
    source="data/videos/vinnytsia_road.mp4",
    source_id=0,
    modules=[
        object_detection_adapter,
        ObjectDetectionOverlayAdapter(colors=colors)
    ],
    show_window=True,
    show_fps=True,
    sync=True
)

video_source_config_2 = VideoSourceConfig(
    source="data/videos/vinnytsia_road.mp4",
    source_id=1,
    modules=[
        object_detection_adapter,
        ObjectDetectionOverlayAdapter(colors=colors)
    ],
    show_window=True,
    show_fps=True,
    sync=True
)

video_source_config_3 = VideoSourceConfig(
    source="data/videos/vinnytsia_road.mp4",
    source_id=2,
    modules=[
        ObjectDetectorAdapter(object_detection_model),
        ObjectDetectionOverlayAdapter(colors=colors)
    ],
    show_window=True,
    show_fps=True,
    sync=True
)


VIDEO_SOURCES = [video_source_config_1, video_source_config_2, video_source_config_3]
