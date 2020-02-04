from wordz import (
    Combinator,
    logs,
)


class FileExtensions(Combinator):

    def process(self):
        basic = self.base('wordlists/http/files/extensions/basic.txt')
        extended = self.base('wordlists/http/files/extensions/extended.txt')
        self.sort(basic, self.temp('extensions-basic.txt'))
        self.sort(extended, self.temp('extensions-extended.txt'))
        self.compare(self.temp('extensions-basic.txt'), self.temp('extensions-extended.txt'), extended)
        self.delete(basic)
        self.copy(self.temp('extensions-basic.txt'), basic)


class HttpWords(Combinator):

    wordlists = (
        'src/keywords/http/paths/adj-adv-det-all.txt',
        'src/keywords/http/paths/adj-adv-det-basic.txt',
        'src/keywords/http/paths/nouns-all.txt',
        'src/keywords/http/paths/nouns-basic.txt',
        'src/keywords/http/paths/verbs-all.txt',
        'src/keywords/http/paths/verbs-basic.txt',
        'src/keywords/http/paths/suffixes.txt',
    )
    rules = (
        'src/rules/lowercase.rule',
        'src/rules/capitalize.rule',
    )

    def setup(self):
        logs.logger.info('Generating HTTP paths/params')

        # NOTE: Process keywords
        self.wordlists_process()

        for lst in ['adj-adv-det', 'nouns', 'verbs']:
            self.diff('src/keywords/http/paths', lst)


class HttpWordsPlain(HttpWords):

    def process(self):
        lowercase_verbs = self.temp(f'lowercase-paths-verbs-{self.group_name}.txt')
        lowercase_nouns = self.temp(f'lowercase-paths-nouns-{self.group_name}.txt')
        lowercase_aads = self.temp(f'lowercase-paths-adj-adv-det-{self.group_name}.txt')

        # NOTE: lowercase paths
        self.merge(
            self.output(f'wordlists/http/paths/lowercase/plain-{self.group_name}.txt'),
            (
                lowercase_verbs,
                lowercase_nouns,
                lowercase_aads,
                self.right(lowercase_verbs, lowercase_nouns),
                self.right(lowercase_nouns, lowercase_verbs),
                self.right(lowercase_aads, lowercase_nouns),
                self.right(lowercase_verbs, lowercase_aads),
                self.right(lowercase_nouns, lowercase_aads),
            )
        )

        verbs_sep = self.right(lowercase_verbs, self.base('src/bits/separators-dash.txt'))
        nouns_sep = self.right(lowercase_nouns, self.base('src/bits/separators-dash.txt'))
        aads_sep = self.right(lowercase_aads, self.base('src/bits/separators-dash.txt'))

        # NOTE: dash-case paths
        self.merge(
            self.output(f'wordlists/http/paths/dash/plain-{self.group_name}.txt'),
            (
                lowercase_verbs,
                lowercase_nouns,
                lowercase_aads,
                self.right(verbs_sep, lowercase_nouns),
                self.right(nouns_sep, lowercase_verbs),
                self.right(aads_sep, lowercase_nouns),
                self.right(verbs_sep, lowercase_aads),
                self.right(nouns_sep, lowercase_aads),
            )
        )

        verbs_sep = self.right(lowercase_verbs, self.base('src/bits/separators-underscore.txt'))
        nouns_sep = self.right(lowercase_nouns, self.base('src/bits/separators-underscore.txt'))
        aads_sep = self.right(lowercase_aads, self.base('src/bits/separators-underscore.txt'))

        # NOTE: snake_case paths
        self.merge(
            self.output(f'wordlists/http/paths/underscore/plain-{self.group_name}.txt'),
            (
                lowercase_verbs,
                lowercase_nouns,
                lowercase_aads,
                self.right(verbs_sep, lowercase_nouns),
                self.right(nouns_sep, lowercase_verbs),
                self.right(aads_sep, lowercase_nouns),
                self.right(verbs_sep, lowercase_aads),
                self.right(nouns_sep, lowercase_aads),
            )
        )

        capitalize_verbs = self.temp(f'capitalize-paths-verbs-{self.group_name}.txt')
        capitalize_nouns = self.temp(f'capitalize-paths-nouns-{self.group_name}.txt')
        capitalize_aads = self.temp(f'capitalize-paths-adj-adv-det-{self.group_name}.txt')

        # NOTE: CamelCase paths
        self.merge(
            self.output(f'wordlists/http/paths/camelcase/plain-{self.group_name}.txt'),
            (
                capitalize_verbs,
                capitalize_nouns,
                capitalize_aads,
                self.right(capitalize_verbs, capitalize_nouns),
                self.right(capitalize_nouns, capitalize_verbs),
                self.right(capitalize_aads, capitalize_nouns),
                self.right(capitalize_verbs, capitalize_aads),
                self.right(capitalize_nouns, capitalize_aads),
            )
        )

        # NOTE: lowerCamelCase paths
        self.merge(
            self.output(f'wordlists/http/paths/lowercamelcase/plain-{self.group_name}.txt'),
            (
                lowercase_verbs,
                lowercase_nouns,
                lowercase_aads,
                self.right(lowercase_verbs, capitalize_nouns),
                self.right(lowercase_nouns, capitalize_verbs),
                self.right(lowercase_aads, capitalize_nouns),
                self.right(lowercase_verbs, capitalize_aads),
                self.right(lowercase_nouns, capitalize_aads),
            )
        )


