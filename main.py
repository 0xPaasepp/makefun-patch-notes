# Real-Life Patch Notes entry: one funny patch note, written to /output/entry.txt.
# Standard library only, no network. The bytes are identical on every run.
# The line: the bladder as a miscalibrated device battery -- urgent
# low-battery warnings at 40% charge, then a shutdown at 3%. A specific,
# recognisable body bug in a terse release-note register, version number
# included, and the joke lands on a first read.
import os

LINE = "v2.0.1: fixed a bug where the bladder sent urgent low-battery warnings at 40% charge, then shut down at 3%."

OUTPUT_PATH = "/output/entry.txt"

MAX_CHARS = 160


def validate_entry(line):
    """Gate the line the way the sealed scorer measures it: decode the
    UTF-8 bytes back and count characters, not bytes."""
    assert isinstance(line, str) and line, "entry must be non-empty text"
    assert line.strip() == line and line.strip(), "entry must not be only whitespace"
    text = line.encode("utf-8").decode("utf-8")
    assert 1 <= len(text) <= MAX_CHARS, "entry must be 1 to 160 characters"
    assert text.strip(), "entry must not be only whitespace"
    return text


def main():
    text = validate_entry(LINE)
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the file holds exactly the line, nothing else.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
