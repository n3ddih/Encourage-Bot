# Encourage Bot Discord

Created based on this [Youtube](https://www.youtube.com/watch?v=SPTfmiYiuok)

The bot is hosted on [repl.it](https://repl.it/)

## Running the bot

In order to run the bot:

- Create new repl on *repl.it*
- Upload 2 `.py` file to your new repl
- Create new bot in [discord developer applications](https://discord.com/developers/applications) portal
- Copy the bot token
- Go to repl.it and add new secret (environment variable) with **key** is `discord_bot_token` and **value** is your copied bot token
- Press `Run`

## To keep the bot alive

*Normally repl will stop the bot if you close the browser but will keep a web server. So the webserver was created to prevent this.*
*But while running a webserver, it would stop if there's no request after times.*

- Run the bot and you will see a page with content `Hello I'm alive`
- Copy the domain name of the page. E.g: `https://Encourage-Bot.n3ddih.repl.co`
- Add a monitor in [uptimerobot.com](https://uptimerobot.com/)

> This *uptimerobot* monitor will ping the url for every interval time set therefore the web server is kept alive
