from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from flaskr.db import db
from flaskr.security import (
    parse_permission_overrides,
    permissions_for_role,
    serialize_permission_overrides,
)


class UserModel(db.Model):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(
        String(20), nullable=False, unique=True, index=True
    )
    
    email: Mapped[str] = mapped_column(
        String(120), nullable=False, unique=True, index=True
    )
    password: Mapped[str] = mapped_column(String(300), nullable=False)
    role: Mapped[str] = mapped_column(String(20), nullable=False, default="user")
    permission_overrides_raw: Mapped[str] = mapped_column(
        "permission_overrides",
        Text(),
        nullable=False,
        default='{"grants": [], "revokes": []}',
    )

    tasks = relationship(
        "TaskModel", back_populates="user", cascade="all, delete-orphan"
    )

    @property
    def custom_permissions(self):
        return parse_permission_overrides(self.permission_overrides_raw)

    @property
    def permissions(self):
        return permissions_for_role(self.role, self.custom_permissions)

    def set_permission_overrides(self, grants=None, revokes=None):
        self.permission_overrides_raw = serialize_permission_overrides(
            {"grants": grants or [], "revokes": revokes or []}
        )
