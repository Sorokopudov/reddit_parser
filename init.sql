CREATE TABLE IF NOT EXISTS users (
    id VARCHAR PRIMARY KEY,
    username VARCHAR NOT NULL,
    link_karma INTEGER,
    post_karma INTEGER,
    created_at TIMESTAMP WITHOUT TIME ZONE
);

CREATE TABLE IF NOT EXISTS posts (
    id VARCHAR PRIMARY KEY,
    user_id VARCHAR REFERENCES users(id),
    title TEXT,
    text TEXT,
    subreddit_id VARCHAR,
    created_at TIMESTAMP WITHOUT TIME ZONE
);

CREATE TABLE IF NOT EXISTS comments (
    id VARCHAR PRIMARY KEY,
    user_id VARCHAR REFERENCES users(id),
    text TEXT,
    parent_id VARCHAR,
    subreddit_id VARCHAR,
    created_at TIMESTAMP WITHOUT TIME ZONE
);
