from db import SessionLocal, Memory

def save_memory(user_id: str, key: str, value: str):
    db = SessionLocal()
    record = db.query(Memory).filter_by(user_id=user_id, key=key).first()

    if record:
        record.value = value
    else:
        record = Memory(user_id=user_id, key=key, value=value)
        db.add(record)

    db.commit()
    db.close()

def get_all_memory(user_id: str) -> dict:
    db = SessionLocal()
    records = db.query(Memory).filter_by(user_id=user_id).all()
    db.close()

    return {r.key: r.value for r in records}
