
set -Eeuo pipefail

CONTAINER="university-mysql"
DATABASE="university_db"
BACKUP_DIR="./backups"

mkdir -p "$BACKUP_DIR"

TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
BACKUP_FILE="$BACKUP_DIR/${DATABASE}_${TIMESTAMP}.sql"

echo "Creating backup of $DATABASE..."

docker exec "$CONTAINER" sh -c \
  'exec mysqldump -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" "$MYSQL_DATABASE"' \
  > "$BACKUP_FILE"

if [[ -s "$BACKUP_FILE" ]]; then
    echo "Backup created: $BACKUP_FILE"
else
    echo "Backup file is empty!"
    rm -f "$BACKUP_FILE"
    exit 1
fi