class HttpWordsObjects(HttpWords):

    def process(self):
        lowercase_nouns = self.temp(f'lowercase-paths-nouns-{self.group_name}.txt')

        # NOTE: lowercase paths
        self.merge(
            self.output(f'wordlists/http/paths/lowercase/objects-{self.group_name}.txt'),
            (
                lowercase_nouns,
                self.right(lowercase_nouns, lowercase_nouns),
            )
        )

        nouns_sep = self.right(lowercase_nouns, self.base('src/bits/separators-dash.txt'))

        # NOTE: dash-case paths
        self.merge(
            self.output(f'wordlists/http/paths/dash/objects-{self.group_name}.txt'),
            (
                lowercase_nouns,
                self.right(nouns_sep, lowercase_nouns),
            )
        )

        nouns_sep = self.right(lowercase_nouns, self.base('src/bits/separators-underscore.txt'))

        # NOTE: snake_case paths
        self.merge(
            self.output(f'wordlists/http/paths/underscore/objects-{self.group_name}.txt'),
            (
                lowercase_nouns,
                self.right(nouns_sep, lowercase_nouns),
            )
        )

        capitalize_nouns = self.temp(f'capitalize-paths-nouns-{self.group_name}.txt')

        # NOTE: CamelCase paths
        self.merge(
            self.output(f'wordlists/http/paths/camelcase/objects-{self.group_name}.txt'),
            (
                capitalize_nouns,
                self.right(capitalize_nouns, capitalize_nouns),
            )
        )

        # NOTE: lowerCamelCase paths
        self.merge(
            self.output(f'wordlists/http/paths/lowercamelcase/objects-{self.group_name}.txt'),
            (
                lowercase_nouns,
                self.right(lowercase_nouns, capitalize_nouns),
            )
        )


class HttpWordsSuffixes(HttpWords):

    def process(self):
        lowercase_nouns = self.temp(f'lowercase-paths-nouns-{self.group_name}.txt')
        lowercase_aads = self.temp(f'lowercase-paths-adj-adv-det-{self.group_name}.txt')
        lowercase_suffixes = self.temp('lowercase-paths-suffixes.txt')
        aads_nouns = self.right(lowercase_aads, lowercase_nouns)

        # NOTE: lowercase paths
        self.merge(
            self.output(f'wordlists/http/paths/lowercase/suffixes-{self.group_name}.txt'),
            (
                self.right(aads_nouns, lowercase_suffixes),
            )
        )

        nouns_sep = self.right(lowercase_nouns, self.base('src/bits/separators-dash.txt'))
        aads_sep = self.right(lowercase_aads, self.base('src/bits/separators-dash.txt'))
        aads_nouns_sep = self.right(aads_sep, nouns_sep)

        # NOTE: dash-case paths
        self.merge(
            self.output(f'wordlists/http/paths/dash/suffixes-{self.group_name}.txt'),
            (
                self.right(aads_nouns_sep, lowercase_suffixes),
            )
        )

        nouns_sep = self.right(lowercase_nouns, self.base('src/bits/separators-underscore.txt'))
        aads_sep = self.right(lowercase_aads, self.base('src/bits/separators-underscore.txt'))
        aads_nouns_sep = self.right(aads_sep, nouns_sep)

        # NOTE: snake_case paths
        self.merge(
            self.output(f'wordlists/http/paths/underscore/suffixes-{self.group_name}.txt'),
            (
                self.right(aads_nouns_sep, lowercase_suffixes),
            )
        )

        capitalize_nouns = self.temp(f'capitalize-paths-nouns-{self.group_name}.txt')
        capitalize_aads = self.temp(f'capitalize-paths-adj-adv-det-{self.group_name}.txt')
        capitalize_suffixes = self.temp('capitalize-paths-suffixes.txt')
        aads_nouns = self.right(capitalize_aads, capitalize_nouns)

        # NOTE: CamelCase paths
        self.merge(
            self.output(f'wordlists/http/paths/camelcase/suffixes-{self.group_name}.txt'),
            (
                self.right(aads_nouns, capitalize_suffixes),
            )
        )

        aads_nouns = self.right(lowercase_aads, capitalize_nouns)

        # NOTE: lowerCamelCase paths
        self.merge(
            self.output(f'wordlists/http/paths/lowercamelcase/suffixes-{self.group_name}.txt'),
            (
                self.right(aads_nouns, capitalize_suffixes),
            )
        )


