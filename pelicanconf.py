# Site Information
AUTHOR = 'Luís Nabais'
SITENAME = 'Luís Nabais'
SITETITLE = 'Luís Nabais'
SITESUBTITLE = ' 🇵🇹 DevOps engineer, Linux specialist and trainer.<br />Passionate about Open Source, running, bodyweight fitness and travelling.'
SITEDESCRIPTION = ''
SITELOGO = '/images/profile.png'

# Locale and Timezone
TIMEZONE = 'Europe/Lisbon'
DEFAULT_LANG = 'en'

# Theme Settings
THEME = 'themes/nabais'
STYLESHEET_URL = 'theme/css/style.css'

# Paths and URLs
PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['blog']
STATIC_PATHS = ['images', 'extra']

PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'

# Disable features
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
TAG_SAVE_AS = ''
TAGS_SAVE_AS = ''
INDEX_SAVE_AS = ''

# Feed Settings
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Navigation
MAIN_MENU = True
MENUITEMS = (
    ('Blog', '/blog'),
)

LINKS = (
    ('Home', '/'),
    ('Blog', '/blog'),
)

SOCIAL = (
    ("linkedin", "https://linkedin.com/in/luisnabais"),
    ("mastodon", "https://mastodon.social/@luisnabais"),
    ("x-twitter", "https://x.com/luis_nabais"),
    ("github",   "https://github.com/luisnabais"),
    ("gitlab",   "https://gitlab.com/luisnabais"),
)

# Pagination
DEFAULT_PAGINATION = 10


# Templates
DIRECT_TEMPLATES = ['index', 'blog_index']
BLOG_INDEX_SAVE_AS = 'blog/index.html'
PAGINATED_TEMPLATES = {'index': None, 'blog_index': None}

# Uncomment to use relative URLs in development
# RELATIVE_URLS = True

# Uncomment these lines when ready to publish
# SITEURL = 'https://nabais.eu'
# OUTPUT_PATH = 'output/'