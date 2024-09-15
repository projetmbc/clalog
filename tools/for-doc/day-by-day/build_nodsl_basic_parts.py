from pathlib import Path
from yaml    import safe_load


# --------------- #
# -- CONSTANTS -- #
# --------------- #

THIS_DIR = Path(__file__).parent

CONTENT_DIR = THIS_DIR

while(CONTENT_DIR.name != "tools"):
    CONTENT_DIR = CONTENT_DIR.parent

CONTENT_DIR = CONTENT_DIR.parent
CONTENT_DIR = CONTENT_DIR / "doc" / "fr" / "content" / "examples" / THIS_DIR.name / "no-dsl" / "basic"

FULL_TAG  = "full"
FULL_FILE = CONTENT_DIR / f"{FULL_TAG}.yaml"


# ----------- #
# -- TOOLS -- #
# ----------- #

def extract_single_kv(onedict):
    assert len(onedict.keys()) == 1

    for k, v in onedict.items():
        return (k, v)


def data_2_content(content, data, indent = '  '):
    if isinstance(data, str):
        content[-1] += f" {data}"

    elif isinstance(data, list):
        notfirstkey = False

        for info in data:
            if isinstance(info, str):
                content.append(f"{indent}- {info}")

            elif isinstance(info, dict):
                for key, val in info.items():
                    if notfirstkey:
                        newline = '\n'

                    else:
                        newline     = ''
                        notfirstkey = True

                    subcontent = [f"{newline}{indent}- {key}:"]

                    data_2_content(
                        content = subcontent,
                        data    = val,
                        indent = indent + '  '
                    )

                    content.append('\n'.join(subcontent))

            else:
                raise ValueError(f"unsupported format:\n{info}")

    else:
        raise ValueError(f"unsupported format:\n{data}")


# ----------------------------- #
# -- JUST KEEP ''full.yaml'' -- #
# ----------------------------- #

for p in CONTENT_DIR.glob("*.yaml"):
    if p.stem == FULL_TAG:
        continue

    p.unlink()


# ------------------------ #
# -- UPDATE THE CONTENT -- #
# ------------------------ #

full_yaml_doc = safe_load(FULL_FILE.read_text())
_, infos      = extract_single_kv(full_yaml_doc)

for block in infos:
    kind, data = extract_single_kv(block)

    assert kind != FULL_TAG

    part_file = CONTENT_DIR / f"{kind}.yaml"

    part_content = [f"- {kind}:"]

    data_2_content(part_content, data)

    part_content  = "\n".join(part_content)
    part_content += "\n"

    part_file.write_text(part_content)
