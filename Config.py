import os

# Bot token from @botfather
BOT_TOKEN = os.environ.get("5571720532:AAEM8BtRRH_fY_sSh2HDgqN3-vsa6CK43gQ")
# From my.telegram.org/
API_ID = int(os.environ.get("18990697", 0))
API_HASH = os.environ.get("f4815b9a16cb03c2f5eabe8db1cb0903")
# For /log cmd
OWNER_ID = [int(i) for i in os.environ.get("OWNER_ID", "5261482689").split(" ")]
# No time limit for this users
AUTH_USERS = [int(i) for i in os.environ.get("AUTH_USERS", "5261482689").split(" ")]
# Time gap after each request (in seconds)
TIME_GAP = int(os.environ.get("TIME_GAP", "360"))
# Bot channel ID for ForceSub, don't forget to add bot in Bot Channel
UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", False)
