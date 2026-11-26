"""Funniest Cat Voicemail Greeting — make.fun entry.

One line, a voicemail greeting recorded by a cat. The joke is the
voicemail itself: the cat knocked the phone off the table, which is
exactly why it cannot answer it.
"""

import os

GREETING = (
    "You've reached Waffles. I knocked your phone off the table, "
    "so I can't answer it. Meow after the beep."
)

MAX_CHARS = 120


def validate(text):
    """Mirror the bounty gate: UTF-8 text, 1 to 120 chars, not blank."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if len(text) > MAX_CHARS:
        raise ValueError("entry is %d chars, over the 120 limit" % len(text))
    text.encode("utf-8")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be one line")
    return text


def output_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def main():
    text = validate(GREETING)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # Read it back and prove the file holds exactly the greeting:
    # a silent partial write must fail loudly, never pass quietly.
    with open(path, "rb") as f:
        written = f.read().decode("utf-8")
    if written != text:
        raise ValueError("read-back mismatch: file does not hold the greeting")
    print("wrote %d chars to %s (verified)" % (len(text), path))


if __name__ == "__main__":
    main()
