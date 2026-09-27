import shutil
from datetime import datetime

name=f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.sqlite3"

shutil.copy("db.sqlite3",name)

print("Backup Created:",name)
