#!/usr/bin/env python3

""" Generates PyTorch ONNX Export Diagnostic rules for C++, Python and documentations.
The rules are defined in torch/onnx/_internal/diagnostics/rules.yaml.

Usage:

python -m tools.onnx.gen_diagnostics \
    torch/onnx/_internal/diagnostics/rules.yaml \
    torch/onnx/_internal/diagnostics \
    torch/csrc/onnx/diagnostics/generated \
    torch/docs/source
"""

import argparse
import os
import subprocess
import textwrap
from typing import Any, Mapping, Sequence

import yaml

from torchgen import utils as torchgen_utils

_RULES_GENERATED_COMMENT = """\
Diagnostic rules for PyTorch ONNX export.

This file is generated by gen_diagnostics.py. Do not edit directly.
See tools/onnx/gen_diagnostics.py for more information.
"""

_PY_RULE_TEMPLATE = """\
{0}: infra.Rule = dataclasses.field(
    default=infra.Rule.from_sarif(**{1}),
    init=False,
)
\"\"\"{2}\"\"\"
"""

_CPP_RULE_TEMPLATE = """\
/**
 * @brief {1}
 */
{0},
"""

_RuleType = Mapping[str, Any]


def _kebab_case_to_snake_case(name: str) -> str:
    return name.replace("-", "_")


def _kebab_case_to_pascal_case(name: str) -> str:
    return "".join(word.capitalize() for word in name.split("-"))


def _format_rule_for_python(rule: _RuleType) -> str:
    name = _kebab_case_to_snake_case(rule["name"])
    short_description = rule["short_description"]["text"]

    return _PY_RULE_TEMPLATE.format(name, rule, short_description)


def _format_rule_for_cpp(rule: _RuleType) -> str:
    name = f"k{_kebab_case_to_pascal_case(rule['name'])}"
    short_description = rule["short_description"]["text"]
    return _CPP_RULE_TEMPLATE.format(name, short_description)


def gen_diagnostics_python(
    rules: Sequence[_RuleType], out_py_dir: str, template_dir: str
) -> None:

    rule_lines = [_format_rule_for_python(rule) for rule in rules]

    fm = torchgen_utils.FileManager(
        install_dir=out_py_dir, template_dir=template_dir, dry_run=False
    )
    fm.write_with_template(
        "_rules.py",
        "rules.py.in",
        lambda: {
            "generated_comment": _RULES_GENERATED_COMMENT,
            "rules": textwrap.indent("\n".join(rule_lines), " " * 4),
        },
    )
    _lint_file(os.path.join(out_py_dir, "_rules.py"))


def gen_diagnostics_cpp(
    rules: Sequence[_RuleType], out_cpp_dir: str, template_dir: str
) -> None:

    rule_lines = [_format_rule_for_cpp(rule) for rule in rules]
    rule_names = [f'"{_kebab_case_to_snake_case(rule["name"])}",' for rule in rules]

    fm = torchgen_utils.FileManager(
        install_dir=out_cpp_dir, template_dir=template_dir, dry_run=False
    )
    fm.write_with_template(
        "rules.h",
        "rules.h.in",
        lambda: {
            "generated_comment": textwrap.indent(
                _RULES_GENERATED_COMMENT,
                " * ",
                predicate=lambda x: True,  # Don't ignore empty line
            ),
            "rules": textwrap.indent("\n".join(rule_lines), " " * 2),
            "py_rule_names": textwrap.indent("\n".join(rule_names), " " * 4),
        },
    )
    _lint_file(os.path.join(out_cpp_dir, "rules.h"))


def gen_diagnostics_docs(
    rules: Sequence[_RuleType], out_docs_dir: str, template_dir: str
) -> None:
    # TODO: Add doc generation in a follow-up PR.
    pass


def _lint_file(file_path: str) -> None:
    p = subprocess.Popen(["lintrunner", "-a", file_path])
    p.wait()


def gen_diagnostics(
    rules_path: str,
    out_py_dir: str,
    out_cpp_dir: str,
    out_docs_dir: str,
) -> None:

    with open(rules_path, "r") as f:
        rules = yaml.load(f, Loader=torchgen_utils.YamlLoader)

    template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")

    gen_diagnostics_python(
        rules,
        out_py_dir,
        template_dir,
    )

    gen_diagnostics_cpp(
        rules,
        out_cpp_dir,
        template_dir,
    )

    gen_diagnostics_docs(rules, out_docs_dir, template_dir)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate ONNX diagnostics files")
    parser.add_argument("rules_path", metavar="RULES", help="path to rules.yaml")
    parser.add_argument(
        "out_py_dir",
        metavar="OUT_PY",
        help="path to output directory for Python",
    )
    parser.add_argument(
        "out_cpp_dir",
        metavar="OUT_CPP",
        help="path to output directory for C++",
    )
    parser.add_argument(
        "out_docs_dir",
        metavar="OUT_DOCS",
        help="path to output directory for docs",
    )
    args = parser.parse_args()
    gen_diagnostics(
        args.rules_path,
        args.out_py_dir,
        args.out_cpp_dir,
        args.out_docs_dir,
    )


if __name__ == "__main__":
    main()