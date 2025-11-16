class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise TypeError("author must be an Author")
        if not isinstance(magazine, Magazine):
            raise TypeError("magazine must be a Magazine")

        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("title must be a string between 5 and 50 characters")

        self.author = author
        self.magazine = magazine
        self._title = title

        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        if isinstance(new_title, str) and (5 <= len(new_title) <= 50):
            self._title = new_title


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("name must be a non-empty string")
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        return

    def articles(self):
        return [a for a in Article.all if a.author is self]

    def magazines(self):
        mags = []
        for a in self.articles():
            if a.magazine not in mags:
                mags.append(a.magazine)
        return mags

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if len(self.articles()) == 0:
            return None

        categories = []
        for m in self.magazines():
            if m.category not in categories:
                categories.append(m.category)
        return categories


class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("name must be a string between 2 and 16 characters")

        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("category must be a non-empty string")

        self._name = name
        self._category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and (2 <= len(new_name) <= 16):
            self._name = new_name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_cat):
        if isinstance(new_cat, str) and len(new_cat) > 0:
            self._category = new_cat

    def articles(self):
        return [a for a in Article.all if a.magazine is self]

    def contributors(self):
        authors = []
        for a in self.articles():
            if a.author not in authors:
                authors.append(a.author)
        return authors

    def article_titles(self):
        if len(self.articles()) == 0:
            return None
        return [a.title for a in self.articles()]

    def contributing_authors(self):
        counts = {}
        for a in self.articles():
            counts[a.author] = counts.get(a.author, 0) + 1
        result = [author for author, c in counts.items() if c > 2]
        return result if result else None
