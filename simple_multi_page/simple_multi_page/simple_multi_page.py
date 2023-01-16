"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(pc.State):
    """The app state."""

    pass


def index():
    return pc.text("Root Page")


def about():
    return pc.text("About Page")


app = pc.App(state=State)
app.add_page(index, path="/")
app.add_page(about, path="/about")
app.compile()