class HttpWordsDouble(HttpWords):

    def process(self):
        lowercase_verbs = self.temp(f'lowercase-paths-verbs-{self.group_name}.txt')
        lowercase_nouns = self.temp(f'lowercase-paths-nouns-{self.group_name}.txt')
        lowercase_aads = self.temp(f'lowercase-paths-adj-adv-det-{self.group_name}.txt')
        aads_nouns = self.right(lowercase_aads, lowercase_nouns)

        # NOTE: lowercase paths
        self.merge(
            self.output(f'wordlists/http/paths/lowercase/double-{self.group_name}.txt'),
            (
                self.right(lowercase_verbs, aads_nouns),
            )
        )

        verbs_sep = self.right(lowercase_verbs, self.base('src/bits/separators-dash.txt'))
        aads_sep = self.right(lowercase_aads, self.base('src/bits/separators-dash.txt'))
        aads_nouns = self.right(aads_sep, lowercase_nouns)

        # NOTE: dash-case paths
        self.merge(
            self.output(f'wordlists/http/paths/dash/double-{self.group_name}.txt'),
            (
                self.right(verbs_sep, aads_nouns),
            )
        )

        verbs_sep = self.right(lowercase_verbs, self.base('src/bits/separators-underscore.txt'))
        aads_sep = self.right(lowercase_aads, self.base('src/bits/separators-underscore.txt'))
        aads_nouns = self.right(aads_sep, lowercase_nouns)

        # NOTE: snake_case paths
        self.merge(
            self.output(f'wordlists/http/paths/underscore/double-{self.group_name}.txt'),
            (
                self.right(verbs_sep, aads_nouns),
            )
        )

        capitalize_verbs = self.temp(f'capitalize-paths-verbs-{self.group_name}.txt')
        capitalize_nouns = self.temp(f'capitalize-paths-nouns-{self.group_name}.txt')
        capitalize_aads = self.temp(f'capitalize-paths-adj-adv-det-{self.group_name}.txt')
        aads_nouns = self.right(capitalize_aads, capitalize_nouns)

        # NOTE: CamelCase paths
        self.merge(
            self.output(f'wordlists/http/paths/camelcase/double-{self.group_name}.txt'),
            (
                self.right(capitalize_verbs, aads_nouns),
            )
        )

        # NOTE: lowerCamelCase paths
        self.merge(
            self.output(f'wordlists/http/paths/lowercamelcase/double-{self.group_name}.txt'),
            (
                self.right(lowercase_verbs, aads_nouns),
            )
        )


class HttpWordsPlainCommon(HttpWordsPlain):

    group_name = 'basic'


class HttpWordsObjectsCommon(HttpWordsObjects):

    group_name = 'basic'


class HttpWordsSuffixesCommon(HttpWordsSuffixes):

    group_name = 'basic'


class HttpWordsDoubleCommon(HttpWordsDouble):

    group_name = 'basic'


class HttpWordsPlainAll(HttpWordsPlain):

    group_name = 'all'


class HttpWordsObjectsAll(HttpWordsObjects):

    group_name = 'all'


class HttpWordsSuffixesAll(HttpWordsSuffixes):

    group_name = 'all'


class HttpWordsDoubleAll(HttpWordsDouble):

    group_name = 'all'
