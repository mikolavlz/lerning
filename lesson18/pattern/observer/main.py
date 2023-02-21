from VideoItem import Movie
from subscriber import Subscriber
from YouTubeChannel import YouTubeChannel

movie1 = Movie("Python 1","СОержимое ролика1 ....")
movie2 = Movie("Java","СОержимое ролика2 ....")
movie3 = Movie("JS","СОержимое ролика3 ....")

movies =[movie1,movie2,movie3]
subscriber1 = Subscriber('User1',["Java","JS","Puthon"])
subscriber2 = Subscriber('User2',["Java","JS","Puthon"])
subscriber3 = Subscriber('User3',["Java","JS","Puthon"])

my_channel = YouTubeChannel("Языки",[subscriber1,subscriber2,subscriber3],movies)

new_subscriber = Subscriber("Oler",["Java","JS"])
my_channel.unsubscribe(my_channel.subscribers[0])