# DO NOT EDIT! This file was generated by jschema_to_python version 0.0.1.dev29,
# with extension for dataclasses and type annotation.

from __future__ import annotations

import dataclasses
from typing import Any


@dataclasses.dataclass
class Run(object):
    """Describes a single run of an analysis tool, and contains the reported output of that run."""

    tool: Any = dataclasses.field(metadata={"schema_property_name": "tool"})
    addresses: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "addresses"}
    )
    artifacts: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "artifacts"}
    )
    automation_details: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "automationDetails"}
    )
    baseline_guid: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "baselineGuid"}
    )
    column_kind: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "columnKind"}
    )
    conversion: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "conversion"}
    )
    default_encoding: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "defaultEncoding"}
    )
    default_source_language: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "defaultSourceLanguage"}
    )
    external_property_file_references: Any = dataclasses.field(
        default=None,
        metadata={"schema_property_name": "externalPropertyFileReferences"},
    )
    graphs: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "graphs"}
    )
    invocations: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "invocations"}
    )
    language: Any = dataclasses.field(
        default="en-US", metadata={"schema_property_name": "language"}
    )
    logical_locations: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "logicalLocations"}
    )
    newline_sequences: Any = dataclasses.field(
        default_factory=lambda: ["\r\n", "\n"],
        metadata={"schema_property_name": "newlineSequences"},
    )
    original_uri_base_ids: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "originalUriBaseIds"}
    )
    policies: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "policies"}
    )
    properties: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "properties"}
    )
    redaction_tokens: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "redactionTokens"}
    )
    results: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "results"}
    )
    run_aggregates: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "runAggregates"}
    )
    special_locations: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "specialLocations"}
    )
    taxonomies: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "taxonomies"}
    )
    thread_flow_locations: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "threadFlowLocations"}
    )
    translations: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "translations"}
    )
    version_control_provenance: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "versionControlProvenance"}
    )
    web_requests: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "webRequests"}
    )
    web_responses: Any = dataclasses.field(
        default=None, metadata={"schema_property_name": "webResponses"}
    )


# flake8: noqa