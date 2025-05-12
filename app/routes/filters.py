from fastapi import APIRouter, HTTPException
from sqlalchemy import text
from app.database import SessionLocal

router = APIRouter()

@router.get("/options/{column}")
def get_unique_values(column: str):
    """
    Get distinct values for a given column from the opta_bi table.
    Only pre-approved (whitelisted) columns are allowed to prevent SQL injection.
    """
    allowed_columns = [
        "teamName",
        "homeTeamName",
        "awayTeamName",
        "datePlayed",
        "actionName",
        "season",
        'playerName',
        "playerpositionName",
        "competitionName",
        "refereeName",
        "result"
    ]

    if column not in allowed_columns:
        raise HTTPException(status_code=400, detail=f"Column '{column}' is not allowed")
    
    db = SessionLocal()
    try:
        # Use raw SQL to fetch distinct values from the specified column
        query = text(f"SELECT DISTINCT {column} FROM opta_bi WHERE {column} IS NOT NULL")
        result = db.execute(query).fetchall()
        return [row[0] for row in result]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.close()