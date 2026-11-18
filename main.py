from database import SessionLocal
from repositories.guide_repository import GuideRepository

def main():
    db = SessionLocal()
    repo = GuideRepository(db)

    print("--- Создание гида ---")
    new_guide = repo.create("Петров Петр", "Москва", "+7-999-123-45-67")
    print(f"Добавлен гид: {new_guide.full_name}, Город: {new_guide.city}")

    print("\n--- Получение списка всех гидов ---")
    guides = repo.get_all()
    for g in guides:
        print(f"ID: {g.id}, ФИО: {g.full_name}, Город: {g.city}")

    print("\n--- Обновление города гида ---")
    repo.update_city(new_guide.id, "Санкт-Петербург")
    print(f"Гид {new_guide.full_name} теперь работает в городе Санкт-Петербург")

    db.close()

if __name__ == "__main__":
    main()