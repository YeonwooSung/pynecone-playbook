import pynecone as pc


config = pc.Config(
    app_name="simple_event_example",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
