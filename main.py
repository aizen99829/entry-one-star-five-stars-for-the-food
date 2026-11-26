# SPDX-License-Identifier: MIT
"""One Star, Five Stars for the Food — make.fun entry.

An alien tourist reviews planet Earth: one star overall, five stars
for the food. The program writes that single review sentence to
/output/entry.txt, exactly as the competition requires.
"""

# The entry: one sentence, an alien's one-star review of Earth that
# still hands the food five stars. The complaints are concrete and
# touristy (gravity, lying weather, brunch queues); the praise lands
# on one specific dish, tacos, so the five stars feel earned rather
# than tacked on. The closing turn — coming back hungry — is the joke
# that the reviewer hates the planet and still can't stay away.
ENTRY = (
    "One star for Earth — gravity is a scam, the weather lies, and "
    "the locals queue an hour for brunch; the tacos alone deserve "
    "five stars, so I'm coming back hungry."
)

# Competition limits: exactly one sentence, at most 200 characters.
# The em-dash and semicolon keep the review a single sentence while
# letting it breathe through three beats — complaint, complaint,
# praise — so it reads like a real review, not a slogan.
MAX_CHARS = 200


def validate(entry):
    """Check the entry against the competition's shape rules."""
    text = entry.strip()
    if not text:
        raise ValueError("entry must not be empty")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")
    if text.count(".") > 1:
        raise ValueError("entry must be a single sentence")
    return text


def write_entry(entry, path="/output/entry.txt"):
    """Write the validated sentence to the harness output file."""
    import os

    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(entry + "\n")
    return path


def main():
    text = validate(ENTRY)
    write_entry(text)
    print(text)


if __name__ == "__main__":
    main()
