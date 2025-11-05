#!/usr/bin/env bash
echo "Borrando la base de datos AI-ModelDB..."
mongosh "mongodb://localhost:27017/AI-ModelDB" --eval "db.dropDatabase()"
echo "Base de datos limpia."
fastapi dev main.py