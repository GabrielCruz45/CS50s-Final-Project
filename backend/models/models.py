from sqlalchemy import Column, DateTime, String, Table, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

from app.db.database import Base


user_conversation_association = Table(
    "user_conversation_link",
    Base.metadata,
    Column("user_id", ForeignKey("users_table.id"), primary_key=True),
    Column("conversation_id", ForeignKey("conversations_table.id"), primary_key=True)
)


class User(Base):
    __tablename__ = "users_table"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(32), unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String(128)) # just to be safe; depends on hashing algorithm
    
    sent_messages: Mapped[list["Message"]] = relationship(back_populates="sender")
    
    conversations: Mapped[list["Conversation"]] = relationship(
        secondary=user_conversation_association,
        back_populates="users"
    )
   
 
class Conversation(Base):
    __tablename__ = "conversations_table"
    id: Mapped[int] = mapped_column(primary_key=True)
    
    # many-to-many: many users can be part of this convo
    users: Mapped[list["User"]] = relationship(
        secondary=user_conversation_association,
        back_populates="conversations"
    )
    
    # one-to-many: one conversation may have many messages; always add cascade with one-to-many on the parent side (where list[...] is)
    messages: Mapped[list["Message"]] = relationship(
        back_populates="conversation", 
        cascade="all, delete-orphan"
    )
    
    
class Message(Base):
    __tablename__ = "messages_table"
    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(String(512)) # check if 512 is too much space for a message
    created_at: Mapped[datetime] = mapped_column(insert_default=func.now()) # check if hour, minute, second is present
    
    sender_id: Mapped[int] = mapped_column(ForeignKey("users_table.id"))
    sender: Mapped["User"] = relationship(back_populates="sent_messages")
    
    conversation_id: Mapped[int] = mapped_column(ForeignKey("conversations_table.id"))
    conversation: Mapped["Conversation"] = relationship(back_populates="messages")