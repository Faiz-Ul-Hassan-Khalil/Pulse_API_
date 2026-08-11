"""
Database table definitions for PulseAPI.

Defines the predictions table that stores every prediction
request and response for history and analysis.
"""

from datetime import datetime, timezone # here datetime is used to get the current date and time, and timezone is used to ensure that the timestamp is in UTC
from sqlalchemy import Integer, Float, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.database.connection import Base


class Prediction(Base):
    """
    Represents one prediction request stored in the database.

    Every time /predict is called successfully, one row gets
    inserted into this table.
    """

    __tablename__ = "predictions"  # The name of the table in the database. This is where all prediction records will be stored.

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True) # The unique identifier for each prediction. It's an integer that auto-increments with each new entry.
    
    # these are the 13 chemical features that the model uses to make predictions. Each feature is stored as a float in the database and cannot be null.
    # Input features
    alcohol: Mapped[float] = mapped_column(Float, nullable=False)
    malic_acid: Mapped[float] = mapped_column(Float, nullable=False)
    ash: Mapped[float] = mapped_column(Float, nullable=False)
    alcalinity_of_ash: Mapped[float] = mapped_column(Float, nullable=False)
    magnesium: Mapped[float] = mapped_column(Float, nullable=False)
    total_phenols: Mapped[float] = mapped_column(Float, nullable=False)
    flavanoids: Mapped[float] = mapped_column(Float, nullable=False)
    nonflavanoid_phenols: Mapped[float] = mapped_column(Float, nullable=False)
    proanthocyanins: Mapped[float] = mapped_column(Float, nullable=False)
    color_intensity: Mapped[float] = mapped_column(Float, nullable=False)
    hue: Mapped[float] = mapped_column(Float, nullable=False)
    od280_od315_of_diluted_wines: Mapped[float] = mapped_column(Float, nullable=False)
    proline: Mapped[float] = mapped_column(Float, nullable=False)

    # Output
    predicted_class: Mapped[int] = mapped_column(Integer, nullable=False)
    class_name: Mapped[str] = mapped_column(String, nullable=False)
    confidence: Mapped[float] = mapped_column(Float, nullable=False)

    created_at: Mapped[datetime] = mapped_column(
    DateTime, default=lambda: datetime.now(timezone.utc).replace(tzinfo=None), nullable=False
)