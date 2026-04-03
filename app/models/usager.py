from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey, Table
from app.database.database import Base
from sqlalchemy.orm import relationship

usager_role = Table(
    "usager_role",
    Base.metadata,
    Column("usager_id", ForeignKey("usager.id"), primary_key=True),
    Column("role_id", ForeignKey("role.id"), primary_key=True),
)

role_permission = Table(
    "role_permission",
    Base.metadata,
    Column("role_id", ForeignKey("role.id"), primary_key=True),
    Column("permission_id", ForeignKey("permission.id"), primary_key=True),
)

class Usager(Base):
    __tablename__ = "usager"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    sexe = Column(String)
    adresse = Column(String)
    date_naissance = Column(Date)
    identifiant = Column(String)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

    roles = relationship("Role", secondary=usager_role, back_populates="usagers")


class Role(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, unique=True, nullable=False)

    usagers = relationship("Usager", secondary=usager_role, back_populates="roles")
    permissions = relationship("Permission", secondary=role_permission, back_populates="roles")


class Permission(Base):
    __tablename__ = "permission"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, unique=True, nullable=False)

    roles = relationship("Role", secondary=role_permission, back_populates="permissions")