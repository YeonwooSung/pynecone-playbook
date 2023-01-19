import pynecone as pc

# custom modules
from .helpers import navbar
from .utils import State


def index():
    return pc.box(
        pc.vstack(
            navbar(State),
            login(),
        ),
        padding_top="10em",
        text_align="top",
        position="relative",
        width="100%",
        height="100vh",
        background="radial-gradient(circle at 22% 11%,rgba(62, 180, 137,.20),hsla(0,0%,100%,0) 19%),radial-gradient(circle at 82% 25%,rgba(33,150,243,.18),hsla(0,0%,100%,0) 35%),radial-gradient(circle at 25% 61%,rgba(250, 128, 114, .28),hsla(0,0%,100%,0) 55%)",
    )


def login():
    return pc.center(
        pc.vstack(
            pc.input(on_blur=State.set_username, placeholder="Username", width="100%"),
            pc.input(on_blur=State.set_password, placeholder="Password", width="100%"),
            pc.button("Login", on_click=State.login, width="100%"),
            pc.link(pc.button("Sign Up", width="100%"), href="/signup", width="100%"),
        ),
        shadow="lg",
        padding="1em",
        border_radius="lg",
        background="white",
    )


def signup():
    return pc.box(
        pc.vstack(
            pc.center(
                pc.vstack(
                    pc.heading("GPT Sign Up", font_size="1.5em"),
                    pc.input(
                        on_blur=State.set_username, placeholder="Username", width="100%"
                    ),
                    pc.input(
                        on_blur=State.set_password, placeholder="Password", width="100%"
                    ),
                    pc.input(
                        on_blur=State.set_password,
                        placeholder="Confirm Password",
                        width="100%",
                    ),
                    pc.button("Sign Up", on_click=State.signup, width="100%"),
                ),
                shadow="lg",
                padding="1em",
                border_radius="lg",
                background="white",
            )
        ),
        padding_top="10em",
        text_align="top",
        position="relative",
        width="100%",
        height="100vh",
        background="radial-gradient(circle at 22% 11%,rgba(62, 180, 137,.20),hsla(0,0%,100%,0) 19%),radial-gradient(circle at 82% 25%,rgba(33,150,243,.18),hsla(0,0%,100%,0) 35%),radial-gradient(circle at 25% 61%,rgba(250, 128, 114, .28),hsla(0,0%,100%,0) 55%)",
    )


def gpt():
    return pc.center(
        navbar(State),
        pc.vstack(
            pc.center(
                pc.vstack(
                    pc.heading("Ask GPT", font_size="1.5em"),
                    pc.input(
                        on_blur=State.set_prompt, placeholder="Question", width="100%"
                    ),
                    pc.button("Get Answer", on_click=State.get_result, width="100%"),
                    pc.text_area(
                        default_value=State.result,
                        placeholder="GPT Result",
                        width="100%",
                    ),
                    pc.button("Save Answer", on_click=State.save_result, width="100%"),
                    shadow="lg",
                    padding="1em",
                    border_radius="lg",
                    width="100%",
                ),
                width="100%",
            ),
            pc.center(
                pc.vstack(
                    pc.heading("Saved Q&A", font_size="1.5em"),
                    pc.divider(),
                    pc.data_table(
                        data=State.questions,
                        columns=["Question", "Answer"],
                        pagination=True,
                        search=True,
                        sort=True,
                        width="100%",
                    ),
                    shadow="lg",
                    padding="1em",
                    border_radius="lg",
                    width="100%",
                ),
                width="100%",
            ),
            width="50%",
            spacing="2em",
        ),
        padding_top="6em",
        text_align="top",
        position="relative",
    )

def dalle():
    return pc.center(
        pc.vstack(
            pc.heading("DALL-E", font_size="1.5em"),
            pc.input(placeholder="Enter a prompt..", on_blur=State.set_prompt),
            pc.button(
                "Generate Image",
                on_click=[State.process_image, State.get_image],
                width="100%",
            ),
            pc.divider(),
            pc.cond(
                State.image_processing,
                pc.circular_progress(is_indeterminate=True),
                pc.cond(
                    State.image_made,
                    pc.image(
                        src=State.image_url,
                        height="25em",
                        width="25em",
                    ),
                ),
            ),
            bg="white",
            padding="2em",
            shadow="lg",
            border_radius="lg",
        ),
        width="100%",
        height="100vh",
        background="radial-gradient(circle at 22% 11%,rgba(62, 180, 137,.20),hsla(0,0%,100%,0) 19%),radial-gradient(circle at 82% 25%,rgba(33,150,243,.18),hsla(0,0%,100%,0) 35%),radial-gradient(circle at 25% 61%,rgba(250, 128, 114, .28),hsla(0,0%,100%,0) 55%)",
    )


# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index)
app.add_page(signup)
app.add_page(login)
app.add_page(gpt)
app.add_page(dalle)
app.compile()
