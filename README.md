<h1 align="center">
  <br>
  <a href="https://github.com/karthikuj/SearchIt"><img src="https://i.ibb.co/jh7pYvB/SearchIt.png" alt="Arjun"></a>
  <br>
  SearchIt
  <br>
</h1>

<h4 align="center">Search multiple search engines through command line</h4>

![searchit-github](https://user-images.githubusercontent.com/59091280/110793736-e087b100-826c-11eb-80c5-72fed57293fd.png)


### About SearchIt

Ever using command line felt the need to browse the web but too lazy to open the browser and go to the desired search engine and type in the query?

This is like daily life for CLI focused users. And this is where SearchIt steps in, with some of the most popular search engines coded into it, 
you can now search for anything directly through the command line.

### Installing SearchIt

You can install `SearchIt` like this:

1. Clone the repository.
```
sudo git clone https://github.com/karthikuj/SearchIt.git
```

2. run the `setup.py` file.
```
sudo python3 setup.py install
```

### Using SearchIt

Syntax:
```
searchit [search engine] [search query]
```
Example:
```
searchit -y coldplay
```

Search Engines supported:
1. Google (Google, google, -g)
2. Youtube (Youtube, youtube, -yt, yt, -y)
3. Amazon (Amazon, amazon, -a)
4. Facebook (Facebook, facebook, fb, -f) (you need to be logged in for this)
5. Bing (Bing, bing, -b)
6. Search directly in browser's taskbar (Taskbar, taskbar, -tb)
7. Yandex (Yandex, yandex, -ya)

##### NOTE
This script won't run in `root` user.

#### Contributors

Karthik U.J. <a href="https://www.instagram.com/5up3r541y4n/">@5up3r541y4n</a>
