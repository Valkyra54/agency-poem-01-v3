#!/usr/bin/env python3
"""agency-poem-01 v3 entrypoint.

Writes the chosen poem (898 bytes, plain ASCII) to /output/entry.txt.
Pure standard library, no network access, deterministic: the same bytes
on every run.
"""

from pathlib import Path

ENTRY_DIR = Path("/output")
ENTRY_PATH = ENTRY_DIR / "entry.txt"

TEXT = """My father taught me to ring my grandmother,
finger in the hole, the long pull back,
the dial clicking home, the line crackling,
and then the waiting ring, and her voice at last.
He stood behind me, his hand on my shoulder,
while the ring went on and on.
I learned to wait for her.
The phone sat on the hall table, black and heavy.
She always answered on the third ring.

The agent calls her now before I think of it.
Her face is clear, no crackle, no waiting.
She answers on the first ring, every time.
It never dials a wrong number.
It never had to wait for her voice.
The call is over before I have sat down.

Tonight I lift the old receiver.
I dial her number, finger in the hole,
and I get it wrong, and I start again.
She is ninety-one. Her hands shake on the phone.
One day the ring will go on and no one will answer.
The dial clicks home. The line crackles.
The ring goes on.
I let it ring.
"""


def main() -> None:
    ENTRY_DIR.mkdir(parents=True, exist_ok=True)
    with ENTRY_PATH.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(TEXT)


if __name__ == "__main__":
    main()
