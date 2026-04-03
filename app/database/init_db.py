from datetime import date
from sqlalchemy.orm import Session

from .database import Base, engine, SessionLocal
from .models import Usager, Role, Permission
from .auth import hash_password


def init_db():
    Base.metadata.create_all(bind=engine)

    db: Session = SessionLocal()

    try:
        permissions_data = [
            "read_usager",
            "create_usager",
            "update_usager",
            "delete_usager",
        ]

        for perm_name in permissions_data:
            existing_perm = db.query(Permission).filter(Permission.nom == perm_name).first()
            if not existing_perm:
                db.add(Permission(nom=perm_name))

        db.commit()

        admin_role = db.query(Role).filter(Role.nom == "admin").first()
        if not admin_role:
            admin_role = Role(nom="admin")
            db.add(admin_role)

        user_role = db.query(Role).filter(Role.nom == "user").first()
        if not user_role:
            user_role = Role(nom="user")
            db.add(user_role)

        db.commit()
        db.refresh(admin_role)
        db.refresh(user_role)

        all_permissions = db.query(Permission).all()
        read_permission = db.query(Permission).filter(Permission.nom == "read_usager").first()

        admin_role.permissions = all_permissions
        user_role.permissions = [read_permission]

        db.commit()

        admin_email = "admin@email.com"
        admin_user = db.query(Usager).filter(Usager.email == admin_email).first()

        if not admin_user:
            admin_user = Usager(
                nom="Admin",
                email=admin_email,
                sexe="M",
                adresse="Adresse admin",
                date_naissance=date(1990, 1, 1),
                mot_de_passe_hash=hash_password("admin123"),
                is_active=True
            )
            admin_user.roles.append(admin_role)
            db.add(admin_user)
            db.commit()

    finally:
        db.close()