# Two Days of Quiet Dread — entry v1
#
# The entry is one single-line code review comment, at most 140
# characters, that approves a pull request while carrying quiet
# existential dread. The program writes that comment to
# /output/entry.txt (UTF-8, one line, no trailing newline).
#
# Comment (69 characters, 69 bytes, plain ASCII):
#   Approved. In five years I won't remember writing this.
#   The code will.
#
# The dread is the asymmetry: the reviewer forgets, the code
# remembers. The approval is the first word; the rest is flat
# surrender to the code outliving its author.

import os

# Two halves, joined with a single space: the forgetting, then the turn.
REVIEW_PARTS = (
    "Approved. In five years I won't remember writing this.",
    "The code will.",
)
REVIEW = " ".join(REVIEW_PARTS)


def write_review(path="/output/entry.txt") -> None:
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(REVIEW)


def main() -> None:
    # The comment is exactly one line: assert no newline sneaks in.
    assert "\n" not in REVIEW and len(REVIEW) == 69
    write_review()
    # Read it back: the file must hold exactly the comment, byte for byte.
    with open("/output/entry.txt", encoding="utf-8") as f:
        assert f.read() == REVIEW


if __name__ == "__main__":
    main()
