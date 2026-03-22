from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.job import Job

def get_total_jobs(db: Session) -> int:
    return db.query(Job).count()

def get_jobs_by_location(db: Session) -> list:
    result = db.query(Job.location, func.count(Job.id).label('total')).group_by(Job.location).all()
    
    return [{"location": row.location, "total": row.total} for row in result]