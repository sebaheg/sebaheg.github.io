"""Personal blog built with Reflex - Static version for GitHub Pages."""

import reflex as rx
from pathlib import Path
import frontmatter


# Posts directory
POSTS_DIR = Path(__file__).parent.parent / "posts"


def get_all_posts() -> list[dict]:
    """Get all blog posts sorted by date (newest first)."""
    posts = []
    if POSTS_DIR.exists():
        for md_file in POSTS_DIR.glob("*.md"):
            post = frontmatter.load(md_file)
            posts.append({
                "slug": md_file.stem,
                "title": post.get("title", md_file.stem),
                "date": str(post.get("date", "")),
                "description": post.get("description", ""),
                "content": post.content,
                "publish": post.get("publish", True),
            })
    posts.sort(key=lambda x: x["date"], reverse=True)
    return posts


# Load all posts at build time (static)
ALL_POSTS = get_all_posts()
PUBLISHED_POSTS = [p for p in ALL_POSTS if p["publish"]]
POSTS_BY_SLUG = {p["slug"]: p for p in ALL_POSTS}


class State(rx.State):
    """Minimal state - not used for content."""
    pass


def navbar() -> rx.Component:
    """Simple navigation bar."""
    return rx.box(
        rx.hstack(
            rx.link(
                rx.text("~", class_name="text-lg"),
                href="/",
                class_name="no-underline text-inherit hover:opacity-70",
            ),
            justify="between",
            align="center",
            width="100%",
        ),
        class_name="py-6 border-b border-gray-200",
    )


def post_item(post: dict) -> rx.Component:
    """A single post item in the list."""
    return rx.link(
        rx.hstack(
            rx.text(
                post["date"],
                class_name="text-gray-500 font-mono text-sm w-28 shrink-0",
            ),
            rx.text(
                post["title"],
                class_name="font-mono",
            ),
            justify="start",
            align="center",
            gap="4",
            width="100%",
        ),
        href=f"/post/{post['slug']}",
        class_name="no-underline text-inherit hover:opacity-70 py-2 block",
    )


def index() -> rx.Component:
    """Home page - list of published blog posts."""
    return rx.box(
        navbar(),
        rx.box(
            rx.text(
                "posts",
                class_name="font-mono text-sm text-gray-500 mb-4",
            ),
            *[post_item(post) for post in PUBLISHED_POSTS],
            class_name="py-8",
        ),
        class_name="max-w-2xl mx-auto px-4",
    )


def create_post_page(post: dict) -> rx.Component:
    """Create a static post page component."""
    return rx.box(
        navbar(),
        rx.box(
            rx.link(
                rx.text(
                    "<- back",
                    class_name="font-mono text-sm text-gray-500 hover:text-gray-700",
                ),
                href="/",
                class_name="no-underline",
            ),
            rx.box(
                rx.text(
                    post["date"],
                    class_name="font-mono text-sm text-gray-500",
                ),
                rx.heading(
                    post["title"],
                    class_name="font-mono text-2xl mt-2 mb-6",
                ),
                class_name="mt-8 mb-6",
            ),
            rx.markdown(
                post["content"],
                class_name="prose prose-sm font-mono",
            ),
            class_name="py-8",
        ),
        class_name="max-w-2xl mx-auto px-4",
    )


# Custom stylesheets
stylesheets = [
    "https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css",
    "/styles.css",
]

app = rx.App(
    enable_state=False,
    stylesheets=stylesheets,
    theme=rx.theme(
        appearance="light",
        accent_color="gray",
    ),
)

# Add index page
app.add_page(index, route="/", title="Blog")

# Add each post as a static page
for post in ALL_POSTS:
    # Unpublished posts get noindex meta tag to prevent search engine indexing
    meta = [] if post["publish"] else [{"name": "robots", "content": "noindex, nofollow"}]
    app.add_page(
        lambda p=post: create_post_page(p),
        route=f"/post/{post['slug']}",
        title=post["title"],
        meta=meta,
    )
