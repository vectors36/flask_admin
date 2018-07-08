from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from datetime import datetime
from sqlalchemy.orm import backref, relationship


Base = declarative_base()


class Documents(Base):
    __tablename__ = 'documents'

    doc_id = Column(Integer, primary_key=True)
    doc_title = Column(String(255), nullable=False)
    # tested for large paragraphs. no loss of text on 978 word test
    doc_contents = Column(String(), nullable=True)
    pub_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    pub_update = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)


engine = create_engine('postgresql://testuser:test123@localhost/docs')


Base.metadata.create_all(engine)
