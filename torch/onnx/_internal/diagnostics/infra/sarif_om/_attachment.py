# DO NOT EDIT! This file was generated by jschema_to_python version 0.0.1.dev29,
# with extension for dataclasses and type annotation.

from __future__ import annotations

import dataclasses
from typing import Any


@dataclasses.dataclass
class Attachment(object):
    """An artifact relevant to a result."""

    artifact_location: Any = dataclasses.field(
        metadata={"schema_property_name": "artifactLocation"}
    )
    description: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "description"}
    )
    properties: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "properties"}
    )
    rectangles: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "rectangles"}
    )
    regions: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "regions"}
    )


# flake8: noqa