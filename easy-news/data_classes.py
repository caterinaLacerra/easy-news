import pandas as pd


class Article:
    def __init__(
        self,
        title: str,
        description: str,
        author: str,
        url: str,
        url_to_image: str,
        content: str,
        source: str,
        published_at: pd.Timestamp,
    ):
        self.title = title
        self.author = author
        self.description = description
        self.url = url
        self.source = source
        self.published_at = published_at
        self.url_to_image = url_to_image
        self.content = content

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data.get("title"),
            author=data.get("author"),
            description=data.get("description"),
            url=data.get("url"),
            url_to_image=data.get("url_to_image"),
            source=data.get("source", {}).get("name"),
            published_at=data.get("publishedAt"),
            content=data.get("content"),
        )

    def __str__(self) -> str:
        return f"{self.title} - {self.author}\n{self.description}"
