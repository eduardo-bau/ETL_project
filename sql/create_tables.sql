create table if not exists tracked_user (
    tracked_user_id INTEGER PRIMARY KEY,
    visitor_id VARCHAR,
    session_id VARCHAR,
    device_id VARCHAR,
    utm_source VARCHAR,
    traits JSON,
    first_seen DATETIME,
    last_seen DATETIME
);

create table if not exists event (
    event_id INTEGER PRIMARY KEY,
    tracked_user_id INTEGER REFERENCES tracked_user(tracked_user_id),
    event_time DATETIME,
    event_type VARCHAR,
    platform VARCHAR,
    campaign VARCHAR,
    cost FLOAT,
    revenue FLOAT,
    properties JSON

);