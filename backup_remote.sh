
set -Eeuo pipefail

: "${DB_HOST:?Set DB_HOST}"
: "${DB_PORT:=3306}"
: "${DB_NAME:?Set DB_NAME}"
: "${DB_USER:?Set DB_USER}"
: "${MYSQL_PWD:?Set MYSQL_PWD}"

CONTAINER="university-mysql"

BACKUP_DIR="./backups"
mkdir -p "$BACKUP_DIR"

TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
BACKUP_FILE="$BACKUP_DIR/${DB_NAME}_remote_${TIMESTAMP}.sql"

echo "Backing up database: $DB_NAME via Docker container $CONTAINER"

docker exec \
  -e MYSQL_PWD="$MYSQL_PWD" \
  "$CONTAINER" \
  mysqldump \
    --user="$DB_USER" \
    --single-transaction \
    --no-tablespaces \
    "$DB_NAME" > "$BACKUP_FILE"

if [[ -s "$BACKUP_FILE" ]]; then
    echo "Backup created: $BACKUP_FILE"
else
    echo "Backup file is empty!"
    rm -f "$BACKUP_FILE"
    exit 1
fi

unset MYSQL_PWD
