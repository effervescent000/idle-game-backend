from sqlalchemy import Column, Float, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship, DeclarativeBase


class Base(DeclarativeBase):
    pass


class AutoIntPK:
    id = Column(Integer, primary_key=True)


class AuditTimes:
    created_at = Column(Integer, default=func.now())
    updated_at = Column(Integer)


class User(AutoIntPK, Base):
    __tablename__ = "users"

    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String)

    heroes = relationship("Hero", back_populates="user")


class HeroAbilities(Base):
    __tablename__ = "hero_abilities"

    hero_id = Column(Integer, ForeignKey("heroes.id"), primary_key=True)
    ability_id = Column(Integer, ForeignKey("abilities.id"), primary_key=True)

    rank = Column(Integer, default=0)

    ability = relationship("Ability")
    hero = relationship("Hero", back_populates="abilities")


class Hero(AutoIntPK, AuditTimes, Base):
    __tablename__ = "heroes"

    name = Column(String, nullable=False)
    level = Column(Integer, nullable=False, default=1)
    hero_class = Column(String, nullable=False)
    max_health = Column(Integer, nullable=False)
    cur_health = Column(Float, nullable=False)
    max_mana = Column(Integer, nullable=False)
    cur_mana = Column(Float, nullable=False)

    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="heroes")
    abilities = relationship("HeroAbilities", back_populates="hero")


class Ability(AutoIntPK, AuditTimes, Base):
    __tablename__ = "abilities"

    name = Column(String, nullable=False)
    hero_class = Column(String, nullable=False)
    execution_time = Column(Float, default=0)
    cooldown = Column(Float, default=0)
    base_damage = Column(Integer, nullable=False)
    damage_coefficient = Column(Float, nullable=False)
    target_count = Column(Integer, default=1)
