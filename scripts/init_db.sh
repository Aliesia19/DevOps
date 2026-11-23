

set -e

DB_SERVICE="${1:-db}"

echo "Initializing database..."

docker compose exec -T "$DB_SERVICE" \
    psql -U "$DB_USER" -d "$DB_NAME" \
    < sql/init.sql

echo "Database initialization completed!"
