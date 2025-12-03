from models import Base, Calculation
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'sqlite:///./proekt.db'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Получаем все записи
calculations = session.query(Calculation).all()
print(f'Всего записей: {len(calculations)}')
for calc in calculations:
    print(f'ID: {calc.id}, Операция: {calc.operation}, X: {calc.x}, Y: {calc.y}, Результат: {calc.result}, Время: {calc.created_at}')

session.close()
