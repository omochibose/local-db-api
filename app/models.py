from sqlalchemy import Column, Integer, String, Float, Date, Time
from app.database import Base

class OptaBi(Base):
    __tablename__ = "opta_bi"

    id = Column(Integer, primary_key=True, index=True)
    playerName = Column(String(255))
    teamName = Column(String(255))
    ps_timestamp = Column(Float)
    ps_endstamp = Column(Float)
    x_coord = Column(Integer)
    y_coord = Column(Integer)
    x_coord_end = Column(Integer)
    y_coord_end = Column(Integer)
    actionName = Column(String(255))
    ActionTypeName = Column(String(255))
    ActionResultName = Column(String(255))
    qualifier3Name = Column(String(255))
    qualifier4Name = Column(String(255))
    qualifier5Name = Column(String(255))
    qualifier6Name = Column(String(255))
    datePlayed = Column(Date)
    kickofftime = Column(Time)
    season = Column(Integer)
    playerpositionName = Column(String(255))
    refereeName = Column(String(255))
    competitionName = Column(String(255))
    isHome = Column(String(255))
    result = Column(String(255))

