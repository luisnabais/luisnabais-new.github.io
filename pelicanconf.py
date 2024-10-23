AUTHOR = 'Luís Nabais'
SITENAME = 'Luís Nabais'
#SITEURL = 'https://luisnabais.github.io'
OUTPUT_PATH = 'output/'

# Theme settings
THEME = 'themes/nabais'
#THEME = 'Flex'
SITETITLE = 'Luís Nabais'
SITESUBTITLE = ' 🇵🇹 DevOps engineer, Linux specialist and trainer.<br />Passionate about Open Source, running, bodyweight fitness and travelling.'
SITEDESCRIPTION = ''
SITELOGO = '/images/profile.png'  # Add path to your logo if you have one


TIMEZONE = 'Europe/Lisbon'
DEFAULT_LANG = 'en'

PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['blog']  # If you have any articles, put them in a separate folder

# URL and save_as settings
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'

# Disable unnecessary features
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
#TAG_SAVE_AS = ''
#TAGS_SAVE_AS = ''

# Ensure no auto-generated index
INDEX_SAVE_AS = ''


# Static paths
STATIC_PATHS = ['images', 'extra']



# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Home', '/'),
    ('Blog', '/blog'),
)

# Social widget
SOCIAL = (
    ("linkedin", "https://linkedin.com/in/luisnabais"),
    ("mastodon", "https://mastodon.social/@luisnabais"),
    ("x-twitter",        "https://x.com/luis_nabais"),
    ("github",   "https://github.com/luisnabais"),
    ("gitlab",   "https://gitlab.com/luisnabais"),
)

MAIN_MENU = True
MENUITEMS = (
    ('Blog', '/blog'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True


# Content variables
#SITESUBTITLE = 'site_subtitle_variable'
STYLESHEET_URL = 'theme/css/style.css'


DIRECT_TEMPLATES = ['index', 'blog_index']
BLOG_INDEX_SAVE_AS = 'blog/index.html'
PAGINATED_TEMPLATES = {'index': None, 'blog_index': None}