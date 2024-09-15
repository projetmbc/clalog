from pathlib import Path
from yaml    import safe_load


# --------------- #
# -- CONSTANTS -- #
# --------------- #

THIS_DIR = Path(__file__).parent

API_CFG_DIR = THIS_DIR

while(API_CFG_DIR.name != "tests"):
    API_CFG_DIR = API_CFG_DIR.parent

API_CFG_DIR = API_CFG_DIR.parent
API_CFG_DIR = API_CFG_DIR / "contribute" / "api" / "class-log" / "en"


# ----------- #
# -- TOOLS -- #
# ----------- #


# ----------- #
# -- XX -- #
# ----------- #

for p in API_CFG_DIR.glob("*.yaml"):
    print(p)
