import pynecone as pc


config = pc.Config(
    app_name="simple_multi_page",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
