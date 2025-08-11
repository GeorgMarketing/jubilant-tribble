import aiosqlite
from typing import Optional
from .config import settings


CREATE_USERS_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    tg_id INTEGER UNIQUE NOT NULL,
    username TEXT,
    full_name TEXT,
    role TEXT, -- business | individual | nonresident
    funnel TEXT, -- import_export | marketplace | usdt | faq | contact
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

CREATE_EVENTS_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY,
    tg_id INTEGER NOT NULL,
    username TEXT,
    full_name TEXT,
    action TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""


async def init_db() -> None:
    async with aiosqlite.connect(settings.DB_PATH) as db:
        await db.execute(CREATE_USERS_TABLE_SQL)
        await db.execute(CREATE_EVENTS_TABLE_SQL)
        await db.commit()


async def upsert_user(tg_id: int, username: Optional[str], full_name: Optional[str]) -> None:
    async with aiosqlite.connect(settings.DB_PATH) as db:
        await db.execute(
            """
            INSERT INTO users (tg_id, username, full_name)
            VALUES (?, ?, ?)
            ON CONFLICT(tg_id) DO UPDATE SET username=excluded.username, full_name=excluded.full_name
            """,
            (tg_id, username, full_name),
        )
        await db.commit()


async def set_user_role(tg_id: int, role: str) -> None:
    async with aiosqlite.connect(settings.DB_PATH) as db:
        await db.execute("UPDATE users SET role=? WHERE tg_id=?", (role, tg_id))
        await db.commit()


async def set_user_funnel(tg_id: int, funnel: str) -> None:
    async with aiosqlite.connect(settings.DB_PATH) as db:
        await db.execute("UPDATE users SET funnel=? WHERE tg_id=?", (funnel, tg_id))
        await db.commit()


async def log_event(tg_id: int, username: Optional[str], full_name: Optional[str], action: str) -> None:
    async with aiosqlite.connect(settings.DB_PATH) as db:
        await db.execute(
            "INSERT INTO events (tg_id, username, full_name, action) VALUES (?, ?, ?, ?)",
            (tg_id, username, full_name, action),
        )
        await db.commit()


async def export_events_to_csv(csv_path: str) -> str:
    import csv
    async with aiosqlite.connect(settings.DB_PATH) as db:
        async with db.execute(
            "SELECT tg_id, username, full_name, action, created_at FROM events ORDER BY id DESC"
        ) as cursor:
            rows = await cursor.fetchall()
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["tg_id", "username", "full_name", "action", "created_at"])
        for r in rows:
            writer.writerow(r)
    return csv_path


