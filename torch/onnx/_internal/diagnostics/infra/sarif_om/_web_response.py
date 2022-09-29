# DO NOT EDIT! This file was generated by jschema_to_python version 0.0.1.dev29,
# with extension for dataclasses and type annotation.

from __future__ import annotations

import dataclasses
from typing import Any


@dataclasses.dataclass
class WebResponse(object):
    """Describes the response to an HTTP request."""

    body: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "body"}
    )
    headers: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "headers"}
    )
    index: Any = dataclasses.field(
        default=-1, metadata={"schema_property_name": "index"}
    )
    no_response_received: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "noResponseReceived"}
    )
    properties: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "properties"}
    )
    protocol: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "protocol"}
    )
    reason_phrase: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "reasonPhrase"}
    )
    status_code: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "statusCode"}
    )
    version: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "version"}
    )


# flake8: noqa