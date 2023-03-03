# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from __future__ import annotations

from typing import MutableMapping, MutableSequence

import proto  # type: ignore

from google.protobuf import struct_pb2  # type: ignore


__protobuf__ = proto.module(
    package='google.cloud.aiplatform.v1beta1.schema.predict.prediction',
    manifest={
        'ImageObjectDetectionPredictionResult',
    },
)


class ImageObjectDetectionPredictionResult(proto.Message):
    r"""Prediction output format for Image Object Detection.

    Attributes:
        ids (MutableSequence[int]):
            The resource IDs of the AnnotationSpecs that
            had been identified, ordered by the confidence
            score descendingly.
        display_names (MutableSequence[str]):
            The display names of the AnnotationSpecs that
            had been identified, order matches the IDs.
        confidences (MutableSequence[float]):
            The Model's confidences in correctness of the
            predicted IDs, higher value means higher
            confidence. Order matches the Ids.
        bboxes (MutableSequence[google.protobuf.struct_pb2.ListValue]):
            Bounding boxes, i.e. the rectangles over the image, that
            pinpoint the found AnnotationSpecs. Given in order that
            matches the IDs. Each bounding box is an array of 4 numbers
            ``xMin``, ``xMax``, ``yMin``, and ``yMax``, which represent
            the extremal coordinates of the box. They are relative to
            the image size, and the point 0,0 is in the top left of the
            image.
    """

    ids: MutableSequence[int] = proto.RepeatedField(
        proto.INT64,
        number=1,
    )
    display_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    confidences: MutableSequence[float] = proto.RepeatedField(
        proto.FLOAT,
        number=3,
    )
    bboxes: MutableSequence[struct_pb2.ListValue] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=struct_pb2.ListValue,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
