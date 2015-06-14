from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, Integer, String

Base = declarative_base()


class WPUsers(Base):
    __tablename__ = "wp_users"
    id = Column(Integer, primary_key=True)
    user_login = Column(String(60), nullable=False, default="")
    user_pass = Column(String(64), nullable=False, default="")
    user_nicenmae = Column(String(50), nullable=False, default="")
    user_email = Column(String(100), nullable=False, default="")
    user_url = Column(String(100), nullable=False, default="")
    # FIXME Add default vlaue
    user_registered = Column(DateTime, nullable=False)
    user_activation_key = Column(String(60), nullable=False, default="")
    user_status = Column(Integer, nullable=False, default=0)
    display_name = Column(String(250), nullable=False, default="")


class WPPost(Base):
    __tablename__ = "wp_posts"
    id = Column(Integer, primary_key=True)
    # This should actually FK to wp_users but since WP is using MyISAM
    post_author = Column(Integer, nullable=False, default=0)
