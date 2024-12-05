from singer_sdk import typing as th

issuesSchema = th.PropertiesList(
    th.Property("id", th.StringType),
    th.Property("title", th.StringType),
    th.Property("url", th.StringType),
    th.Property("createdAt", th.DateTimeType),
    th.Property("updatedAt", th.DateTimeType),
    th.Property("canceledAt", th.DateTimeType),
    th.Property("completedAt", th.DateTimeType),
    th.Property("dueDate", th.DateTimeType),
    th.Property("priority", th.IntegerType),
    th.Property("priorityLabel", th.StringType),
    th.Property("description", th.StringType),

    th.Property(
        "creator",
        th.ObjectType(
            th.Property("id", th.StringType),
            th.Property("name", th.StringType),
            th.Property("email", th.StringType),
        ),
    ),
    th.Property(
        "assignee",
        th.ObjectType(
            th.Property("id", th.StringType),
            th.Property("name", th.StringType),
            th.Property("email", th.StringType),
        ),
    ),
    th.Property(
        "project",
        th.ObjectType(
            th.Property("id", th.StringType),
            th.Property("name", th.StringType),
        ),
    ),
    th.Property(
        "team",
        th.ObjectType(
            th.Property("id", th.StringType),
            th.Property("name", th.StringType),
        ),
    ),
    th.Property(
        "state",
        th.ObjectType(
            th.Property("createdAt", th.DateTimeType),
            th.Property("id", th.StringType),
            th.Property("name", th.StringType),
            th.Property("updatedAt", th.DateTimeType),
            th.Property("position", th.IntegerType)
        ),
    ),
).to_dict()
