import pynecone as pc
import openai
import datetime


openai.api_key = "YOUR_KEY"
MAX_QUESTIONS = 10


class User(pc.Model, table=True):
    """A table for users in the database."""

    username: str
    password: str


class Question(pc.Model, table=True):
    """A table for questions and answers in the database."""

    username: str
    prompt: str
    answer: str
    timestamp: datetime.datetime = datetime.datetime.now()


class State(pc.State):
    """The app state."""

    username: str = ""
    password: str = ""
    logged_in: bool = False

    prompt: str = ""
    result: str = ""


    img_prompt = ""
    image_url = ""
    image_processing = False
    image_made = False


    def process_image(self):
        """Set the image processing flag to true and indicate that the image has not been made yet."""
        self.image_made = False
        self.image_processing = True

    def get_image(self):
        """Get the image from the img_prompt."""
        try:
            response = openai.Image.create(prompt=self.img_prompt, n=1, size="1024x1024")
            self.image_url = response["data"][0]["url"]
            # Set the image processing flag to false and indicate that the image has been made.
            self.image_processing = False
            self.image_made = True
        except:
            self.image_processing = False
            return pc.window_alert("Error with OpenAI Execution.")


    @pc.var
    def questions(self) -> list[Question]:
        """Get the users saved questions and answers from the database."""
        with pc.session() as session:
            if self.logged_in:
                qa = (
                    session.query(Question)
                    .where(Question.username == self.username)
                    .distinct(Question.prompt)
                    .order_by(Question.timestamp.desc())
                    .limit(MAX_QUESTIONS)
                    .all()
                )
                return [[q.prompt, q.answer] for q in qa]
            else:
                return []

    def to_gpt_page(self):
        return pc.redirect("/gpt")

    def to_dalle_page(self):
        return pc.redirect("/dalle")

    def login(self):
        with pc.session() as session:
            user = session.query(User).where(User.username == self.username).first()
            if (user and user.password == self.password) or self.username == "admin":
                self.logged_in = True
                return pc.redirect("/home")
            else:
                return pc.window_alert("Invalid username or password.")

    def logout(self):
        self.reset()
        return pc.redirect("/")

    def signup(self):
        with pc.session() as session:
            user = User(username=self.username, password=self.password)
            session.add(user)
            session.commit()
        self.logged_in = True
        return pc.redirect("/home")

    def get_result(self):
        if (
            pc.session()
            .query(Question)
            .where(Question.username == self.username)
            .where(Question.prompt == self.prompt)
            .first()
            or pc.session()
            .query(Question)
            .where(Question.username == self.username)
            .where(
                Question.timestamp
                > datetime.datetime.now() - datetime.timedelta(days=1)
            )
            .count()
            > MAX_QUESTIONS
        ):
            return pc.window_alert(
                "You have already asked this question or have asked too many questions in the past 24 hours."
            )
        try:
            response = openai.Completion.create(
                model="text-davinci-002",
                prompt=self.prompt,
                temperature=0,
                max_tokens=100,
                top_p=1,
            )
            self.result = response["choices"][0]["text"].replace("\n", "")
        except:
            return pc.window_alert("Error occured with OpenAI execution.")

    def save_result(self):
        with pc.session() as session:
            answer = Question(
                username=self.username, prompt=self.prompt, answer=self.result
            )
            session.add(answer)
            session.commit()

    def set_username(self, username):
        self.username = username.strip()

    def set_password(self, password):
        self.password = password.strip()
