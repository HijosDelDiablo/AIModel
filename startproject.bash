#!/usr/bin/env bash
sudo chown -R $USER:$USER .
sudo docker start ollama
sudo docker compose up --build -d
# Limpiar la base de datos MongoDB

# Usar credenciales si están en .env (MONGO_INITDB_ROOT_USERNAME, MONGO_INITDB_ROOT_PASSWORD)
if [ -f .env ]; then
	export $(grep -v '^#' .env | xargs)
fi

# Construir URI con authSource=admin para poder ejecutar dropDatabase
mongosh "mongodb://${MONGO_INITDB_ROOT_USERNAME:-admin}:${MONGO_INITDB_ROOT_PASSWORD:-password123}@localhost:27017/AI-ModelDB?authSource=admin" --eval "db.dropDatabase()"
echo "Base de datos limpia."
fastapi dev main.py