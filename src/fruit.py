# 使用する型
from sqlalchemy import Column, Integer, String
# テーブルとの紐付けに使用するBaseオブジェクト
from db import Base

# テーブル名
TABLE_NAME = 'fruits'

# Fruit モデル
class Fruit(Base):
    # テーブルと紐付ける
    __tablename__ = TABLE_NAME

    # id カラム
    id = Column(Integer, primary_key=True)
    # name カラム
    name = Column(String)
    # country カラム
    country = Column(String)

    def __init__(self, name, country):
        self.name = name
        self.country = country

    def __str__(self):
        return 'id:{}, name:{}, country:{}'.format(self.id, self.name, self.country)
    