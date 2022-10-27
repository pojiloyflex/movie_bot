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
    "десять негритят":
    Movie(name="Десять негритят 1987",
          description="советский двухсерийный художественный полнометражный цветной детективный фильм Станислава Говорухина по одноимённому роману Агаты Кристи (1939), снятый на Одесской киностудии. Экранизация сохранила пессимистический характер концовки романа, не были изменены ни персонажи, ни их прошлое. Это также первая экранизация, в которой было сохранено исходное название романа.",
          link="https://www.youtube.com/watch?v=uoTDsuSgPBw"),
    "Джейн Эйр":
    Movie(name="Jane Eyre 1983",
          description="телеэкранизация одноимённого романа английской писательницы Шарлотты Бронте. Это вторая экранизация, выпущенная BBC.",
          link="https://www.youtube.com/watch?v=0DiqUwK4jYM"),
    "сестра Керри":
    Movie(name="Carrie 1952",
          description="кинофильм режиссёра Уильяма Уайлера, вышедший на экраны в 1952 году. Экранизация одноимённого романа Теодора Драйзера (1900)",
          link="https://okko.tv/movie/carrie-16824287?utm_medium=referral&utm_source=yandex_search&utm_campaign=new_search_feed"),
    "отверженные":
    Movie(name=" Les Misérables 2012",
          description="драматический мюзикл Тома Хупера. Экранизация мюзикла по одноимённому роману-эпопее Виктора Гюго (1862)",
          link="https://www.kinopoisk.ru/film/566055/"),
    "великий гэтсби":
    Movie(name="The Great Gatsby 1974",
          description="ретья по счету экранизация одноимённого романа Фрэнсиса Скотта Фицджеральда под режиссурой Джека Клэйтона. 2 премии «Оскар» за Лучшую музыку и Лучший дизайн костюмов.",
          link="https://okko.tv/movie/the-great-gatsby-79185?utm_medium=referral&utm_source=yandex_search&utm_campaign=new_search_feed"),
    "гордость и предубеждение":
    Movie(name="Pride and Prejudice 2005",
          description="фильм режиссёра Джо Райта по мотивам одноимённого романа Джейн Остин 1813 года. Главные роли исполнили Кира Найтли и Мэттью Макфэдьен",
          link="https://www.kinopoisk.ru/film/81733/"),
    "грозовой перевал":
    Movie(name="Wuthering Heights 1992",
          description="британская романа Эмили Бронте Питера Козмински с Рэйфом Файнсом и Жульет Бинош в главных ролях.",
          link="https://okko.tv/movie/wuthering-heights?utm_medium=referral&utm_source=yandex_search&utm_campaign=new_search_feed"),
    "анна каренина":
    Movie(name="Анна Каренина 1967",
          description="советский широкоформатный художественный фильм режиссёра Александра Зархи в двух частях по одноимённому роману Льва Николаевича Толстого",
          link="https://www.kinopoisk.ru/film/43498/"),
    "моби дик":
    Movie(name="Moby Dick 1956",
          description="экранизация знаменитого романа Германа Мелвилла. Продюсер и режиссёр — Джон Хьюстон. Фильм точно передаёт основной сюжет книги, вплоть до сохранения оригинального текста монологов и диалогов.",
          link="https://okko.tv/movie/moby-dick-47320608?utm_medium=referral&utm_source=yandex_search&utm_campaign=new_search_feed"),
    "Разум и чувства":
    Movie(name="Sense and Sensibility 1995",
          description="мелодрама по мотивам одноимённого романа британской романистки Джейн Остин. Премии BAFTA, «Золотой глобус» и «Оскар», главный приз Берлинале «Золотой медведь». Также шесть номинаций на премию «Оскар», в том числе как лучшему фильму года. В главных ролях: Эмма Томпсон, Кейт Уинслет, Алан Рикман, Хью Грант.",
          link="https://www.kinopoisk.ru/film/6148/"),
    "прощай, оружие":
    Movie(name="A Farewell to Arms 1932",
          description="фильм американского режиссёра Фрэнка Борзейги, снятый в 1932 году на киностудии Paramount Pictures по сюжету одноимённого романа Эрнеста Хемингуэя. Картина была номинирована на 4 премии Оскар, из которых получила две — за лучшую операторскую работу и за лучший звук. Главные роли исполнили: Гэри Купер, Хелен Хейс, Адольф Менжу.",
          link="https://www.kinopoisk.ru/film/3382/"),
} 