import threading

# Singleton class: Database
class Database:
    _instance = None
    _lock = threading.Lock()

    # Private constructor logic via __new__
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance.connection = "Database connection established"
                    print("Creating database instance")
        return cls._instance

    def query(self, sql: str) -> str:
        return f"Executing query: {sql} on {self.connection}"


# Main: demonstrating Singleton pattern
if __name__ == "__main__":
    # Get singleton instance
    db1 = Database()
    print(db1.query("SELECT * FROM users"))

    print()

    # Get singleton instance again (same instance)
    db2 = Database()
    print(db2.query("SELECT * FROM products"))

    print()

    # Verify both are the same instance
    print(f"db1 and db2 are the same instance: {db1 is db2}")
