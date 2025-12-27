import webbrowser


def open_url(url: str):
    def handler(args, state):
        webbrowser.open(url)
    return handler


CUSTOM_COMMANDS = {
    # AI tools
    "gpt": open_url("https://chat.openai.com"),
    "gemini": open_url("https://gemini.google.com"),
    "grok": open_url("https://grok.com/"),

    # Dev / platforms
    "github": open_url("https://github.com/ritik-2407"),
    "vercel": open_url("https://vercel.com/ritik-2407s-projects"),
    "devdna": open_url("https://dev-dna-chi.vercel.app/"),
    "portfolio": open_url("https://ritik247.netlify.app/"),

    # Social / productivity
    "yt": open_url("https://youtube.com"),
    "meet": open_url("https://meet.google.com/xij-pjkr-bju?pli=1&authuser=1"),
    "twitter": open_url("https://twitter.com"),
    "x": open_url("https://twitter.com"),
    "linkedin": open_url("https://linkedin.com"),
}
