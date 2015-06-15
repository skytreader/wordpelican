from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import BigInteger, Column, DateTime, Integer, String, UnicodeText

Base = declarative_base()


class WPUsers(Base):
    __tablename__ = "wp_users"
    id = Column(BigInteger, primary_key=True)
    user_login = Column(String(60), nullable=False, default="")
    user_pass = Column(String(64), nullable=False, default="")
    user_nicename = Column(String(50), nullable=False, default="")
    user_email = Column(String(100), nullable=False, default="")
    user_url = Column(String(100), nullable=False, default="")
    # FIXME Add default vlaue
    user_registered = Column(DateTime, nullable=False)
    user_activation_key = Column(String(60), nullable=False, default="")
    user_status = Column(Integer, nullable=False, default=0)
    display_name = Column(String(250), nullable=False, default="")


class WPPost(Base):
    __tablename__ = "wp_posts"
    id = Column(BigInteger, primary_key=True)
    # This should actually FK to wp_users but since WP is using MyISAM
    post_author = Column(BigInteger, nullable=False, default=0)
    post_date = Column(DateTime, nullable=False)
    post_date_gmt = Column(DateTime, nullable=False)
    post_content = Column(UnicodeText, nullable=False)
    post_title = Column(UnicodeText, nullable=False)
    post_excerpt = Column(UnicodeText, nullable=False)
    post_status = Column(String(20), nullable=False, default="publish")
    comment_status = Column(String(20), nullable=False, default="open")
    ping_status = Column(String(20), nullable=False, default="open")
    post_password = Column(String(20), nullable=False, default="")
    post_name = Column(String(200), nullable=False, default="")
    to_ping = Column(UnicodeText, nullable=False)
    pinged = Column(UnicodeText, nullable=False)
    post_modified = Column(DateTime, nullable=False)
    post_modified_gmt = Column(DateTime, nullable=False)
    post_parent = Column(BigInteger, nullable=False, default=0)
    guid = Column(String(255), nullable=False, default="")
    menu_order = Column(Integer, nullable=False, default=0)
    post_type = Column(Integer, nullable=False, default="post")
    post_mime_type = Column(String(100), nullable=False, default="")
    comment_count = Column(BigInteger, nullable=False, default=0)
