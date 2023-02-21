class YouTubeChannel:
    def __init__(self,title,subscribers,movies):
        self.title = title
        self.subscribers = subscribers
        self.movies = movies

    def show_content(self):
        for item in self.movies:
            print(item.get_info_movie())
    def subscribe(self,subscriber):
        self.subscribers.append(subscriber)
        print(f"{subscriber.login} вы успешно подписаны на канал {self.title}")

    def unsubscribe(self, subscriber):
        self.subscribers.remove(subscriber)
        print(f"{subscriber.login} вы успешно отписались на канал {self.title}")

    def add_movie(self,movie):
        self.movies.append(movie)
        for item in self.subscribers:
            item.update(self.title,movie.title)
        print("Список доступных роликов ",self.show_content() )
