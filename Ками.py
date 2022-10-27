class Movie:
    def __init__(self, name, description, link):
        """

        :rtype: object
        """
        self.name = name
        self.description = description
        self.link = link

    def get_text(self):
        return 'Название фильма: ' + self.name + '\n\n' + 'Описание: ' + self.description + '\n\n' + 'Ccылка: ' + self.link


def getMovieCollection():
    return "\n".join(list(movie_collection.keys()))


movie_collection = {
    "убийство на улице морг":
        Movie(name="Убийство на улице Морг",
              description="Телевизионный фильм. Режиссёром выступил Жанно Шварц, главные роли исполнили Джордж К. Скотт, Ребекка Де Морнэй, Иэн МакШейн и Вэл Килмер",
              link="https://youtu.be/B9SKE_uwzWk"),
    "тайна мари роже":
        Movie(name="Тайна Мари Роже",
              description="фильм-нуар, детективный фильм с участием Патрика Ноулза. История была адаптирована из рассказа «Тайна Мари Роже », написанного Эдгаром Алланом По в 1842 году. Фильм снят Филом Розен и производство Universal Pictures , действие происходит в 1889 году.",
              link="https://www.youtube.com/watch?v=HuX4aIATgAo"),

}