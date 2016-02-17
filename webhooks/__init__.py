from tornado.web import Application
from webhooks._default import DefaultHandler
from webhooks.github import GithubHandler
from webhooks.karma import KarmaHandler

# Single Handler Apps
all_handlers = [
    (r"/", DefaultHandler),
    (r"/github", GithubHandler),
    (r"/karma", KarmaHandler)
]

# Multi Handler Apps
# all_handlers.extend(handlers_list)

app = Application(all_handlers)
