![homepage](/main_app/static/images/readme/home.png)

![allchars](/main_app/static/images/readme/chars.png)

![details](/main_app/static/images/readme/detail.png)

# Description

#### This is a platform where DBZ's fans can share their opinion about their favorite characters and their best skills. Users have the ability to create characters and manage their content using the Create Read Update Delete (CRUD) operations.


<p>&nbsp;</p>

# **Getting Started  [dbzcollector.fly.dev](https://dbzcollector.fly.dev/about)**


<p>&nbsp;</p>

# Installation

**Clone my project.**

```bash
git clone https://github.com/TuanNguyen0915/dragon_ball_character_collector
```

**Install docker desktop and add it to the system path.**

```
https://docs.docker.com/get-docker/
```

**Install docker extension from vscode**
```
To install the extension, open the Extensions view (MacOS) -> (⇧+⌘+X) , (Windows) -> (Ctrl+Shift+X ) , search for docker to filter results and select Docker extension authored by Microsoft.
```
**Create an account from neon.tech for database**
```
https://neon.tech/
```

**Create the .env**

```bash
NEON_USER=< YOUR_USERNAME >
NEON_DATABASE_NAME=neondb
NEON_HOST=< AFTER @ TO TECH/ >
NEON_PASSWORD=< YOUR_PASSWORD >
```
**Using docker extension**

![shell](/main_app/static/images/readme/shell.png)

**Run 3 lines (step by step) **
```
python3 manage.py startapp main_app
python3 manage.py makemigrations
python3 manage.py migrate
```

**Run the code on terminal **
```
sudo docker compose up
```
** To turn off the app **
```
sudo docker compose down
```

<p>&nbsp;</p>

# Attributions

- ### Google font:
    -   [Bangers](https://fonts.google.com/?query=bangers)
    -   [Bona Nova](https://fonts.google.com/?query=Bona+Nova)

- ### Icon for about section:
    -   [fontawesome.com](https://fontawesome.com/)

- ### Image:
    -   [wallpaperflare.com](https://www.wallpaperflare.com/search?wallpaper=Dragon+Ball+Super)
    -   [wall.alphacoders.com](https://wall.alphacoders.com/by_sub_category.php?id=179743&name=Dragon+Ball+Z+Wallpapers)

- ### Information about characters:
    -   [dragonball.fandom.com](https://dragonball.fandom.com/wiki/Main_Page)

<p>&nbsp;</p>

# Technologies Used

- ### Python
- ### Django
- ### CSS flexbox
- ### Git
- ### fly.io
