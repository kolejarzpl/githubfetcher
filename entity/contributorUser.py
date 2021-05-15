class Contributor:

    # TODO add contributor dedicated id for the database

    def __init__(self, login, id, node_id, avatar_url, gravatar_id, url, html_url, followers_url, following_url,
                 gists_url, starred_url, subscriptions_url, organizations_url, repos_url, events_url,
                 received_events_url, type, site_admin, contributions):
        self.login = login
        self.id = id
        self.node_id = node_id
        self.avatar_url = avatar_url
        self.gravatar_id = gravatar_id
        self.url = url
        self.html_url = html_url
        self.followers_url = followers_url
        self.following_url = following_url
        self.gists_url = gists_url
        self.starred_url = starred_url
        self.subscriptions_url = subscriptions_url
        self.organizations_url = organizations_url
        self.received_events_url = received_events_url
        self.repos_url = repos_url
        self.events_url = events_url
        self.type = type
        self.site_admin = site_admin
        self.contributions = contributions

    def __repr__(self):
        return "Contributor ('{}', '{}')".format(self.login, self.id)
