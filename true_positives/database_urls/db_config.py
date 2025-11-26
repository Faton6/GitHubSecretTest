#!/usr/bin/env python3
"""
Database Connection URLs Test File
⚠️ WARNING: All credentials below are FAKE and non-functional.
Used ONLY for research and testing purposes.
"""

# PostgreSQL Connection URLs
DATABASE_URL = "postgresql://admin:SuperSecret123!@db.example.com:5432/production"
POSTGRES_URL = "postgres://user:password123@localhost:5432/mydb"
PG_CONNECTION = "postgresql://dbuser:dbpass@192.168.1.100:5432/appdb"

# MySQL Connection URLs
MYSQL_URL = "mysql://root:rootpassword@mysql.example.com:3306/database"
MYSQL_CONNECTION = "mysql+pymysql://admin:Admin123!@localhost/myapp"

# MongoDB Connection URLs
MONGODB_URI = "mongodb://admin:MongoPass123@mongo.example.com:27017/production"
MONGO_URL = "mongodb+srv://user:password@cluster.mongodb.net/mydb"

# Redis Connection
REDIS_URL = "redis://:redispassword123@redis.example.com:6379/0"
REDIS_CONNECTION = "redis://user:password@localhost:6379"

# SQLite (no password, but included for completeness)
SQLITE_PATH = "sqlite:///path/to/database.db"

class DatabaseConfig:
    """Database configuration holder"""
    
    def __init__(self):
        self.postgres_url = "postgresql://prod_user:ProdPass123!@db.prod.com:5432/app"
        self.mysql_url = "mysql://admin:Secret123@mysql.internal:3306/data"
        self.mongodb_uri = "mongodb://mongo_user:MongoSecret@mongo.internal:27017"
