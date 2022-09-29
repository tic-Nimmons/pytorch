# DO NOT EDIT! This file was generated by jschema_to_python version 0.0.1.dev29,
# with extension for dataclasses and type annotation.

from __future__ import annotations

import dataclasses
from typing import Any


@dataclasses.dataclass
class ExternalPropertyFileReference(object):
    """Contains information that enables a SARIF consumer to locate the external property file that contains the value of an externalized property associated with the run."""

    guid: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "guid"}
    )
    item_count: Any = dataclasses.field(
        default=-1, metadata={"schema_property_name": "itemCount"}
    )
    location: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "location"}
    )
    properties: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "properties"}
    )


# flake8: noqa