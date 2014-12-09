from sqlalchemy import and_
from sqlalchemy import (
    Boolean, Column, Date, ForeignKey, Float,
    Integer, String, Text)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (
    scoped_session, sessionmaker, relationship)
from zope.sqlalchemy import ZopeTransactionExtension


DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class Cathedral(Base):
    __tablename__ = 'cathedrals'
    __table_args__ = (
        {'mysql_engine': 'InnoDB'}
    )

    slug = Column(String(100), primary_key=True)
    city = Column(String(100), primary_key=True)
    name = Column(String(100), nullable=False)
    summary = Column(Text, nullable=True)
    blurb = Column(Text, nullable=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    geometry = Column(Text, nullable=True)
    date_visited = Column(Date, nullable=True)

    features = relationship(
        'Story', backref='cathedral', primaryjoin=lambda: and_(
            Cathedral.slug == Story.cathedral_slug,
            Cathedral.city == Story.cathedral_city,
        )
    )

    blog = relationship(
        'BlogEntry', backref='cathedral', primaryjoin=lambda: and_(
            Cathedral.slug == BlogEntry.cathedral_slug,
            Cathedral.city == BlogEntry.cathedral_city,
        )
    )

    scores = relationship(
        'Score', backref='cathedral', primaryjoin=lambda: and_(
            Cathedral.slug == Score.cathedral_slug,
            Cathedral.city == Score.cathedral_city,
        )
    )


class StoryCode(Base):
    __tablename__ = 'story_codes'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    code = Column(String(100), primary_key=True)
    label = Column(String(255), nullable=False)


class Story(Base):
    __tablename__ = 'stories'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer(), primary_key=True)
    story_code = Column(ForeignKey(StoryCode.code), nullable=False)
    cathedral_slug = Column(ForeignKey(Cathedral.slug), nullable=False)
    cathedral_city = Column(ForeignKey(Cathedral.city), nullable=False)
    headline = Column(String(255), nullable=True)
    story = Column(Text, nullable=True)



class BlogEntry(Base):
    __tablename__ = 'blog_entries'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    id = Column(Integer(), primary_key=True)
    cathedral_slug = Column(ForeignKey(Cathedral.slug), nullable=False)
    cathedral_city = Column(ForeignKey(Cathedral.city), nullable=False)
    author = Column(String(100), nullable=True)
    date_written = Column(Date, nullable=False)
    published = Column(Boolean, nullable=False)
    blog = Column(Text, nullable=False)


class Score(Base):
    __tablename__ = 'scores'
    __table_args__ = {'mysql_engine': 'InnoDB'}

    story_code = Column(ForeignKey(StoryCode.code), primary_key=True)
    cathedral_slug = Column(ForeignKey(Cathedral.slug), primary_key=True)
    cathedral_city = Column(ForeignKey(Cathedral.city), primary_key=True)
    score = Column(Integer, nullable=False)
