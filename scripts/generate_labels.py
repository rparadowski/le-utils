"""
generate_labels
Builds or rebuilds the labels py files assigning ids to the labels
"""
from __future__ import unicode_literals

import json
import os
import re
import string
from hashlib import md5
from uuid import UUID
from uuid import uuid3

from pkg_resources import get_distribution

try:
    FileNotFoundError
except NameError:
    FileNotFoundError = IOError


root_label = md5()
root_label.update("Kolibri labels")

root_namespace = UUID(hex=root_label.hexdigest())

pascal_case_pattern = re.compile(r"(?<!^)(?=[A-Z])")

js_labels_output_dir = os.path.join(os.path.dirname(__file__), "..", "js", "labels")


def pascal_to_snake(name):
    return pascal_case_pattern.sub("_", name).lower()


CHARACTERS = string.letters + string.digits + "#" + "&"


def _from_uuid(uuid):
    """
    :params uuid: UUID
    :returns: character string that represents the UUID
    """
    data = int(uuid.hex[:8], 16)
    res = []
    while data > 0 or not res:
        res += CHARACTERS[(data & 0x3F)]
        data >>= 6
    res.reverse()
    return "".join(res)


def generate_identifier(namespace, label):
    return uuid3(namespace, label.encode("utf-8"))


def generate_key(identifier, previous=None):
    key = _from_uuid(identifier)
    if previous is None:
        return key
    return "{}.{}".format(previous, key)


def handle_array(labels, namespace, previous=None):
    output = {}
    for label in labels:
        identifier = generate_identifier(namespace, label)
        output[label] = generate_key(identifier, previous)
    return output


def handle_object(element, namespace, previous=None):
    output = {}
    for key, value in element.items():
        handler = handle_object if isinstance(value, dict) else handle_array
        identifier = generate_identifier(namespace, key)
        new_key = generate_key(identifier, previous)
        output[key] = new_key
        output.update(handler(value, namespace, new_key))
    return output


def read_labels_spec():
    labels_spec_file = os.path.join(
        os.path.dirname(__file__),
        "..",
        "spec",
        "labels.json",
    )
    with open(labels_spec_file) as json_labels_spec_file:
        return json.load(json_labels_spec_file)


def write_labels_src(labels_spec):
    py_output_dir = os.path.join(
        os.path.dirname(__file__), "..", "le_utils", "constants", "labels"
    )

    for label_type, labels in labels_spec.items():
        handler = handle_object if isinstance(labels, dict) else handle_array
        namespace = generate_identifier(root_namespace, label_type)
        output = handler(labels, namespace)
        py_output_file = os.path.join(
            py_output_dir, "{}.py".format(pascal_to_snake(label_type))
        )
        with open(py_output_file, "w") as f:
            f.write("# -*- coding: utf-8 -*-\n")
            f.write("# Generated by scripts/generate_labels.py\n")
            f.write("from __future__ import unicode_literals\n")
            f.write("\n")
            f.write("# {}\n".format(label_type))
            f.write("\n")
            for key, value in output.items():
                f.write('{} = "{}"\n'.format(key, value))
            f.write("\n")
            f.write("choices = (\n")
            for key in output.keys():
                f.write('    ({}, "{}"),\n'.format(key, key.replace("_", " ").title()))
            f.write(")\n")
            f.write("\n")
            f.write("{}LIST = [\n".format(label_type.upper()))
            for key in output.keys():
                f.write("    {},\n".format(key))
            f.write("]\n")

        js_output_file = os.path.join(js_labels_output_dir, "{}.js".format(label_type))
        with open(js_output_file, "w") as f:
            f.write("// -*- coding: utf-8 -*-\n")
            f.write("// Generated by scripts/generate_labels.py\n")
            f.write("\n")
            f.write("export default {\n")
            for key, value in output.items():
                f.write('    {key}: "{value}",\n'.format(key=key, value=value))
            f.write("};\n")

    js_labels_index_file = os.path.join(js_labels_output_dir, "index.js")

    with open(js_labels_index_file, "w") as f:
        f.write("// -*- coding: utf-8 -*-\n")
        f.write("// Generated by scripts/generate_labels.py\n")
        f.write("\n")
        for label_type in labels_spec.keys():
            f.write('import {0} from "./{0}";\n'.format(label_type))
        f.write("\n")
        f.write("export default {\n")
        for label_type in labels_spec.keys():
            f.write("    {0}: {0},\n".format(label_type))
        f.write("};\n")


def create_js_index(labels_spec):
    js_index_file = os.path.join(os.path.dirname(__file__), "..", "js", "index.js")

    with open(js_index_file, "w") as f:
        f.write("// -*- coding: utf-8 -*-\n")
        f.write("// Generated by scripts/generate_labels.py\n")
        f.write("\n")
        for label_type in labels_spec.keys():
            f.write('import {0} from "./labels/{0}";\n'.format(label_type))
        f.write("\n")
        f.write("export default {\n")
        for label_type in labels_spec.keys():
            f.write("    {0}: {0},\n".format(label_type))
        f.write("};\n")


def set_package_json_version():
    python_version = get_distribution("le-utils").version

    package_json = os.path.join(os.path.dirname(__file__), "..", "package.json")

    with open(package_json, "r") as f:
        package = json.load(f)

    package["version"] = python_version

    with open(package_json, "w") as f:
        json.dump(package, f, indent=2, sort_keys=True)


if __name__ == "__main__":
    labels_spec = read_labels_spec()

    write_labels_src(labels_spec)

    create_js_index(labels_spec)

    set_package_json_version()
