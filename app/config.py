from pathlib import Path

# IAMLite SQLite Database Configuration
SQLITE_DB_PATH = Path(f"{__file__}/../db/iam_admins.db").resolve()
SQLITE_CONFIG_TABLE_NAME = "iam_config"
SQLITE_ADMINS_TABLE_NAME = "iam_admins"

# Application Configuration
APP_TITLE = "IAMLite"