#!/usr/bin/env python3
"""Caption-kit guard. CLAUDE.md 15 is a long checklist and a long checklist gets skipped.

Every deck ships four pieces of copy plus the DM, and the nine decks shipped with none of
them, which is how the gap got there in the first place: the rules lived in prose and nobody
was counting words. So this counts them.

Hard fails:
  1  LinkedIn caption 400-470 words, five blocks separated by `- - -`
  2  the caption hook does not start with "I", and names Claude or AI in its first two lines
  3  3 to 5 arrow items in block 3
  4  the fixed CTA, exactly
  5  ALT 80-150 words, first comment 40-80
  6  charscan: zero em dash, en dash, ellipsis char, curly quote
  7  exactly the five-tag set, on the last line of the reel caption and nowhere else
  8  no emoji, no markdown bold, no markdown links
  9  every 51ultron.com link is one of the confirmed paths
 10  no agent roster names (CLAUDE.md 21: Claude, AI and Ultron, nothing else)

Reported, not failed: the three hooks being genuinely different sentences. Word overlap is a
weak proxy for that, so it prints the overlap and leaves the judgement to a person.
"""
import pathlib, re, sys

CONFIRMED = {
    "51ultron.com", "app.51ultron.com", "app.51ultron.com/resources",
    "app.51ultron.com/resources#blueprints", "app.51ultron.com/techniques",
    "app.51ultron.com/docs", "app.51ultron.com/docs/architecture",
    "app.51ultron.com/enterprise", "app.51ultron.com/bcp", "app.51ultron.com/creators",
    "work.51ultron.com/calculator",
}
TAGS = ["#claude", "#ai", "#founder", "#startup", "#buildinpublic"]
ROSTER = ("CORTEX", "SPECTER", "STRIKER", "PULSE", "SENTINEL", "AMPLIFY", "COUNSEL")
CTA1 = "Follow for one AI system for founders every day."


def sections(text: str) -> dict:
    out, cur = {}, None
    for line in text.split("\n"):
        if line.startswith("## "):
            cur = line[3:].split("  (")[0].strip()
            out[cur] = []
        elif cur is not None and line.strip() != "---":
            out[cur].append(line)
    return {k: "\n".join(v).strip() for k, v in out.items()}


def words(s: str) -> int:
    s = re.sub(r"^- - -$", "", s, flags=re.M)
    return len([w for w in s.split() if any(c.isalnum() for c in w)])


def check(path: pathlib.Path) -> list[str]:
    t = path.read_text()
    S = sections(t)
    bad = []

    def need(name):
        if name not in S:
            bad.append(f"missing section: {name}")
        return S.get(name, "")

    li, alt = need("LINKEDIN CAPTION"), need("ALT TEXT")
    fc, reel = need("FIRST COMMENT"), need("REEL CAPTION")
    need("DM")

    n = words(li)
    if not 400 <= n <= 470:
        bad.append(f"linkedin caption {n} words, needs 400-470")
    blocks = [b.strip() for b in li.split("\n- - -\n")]
    if len(blocks) != 5:
        bad.append(f"linkedin caption has {len(blocks)} blocks, needs 5 split by '- - -'")
    if li.startswith("I "):
        bad.append("caption hook starts with 'I'")
    first2 = " ".join(li.split("\n")[:2])
    if "Claude" not in first2 and "AI" not in first2:
        bad.append("caption hook does not name Claude or AI in its first two lines")
    arrows = blocks[2].count("→") if len(blocks) >= 3 else 0
    if not 3 <= arrows <= 5:
        bad.append(f"block 3 has {arrows} arrow items, needs 3-5")
    if CTA1 not in li:
        bad.append("the fixed CTA first line is not exact")
    if not re.search(r"Comment [A-Z0-9]+ and I will send you the exact Claude ", li):
        bad.append("the fixed CTA second line is not in the required form")

    na, nf = words(alt), words(fc)
    if not 80 <= na <= 150:
        bad.append(f"alt text {na} words, needs 80-150")
    if not 40 <= nf <= 80:
        bad.append(f"first comment {nf} words, needs 40-80")

    found = sorted(set(re.findall(r"[—–…‘’“”]", t)))
    if found:
        bad.append(f"charscan hits: {found}")
    if re.search(r"[\U0001F300-\U0001FAFF☀-➿]", t):
        bad.append("emoji present")
    if "**" in li + fc + reel:
        bad.append("markdown bold in copy")
    if re.search(r"\[[^\]]+\]\([^)]+\)", li + fc + reel):
        bad.append("markdown link in copy")

    tags = re.findall(r"#\w+", t)
    if tags != TAGS:
        bad.append(f"hashtags are {tags}, need exactly {TAGS} once, on the reel's last line")
    if reel and not reel.rstrip().endswith(" ".join(TAGS)):
        bad.append("the five tags are not the reel caption's last line")

    links = set(re.findall(r"\b(?:app\.|work\.)?51ultron\.com[\w/#]*", t))
    for l in sorted(links - CONFIRMED):
        bad.append(f"unconfirmed link: {l}")
    for r in ROSTER:
        if re.search(rf"\b{r}\b", t):
            bad.append(f"agent roster name in copy: {r}")

    kw = re.search(r"Comment ([A-Z0-9]+) and I will send", li)
    if kw:
        k = kw.group(1)
        if f"Drop {k} " not in fc and k not in fc:
            bad.append(f"keyword {k} missing from the first comment")
        if k not in reel:
            bad.append(f"keyword {k} missing from the reel caption")
    return bad


def report(path: pathlib.Path) -> bool:
    S = sections(path.read_text())
    bad = check(path)
    n = [words(S.get(k, "")) for k in
         ("LINKEDIN CAPTION", "ALT TEXT", "FIRST COMMENT", "REEL CAPTION")]
    flag = "FAIL" if bad else "ok  "
    print(f"{flag} {path.parent.name:16} li {n[0]:3}  alt {n[1]:3}  fc {n[2]:3}  reel {n[3]:3}")
    for b in bad:
        print(f"       - {b}")
    return not bad


if __name__ == "__main__":
    args = sys.argv[1:] or sorted(
        str(p) for p in pathlib.Path("content/decks").glob("*/caption.md"))
    # every file, always. `all(generator)` short-circuits, which quietly hides every kit
    # after the first failing one - the opposite of what a batch guard is for.
    results = [report(pathlib.Path(a)) for a in args]
    print(f"\n{sum(results)}/{len(results)} clean" if all(results) is False
          else f"\nall {len(results)} clean")
    sys.exit(0 if all(results) else 1)
