import pynecone as pc


class WordCycleState(pc.State):
    # The words to cycle through.
    text = ["Welcome", "to", "Pynecone", "!"]

    # The index of the current word.
    index = 0

    def next_word(self):
        self.index = (self.index + 1) % len(self.text)

    @pc.var
    def get_text(self):
        return self.text[self.index]


def index():
    return pc.heading(
        WordCycleState.get_text,
        on_mouse_over=WordCycleState.next_word,
        color="green",
    )


# Add state and page to the app.
app = pc.App(state=WordCycleState)
app.add_page(index)
app.compile()
