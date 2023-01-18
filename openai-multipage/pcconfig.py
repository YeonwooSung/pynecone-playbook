import pynecone as pc


config = pc.Config(
    app_name="openai_multipage",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
