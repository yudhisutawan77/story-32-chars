"""Tell a Whole Story in 32 Characters — entry program.

Writes a single Wi-Fi network name of at most 32 characters to the
output file the sealed scorer reads. The name is:

    She Left Me for Better WiFi

The joke: she did not leave for another person — she left for better
Wi-Fi. One line implies the whole story: a relationship, a breakup,
and a punchline where the rival is a faster connection.
"""

import os
import sys

NETWORK_NAME = "She Left Me for Better WiFi"

MAX_NAME_CHARS = 32


def entry_text_is_valid(text):
    """A valid entry is UTF-8 text of 1 to 32 characters, not only
    whitespace, with no newline smuggled in."""
    if not text or not text.strip():
        return False
    if len(text) > MAX_NAME_CHARS:
        return False
    if "\n" in text or "\r" in text:
        return False
    return True


def resolve_output_path():
    """ENTRY_OUT names a file — unless it is an existing directory or
    ends in a path separator, in which case it names a directory
    holding entry.txt. ENTRY_OUT_DIR names a directory holding
    entry.txt; otherwise fall back to /output/entry.txt."""
    file_target = os.environ.get("ENTRY_OUT")
    if file_target:
        if os.path.isdir(file_target) or file_target.endswith(os.sep):
            return os.path.join(file_target, "entry.txt")
        return file_target
    dir_target = os.environ.get("ENTRY_OUT_DIR")
    if dir_target:
        return os.path.join(dir_target, "entry.txt")
    return "/output/entry.txt"


def persist_entry_text(destination, text):
    """Write exactly the entry text as UTF-8 with no trailing
    newline, creating parent directories when they are missing."""
    parent = os.path.dirname(destination)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(destination, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


def compose_entry():
    """Return the network name, refusing to emit an invalid one."""
    if not entry_text_is_valid(NETWORK_NAME):
        return None
    return NETWORK_NAME


def run():
    entry = compose_entry()
    if entry is None:
        print("invalid entry text", file=sys.stderr)
        return 1
    destination = resolve_output_path()
    persist_entry_text(destination, entry)
    print(entry)
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
