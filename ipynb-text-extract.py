import json
import os
import re
import sys

CODE_PLACEHOLDER = "\n\n```\n[code]\n```\n\n"
COMMENT = re.compile("(#.*$)")


def main(input_file: str, comments_enabled: bool = False):
    md_doc = get_text(input_file, comments_enabled)

    filename = os.path.basename(os.path.realpath(input_file))
    filename = os.path.splitext(filename)[0]

    output_file = filename + ".md"

    with open(output_file, "w") as writer:
        writer.write(md_doc)

    print(f"Text saved to {output_file}")


def get_text(input_file: str, comments_enabled: bool = False) -> str:
    try:
        with open(input_file) as notebook:
            notebook_json = json.loads(notebook.read())
    except FileNotFoundError:
        print(f"File {input_file} not found.")
        sys.exit(2)

    md_doc = ""

    for cell in notebook_json["cells"]:
        if cell["cell_type"] == "markdown":
            md_doc += "".join(cell["source"])
        elif cell["cell_type"] == "code" and comments_enabled:
            md_doc += parse_code_cell(cell["source"])
        elif cell["cell_type"] == "code":
            md_doc += CODE_PLACEHOLDER

    return md_doc


def parse_code_cell(source: list[str]) -> str:
    comments = ""
    for line in source:
        result = re.search(COMMENT, line)
        if result:
            comments += result.group(0) + "\n"

    if not comments:
        comments = CODE_PLACEHOLDER
    else:
        comments = "\n\n```\n" + comments + "```\n\n"

    return comments


def parse_arguments() -> list:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="ipynb file to process")
    parser.add_argument(
        "-c",
        "--comments",
        help="include comments from code cells",
        action="store_true",
    )
    args = parser.parse_args()

    return [args.input, args.comments]


if __name__ == "__main__":
    arguments = parse_arguments()
    main(*arguments)
