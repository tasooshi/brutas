from wordz import (
    Combinator,
    logs,
)


class Passwords(Combinator):

    passwords_all = 'passwords-all.txt'
    wordlists = (
        'wordlists/passwords/classics.txt',
        'wordlists/passwords/patterns.txt',
        'wordlists/passwords/top.txt',
        'wordlists/passwords/unique.txt',
        'wordlists/usernames/basic.txt',
        'wordlists/usernames/all.txt',
        'src/keywords/lang/all.txt',
        'src/keywords/lang/int-basic.txt',
        'src/keywords/lang/int-extended.txt',
    )
    rules = (
        'src/rules/both.rule',
        'src/rules/complex.rule',
        'src/rules/hax0r.rule',
        'src/rules/repeat.rule',
        'src/rules/simple.rule',
    )

    def setup(self):
        logs.logger.info('Preparing bits')
        for lst in ['extra', 'numbers']:
            self.diff('src/bits', lst)

        logs.logger.info('Preparing keyword lists')

        basic = self.base('src/keywords/lang/int-basic.txt')
        extended = self.base('src/keywords/lang/int-extended.txt')
        self.sort(basic, self.temp('lowercase-lang-int-basic.txt'))
        self.sort(extended, self.temp('lowercase-lang-int-extended.txt'))
        self.compare(self.temp('lowercase-lang-int-basic.txt'), self.temp('lowercase-lang-int-extended.txt'), extended)
        self.delete(basic)
        self.copy(self.temp('lowercase-lang-int-basic.txt'), basic)

        # NOTE: Combine all languages
        self.delete(self.base('src/keywords/lang/all.txt'))
        self.sort(self.base('src/keywords/lang/*.txt'), self.temp('lowercase-lang-all.txt'), unique=True)
        self.copy(self.temp('lowercase-lang-all.txt'), self.base('src/keywords/lang/all.txt'))

        # NOTE: Initialize lookup/compare set
        if not self.temp(self.passwords_all).is_file():
            self.sort(self.base('wordlists/passwords/1-xxs.txt'), self.temp(self.passwords_all))

        # NOTE: Process keywords
        self.wordlists_process()

        # NOTE: Prepare some lists beforehand
        separators = self.base('src/bits/separators.txt')
        self.left(self.temp('simple-usernames-all.txt'), separators)
        self.left(self.temp('simple-usernames-basic.txt'), separators)
        self.right(self.temp('simple-usernames-all.txt'), separators)
        self.right(self.temp('simple-usernames-basic.txt'), separators)
        self.right(self.temp('simple-passwords-patterns.txt'), separators)


class BasicPasswords(Passwords):

    def process(self):
        self.merge(
            self.output('wordlists/passwords/2-xs.txt'),
            (
                self.base('wordlists/passwords/classics.txt'),
                self.base('wordlists/passwords/patterns.txt'),
                self.base('wordlists/usernames/all.txt'),
            ),
            compare=self.temp(self.passwords_all)
        )

        self.merge(
            self.output('wordlists/passwords/3-s.txt'),
            (
                self.base('wordlists/passwords/numbers.txt'),
                self.base('wordlists/passwords/top.txt'),
                self.base('wordlists/passwords/unique.txt'),
                self.left(self.temp('simple-usernames-basic.txt'), self.base('src/bits/extra-basic.txt')),
                self.left(self.temp('simple-usernames-basic.txt'), self.base('src/bits/functional.txt')),
                self.right(self.temp('simple-usernames-basic.txt'), self.base('src/bits/extra-basic.txt')),
                self.right(self.temp('simple-usernames-basic+extra-basic.txt'), self.base('src/bits/years-current.txt')),
                self.right(self.temp('simple-usernames-basic+separators.txt'), self.base('src/bits/functional.txt')),
                self.right(self.temp('simple-usernames-basic+separators.txt'), self.base('src/bits/months.txt')),
                self.right(self.temp('simple-usernames-basic+separators.txt'), self.base('src/bits/years-current.txt')),
                self.right(self.temp('simple-usernames-basic.txt'), self.base('src/bits/numbers-basic.txt')),
                self.right(self.temp('simple-usernames-basic.txt'), self.base('src/bits/years-current.txt')),
                self.rule(self.base('wordlists/usernames/basic.txt'), self.base('src/rules/overkill.rule')),
                self.temp('overkill-usernames-basic.txt'),
                self.temp('repeat-usernames-basic.txt'),
                self.temp('simple-passwords-classics.txt'),
                self.temp('simple-passwords-top.txt'),
                self.temp('simple-usernames-basic.txt'),
            ),
            compare=self.temp(self.passwords_all)
        )

        self.merge(
            self.output('wordlists/passwords/4-m.txt'),
            (
                self.left(self.temp('separators+simple-usernames-basic.txt'), self.base('src/bits/functional.txt')),
                self.left(self.temp('separators+simple-usernames-basic.txt'), self.base('src/bits/years-current.txt')),
                self.right(self.temp('simple-lang-int-basic.txt'), self.base('src/bits/extra-top.txt')),
                self.right(self.temp('simple-passwords-patterns.txt'), self.base('src/bits/months.txt')),
                self.right(self.temp('simple-passwords-patterns.txt'), self.base('src/bits/numbers-basic.txt')),
                self.right(self.temp('simple-passwords-patterns.txt'), self.base('src/bits/years-current.txt')),
                self.right(self.temp('simple-usernames-basic+extra-basic.txt'), self.base('src/bits/extra-basic.txt')),
                self.right(self.temp('simple-usernames-basic+numbers-basic.txt'), self.base('src/bits/extra-basic.txt')),
                self.right(self.temp('simple-usernames-basic+years-current.txt'), self.base('src/bits/extra-basic.txt')),
                self.right(self.temp('simple-usernames-basic.txt'), self.base('src/bits/extra-extended.txt')),
                self.right(self.temp('simple-usernames-basic.txt'), self.base('src/bits/years-all.txt')),
                self.rule(self.rule(self.base('wordlists/usernames/basic.txt'), self.base('src/rules/repeat.rule')), self.base('src/rules/both.rule')),
                self.temp('both-passwords-classics.txt'),
                self.temp('both-passwords-patterns.txt'),
                self.temp('both-tmp-repeat-usernames-basic.txt'),
                self.temp('both-usernames-all.txt'),
                self.temp('hax0r-usernames-all.txt'),
                self.temp('repeat-usernames-basic.txt'),
                self.temp('simple-lang-int-basic.txt'),
            ),
            compare=self.temp(self.passwords_all)
        )


class ExtendedPasswords(Passwords):

    def process(self):
        # NOTE: Generate here, don't include in merge
        self.right(self.temp('simple-lang-int-basic.txt'), self.base('src/bits/months.txt'))
        self.right(self.temp('simple-lang-int-basic.txt'), self.base('src/bits/years-all.txt'))
        self.right(self.temp('simple-lang-int-basic.txt'), self.base('src/bits/separators.txt'))
        self.right(self.temp('simple-lang-int-basic+months.txt'), self.base('src/bits/separators.txt'))
        self.right(self.temp('simple-lang-int-basic+years-all.txt'), self.base('src/bits/separators.txt'))

        self.merge(
            self.output('wordlists/passwords/5-l.txt'),
            (
                self.right(self.temp('simple-usernames-all.txt'), self.base('src/bits/extra-basic.txt')),
                self.right(self.temp('simple-usernames-all.txt'), self.base('src/bits/years-all.txt')),
                self.right(self.temp('simple-usernames-all.txt'), self.base('src/bits/numbers-basic.txt')),
                self.left(self.temp('simple-usernames-basic.txt'), self.base('src/bits/extra-basic.txt')),
                self.left(self.temp('simple-usernames-basic.txt'), self.base('src/bits/functional.txt')),
                self.left(self.temp('simple-usernames-basic.txt'), self.base('src/bits/numbers-basic.txt')),
                self.right(self.temp('extra-basic+simple-usernames-basic.txt'), self.base('src/bits/months.txt')),
                self.right(self.temp('extra-basic+simple-usernames-basic.txt'), self.base('src/bits/years-current.txt')),
                self.right(self.temp('hax0r-lang-int-basic.txt'), self.base('src/bits/extra-basic.txt')),
                self.right(self.temp('hax0r-usernames-basic.txt'), self.base('src/bits/extra-basic.txt')),
                self.right(self.temp('simple-lang-int-basic.txt'), self.base('src/bits/extra-basic.txt')),
                self.right(self.temp('simple-lang-int-basic.txt'), self.base('src/bits/months.txt')),
                self.right(self.temp('simple-lang-int-extended.txt'), self.base('src/bits/extra-top.txt')),
                self.right(self.temp('simple-passwords-patterns.txt'), self.base('src/bits/extra-basic.txt')),
                self.right(self.temp('simple-passwords-patterns.txt'), self.base('src/bits/numbers-extended.txt')),
                self.right(self.temp('simple-passwords-patterns.txt'), self.base('src/bits/years-all.txt')),
                self.right(self.temp('simple-usernames-basic+extra-basic.txt'), self.base('src/bits/years-current.txt')),
                self.right(self.temp('simple-usernames-basic+separators.txt'), self.base('src/bits/months.txt')),
                self.right(self.temp('simple-usernames-basic+separators.txt'), self.base('src/bits/years-current.txt')),
                self.right(self.temp('simple-usernames-basic+years-all.txt'), self.base('src/bits/extra-basic.txt')),
                self.right(self.temp('simple-usernames-basic.txt'), self.base('src/bits/extra-basic.txt')),
                self.right(self.temp('simple-usernames-basic.txt'), self.base('src/bits/extra-extended.txt')),
                self.right(self.temp('simple-usernames-basic.txt'), self.base('src/bits/numbers-basic.txt')),
                self.right(self.temp('simple-usernames-basic.txt'), self.base('src/bits/years-all.txt')),
                self.rule(self.rule(self.base('wordlists/usernames/basic.txt'), self.base('src/rules/repeat.rule')), self.base('src/rules/both.rule')),
                self.rule(self.base('wordlists/usernames/basic.txt'), self.base('src/rules/overkill.rule')),
                self.rule(self.temp('hax0r-lang-int-basic.txt'), self.base('src/rules/capitalize.rule')),
                self.rule(self.temp('hax0r-lang-int-basic+extra-basic.txt'), self.base('src/rules/capitalize.rule')),
                self.temp('both-passwords-top.txt'),
                self.temp('both-passwords-unique.txt'),
                self.temp('both-tmp-repeat-usernames-basic.txt'),
                self.temp('capitalize-tmp-hax0r-lang-int-basic+extra-basic.txt'),
                self.temp('capitalize-tmp-hax0r-lang-int-basic.txt'),
                self.temp('complex-usernames-basic.txt'),
                self.temp('hax0r-passwords-classics.txt'),
                self.temp('hax0r-passwords-top.txt'),
                self.temp('hax0r-passwords-unique.txt'),
                self.temp('hax0r-usernames-basic.txt'),
                self.temp('overkill-usernames-basic.txt'),
                self.temp('simple-lang-int-extended.txt'),
            ),
            compare=self.temp(self.passwords_all)
        )

        self.merge(
            self.output('wordlists/passwords/6-xl.txt'),
            (
                self.both(self.temp('repeat-usernames-basic.txt'), self.base('src/bits/extra-basic.txt')),
                self.left(self.temp('simple-usernames-all.txt'), self.base('src/bits/extra-basic.txt')),
                self.left(self.temp('simple-usernames-all.txt'), self.base('src/bits/numbers-extended.txt')),
                self.right(self.temp('hax0r-usernames-all.txt'), self.base('src/bits/extra-basic.txt')),
                self.right(self.temp('extra-basic+simple-usernames-all.txt'), self.base('src/bits/months.txt')),
                self.right(self.temp('extra-basic+simple-usernames-all.txt'), self.base('src/bits/years-current.txt')),
                self.right(self.temp('extra-basic+simple-usernames-all.txt'), self.base('src/bits/years-all.txt')),
                self.right(self.temp('simple-usernames-all+extra-basic.txt'), self.base('src/bits/years-current.txt')),
                self.right(self.temp('simple-usernames-all+separators.txt'), self.base('src/bits/months.txt')),
                self.right(self.temp('simple-usernames-all+separators.txt'), self.base('src/bits/years-current.txt')),
                self.right(self.temp('simple-usernames-all+years-all.txt'), self.base('src/bits/extra-basic.txt')),
                self.right(self.temp('simple-lang-int-basic.txt'), self.base('src/bits/numbers-basic.txt')),
                self.right(self.temp('simple-lang-int-basic.txt'), self.base('src/bits/years-all.txt')),
                self.right(self.temp('simple-lang-int-extended.txt'), self.base('src/bits/extra-basic.txt')),
                self.right(self.temp('simple-passwords-patterns+separators.txt'), self.base('src/bits/numbers-basic.txt')),
                self.right(self.temp('simple-passwords-patterns+separators.txt'), self.base('src/bits/numbers-extended.txt')),
                self.right(self.temp('simple-passwords-patterns+separators.txt'), self.base('src/bits/years-all.txt')),
                self.right(self.temp('simple-usernames-all.txt'), self.base('src/bits/functional.txt')),
                self.right(self.temp('simple-usernames-all.txt'), self.base('src/bits/numbers-extended.txt')),
                self.right(self.temp('simple-usernames-all+extra-basic.txt'), self.base('src/bits/extra-basic.txt')),
                self.right(self.temp('simple-usernames-all+extra-basic.txt'), self.base('src/bits/years-all.txt')),
                self.right(self.temp('simple-usernames-all+numbers-basic.txt'), self.base('src/bits/extra-basic.txt')),
                self.right(self.temp('simple-usernames-all+separators.txt'), self.base('src/bits/functional.txt')),
                self.right(self.temp('simple-usernames-all+separators.txt'), self.base('src/bits/years-all.txt')),
                self.right(self.temp('simple-usernames-basic+separators+months.txt'), self.base('src/bits/years-current.txt')),
                self.right(self.temp('simple-usernames-basic+years-all.txt'), self.base('src/bits/extra-basic.txt')),
                self.right(self.temp('hax0r-lang-int-basic.txt'), self.base('src/bits/extra-extended.txt')),
                self.rule(self.temp('hax0r-lang-int-basic+extra-extended.txt'), self.base('src/rules/capitalize.rule')),
                self.rule(self.base('src/keywords/lang/int-basic.txt'), self.base('src/rules/overkill.rule')),
                self.temp('complex-lang-all.txt'),
                self.temp('complex-passwords-classics.txt'),
                self.temp('complex-passwords-unique.txt'),
                self.temp('capitalize-tmp-hax0r-lang-int-basic+extra-extended.txt'),
                self.temp('complex-usernames-all.txt'),
                self.temp('hax0r-lang-int-basic.txt'),
                self.temp('repeat-usernames-all.txt'),
                self.temp('simple-lang-all.txt'),
            ),
            compare=self.temp(self.passwords_all)
        )


class BigPasswords(Passwords):

    def process(self):
        # NOTE: Generate here, don't include in merge
        self.right(self.temp('simple-lang-int-basic.txt'), self.base('src/bits/months.txt'))
        self.right(self.temp('simple-lang-int-basic.txt'), self.base('src/bits/years-all.txt'))
        self.right(self.temp('simple-lang-int-basic.txt'), self.base('src/bits/separators.txt'))
        self.right(self.temp('simple-lang-int-basic+months.txt'), self.base('src/bits/separators.txt'))
        self.right(self.temp('simple-lang-int-basic+years-all.txt'), self.base('src/bits/separators.txt'))

        self.merge(
            self.output('wordlists/passwords/7-xxl.txt'),
            (
                self.both(self.temp('repeat-usernames-basic.txt'), self.base('src/bits/extra-all.txt')),
                self.left(self.temp('simple-lang-int-basic.txt'), self.base('src/bits/extra-basic.txt')),
                self.left(self.temp('simple-lang-int-basic.txt'), self.base('src/bits/extra-extended.txt')),
                self.left(self.temp('simple-lang-int-basic.txt'), self.base('src/bits/numbers-basic.txt')),
                self.left(self.temp('simple-lang-int-basic.txt'), self.base('src/bits/numbers-extended.txt')),
                self.left(self.temp('simple-usernames-all+numbers-basic.txt'), self.base('src/bits/extra-basic.txt')),
                self.right(self.temp('hax0r-usernames-all.txt'), self.base('src/bits/extra-extended.txt')),
                self.right(self.temp('numbers-basic+simple-lang-int-basic.txt'), self.base('src/bits/extra-basic.txt')),
                self.right(self.temp('numbers-basic+simple-lang-int-basic.txt'), self.base('src/bits/extra-extended.txt')),
                self.right(self.temp('numbers-basic+simple-usernames-all.txt'), self.base('src/bits/extra-basic.txt')),
                self.right(self.temp('numbers-basic+simple-usernames-all.txt'), self.base('src/bits/extra-extended.txt')),
                self.right(self.temp('numbers-extended+simple-lang-int-basic.txt'), self.base('src/bits/extra-extended.txt')),
                self.right(self.temp('numbers-extended+simple-usernames-all.txt'), self.base('src/bits/extra-basic.txt')),
                self.right(self.temp('numbers-extended+simple-usernames-all.txt'), self.base('src/bits/extra-extended.txt')),
                self.right(self.temp('simple-lang-int-basic.txt'), self.base('src/bits/extra-extended.txt')),
                self.right(self.temp('simple-lang-int-basic.txt'), self.base('src/bits/numbers-extended.txt')),
                self.right(self.temp('simple-lang-int-basic+extra-basic.txt'), self.base('src/bits/months.txt')),
                self.right(self.temp('simple-lang-int-basic+extra-basic.txt'), self.base('src/bits/years-all.txt')),
                self.right(self.temp('simple-lang-int-basic+extra-extended.txt'), self.base('src/bits/months.txt')),
                self.right(self.temp('simple-lang-int-basic+extra-extended.txt'), self.base('src/bits/years-all.txt')),
                self.right(self.temp('simple-lang-int-basic+months.txt'), self.base('src/bits/extra-basic.txt')),
                self.right(self.temp('simple-lang-int-basic+months.txt'), self.base('src/bits/extra-extended.txt')),
                self.right(self.temp('simple-lang-int-basic+months+separators.txt'), self.base('src/bits/years-all.txt')),
                self.right(self.temp('simple-lang-int-basic+numbers-basic.txt'), self.base('src/bits/extra-basic.txt')),
                self.right(self.temp('simple-lang-int-basic+numbers-basic.txt'), self.base('src/bits/extra-extended.txt')),
                self.right(self.temp('simple-lang-int-basic+numbers-extended.txt'), self.base('src/bits/extra-basic.txt')),
                self.right(self.temp('simple-lang-int-basic+numbers-extended.txt'), self.base('src/bits/extra-extended.txt')),
                self.right(self.temp('simple-lang-int-basic+separators.txt'), self.base('src/bits/functional.txt')),
                self.right(self.temp('simple-lang-int-basic+separators.txt'), self.base('src/bits/months.txt')),
                self.right(self.temp('simple-lang-int-basic+separators.txt'), self.base('src/bits/years-all.txt')),
                self.right(self.temp('simple-lang-int-basic+separators+months.txt'), self.base('src/bits/years-all.txt')),
                self.right(self.temp('simple-lang-int-basic+separators+years-all.txt'), self.base('src/bits/months.txt')),
                self.right(self.temp('simple-lang-int-basic+years-all.txt'), self.base('src/bits/extra-basic.txt')),
                self.right(self.temp('simple-lang-int-basic+years-all.txt'), self.base('src/bits/months.txt')),
                self.right(self.temp('simple-lang-int-basic+years-all+separators.txt'), self.base('src/bits/months.txt')),
                self.right(self.temp('simple-usernames-all+numbers-basic.txt'), self.base('src/bits/extra-extended.txt')),
                self.right(self.temp('simple-usernames-all+numbers-extended.txt'), self.base('src/bits/extra-basic.txt')),
                self.right(self.temp('simple-usernames-all+numbers-extended.txt'), self.base('src/bits/extra-extended.txt')),
                self.right(self.temp('simple-usernames-all+separators.txt'), self.base('src/bits/extra-basic.txt')),
                self.right(self.temp('simple-usernames-all+separators+months.txt'), self.base('src/bits/separators.txt')),
                self.right(self.temp('simple-usernames-all+separators+months.txt'), self.base('src/bits/years-all.txt')),
                self.right(self.temp('simple-usernames-all+separators+months+separators.txt'), self.base('src/bits/years-all.txt')),
                self.right(self.temp('hax0r-lang-int-extended.txt'), self.base('src/bits/extra-basic.txt')),
                self.right(self.temp('hax0r-lang-int-extended.txt'), self.base('src/bits/extra-extended.txt')),
                self.rule(self.temp('hax0r-lang-int-extended.txt'), self.base('src/rules/capitalize.rule')),
                self.rule(self.temp('hax0r-usernames-all+extra-basic.txt'), self.base('src/rules/complex.rule')),
                self.rule(self.temp('hax0r-usernames-all+extra-extended.txt'), self.base('src/rules/complex.rule')),
                self.rule(self.temp('hax0r-lang-int-extended+extra-basic.txt'), self.base('src/rules/capitalize.rule')),
                self.rule(self.temp('hax0r-lang-int-extended+extra-extended.txt'), self.base('src/rules/capitalize.rule')),
                self.rule(self.base('src/keywords/lang/int-extended.txt'), self.base('src/rules/overkill.rule')),
                self.rule(self.rule(self.base('wordlists/usernames/all.txt'), self.base('src/rules/repeat.rule')), self.base('src/rules/both.rule')),
                self.temp('both-tmp-repeat-usernames-basic.txt'),
                self.temp('both-lang-int-basic.txt'),
                self.temp('both-lang-int-extended.txt'),
                self.temp('hax0r-lang-int-basic.txt'),
                self.temp('hax0r-lang-int-extended.txt'),
                self.temp('capitalize-tmp-hax0r-lang-int-extended.txt'),
                self.temp('capitalize-tmp-hax0r-lang-int-extended+extra-basic.txt'),
                self.temp('capitalize-tmp-hax0r-lang-int-extended+extra-extended.txt'),
            ),
            compare=self.temp(self.passwords_all)
        )


class CustomPasswords(Passwords):

    wordlists = (
        'src/keywords/custom.txt',
    )
    rules = (
        'src/rules/both.rule',
        'src/rules/complex.rule',
        'src/rules/hax0r.rule',
        'src/rules/repeat.rule',
        'src/rules/simple.rule',
        'src/rules/overkill.rule',
    )

    def process(self):
        self.merge(
            self.output('wordlists/passwords/custom.txt'),
            (
                self.both(self.temp('repeat-keywords-custom.txt'), self.base('src/bits/extra-all.txt')),
                self.left(self.temp('hax0r-keywords-custom.txt'), self.base('src/bits/extra-all.txt')),
                self.left(self.temp('hax0r-keywords-custom.txt'), self.base('src/bits/months.txt')),
                self.left(self.temp('hax0r-keywords-custom.txt'), self.base('src/bits/numbers-all.txt')),
                self.left(self.temp('hax0r-keywords-custom.txt'), self.base('src/bits/separators.txt')),
                self.left(self.temp('hax0r-keywords-custom.txt'), self.base('src/bits/years-current.txt')),
                self.left(self.temp('repeat-keywords-custom.txt'), self.base('src/bits/extra-all.txt')),
                self.left(self.temp('repeat-keywords-custom.txt'), self.base('src/bits/months.txt')),
                self.left(self.temp('repeat-keywords-custom.txt'), self.base('src/bits/numbers-all.txt')),
                self.left(self.temp('repeat-keywords-custom.txt'), self.base('src/bits/separators.txt')),
                self.left(self.temp('repeat-keywords-custom.txt'), self.base('src/bits/years-current.txt')),
                self.left(self.temp('separators+hax0r-keywords-custom.txt'), self.base('src/bits/functional.txt')),
                self.left(self.temp('separators+hax0r-keywords-custom.txt'), self.base('src/bits/months.txt')),
                self.left(self.temp('separators+hax0r-keywords-custom.txt'), self.base('src/bits/years-current.txt')),
                self.left(self.temp('separators+repeat-keywords-custom.txt'), self.base('src/bits/functional.txt')),
                self.left(self.temp('separators+repeat-keywords-custom.txt'), self.base('src/bits/months.txt')),
                self.left(self.temp('separators+repeat-keywords-custom.txt'), self.base('src/bits/years-current.txt')),
                self.left(self.temp('separators+simple-keywords-custom.txt'), self.base('src/bits/functional.txt')),
                self.left(self.temp('separators+simple-keywords-custom.txt'), self.base('src/bits/months.txt')),
                self.left(self.temp('separators+simple-keywords-custom.txt'), self.base('src/bits/years-current.txt')),
                self.left(self.temp('simple-keywords-custom+numbers-all.txt'), self.base('src/bits/extra-all.txt')),
                self.left(self.temp('simple-keywords-custom.txt'), self.base('src/bits/extra-all.txt')),
                self.left(self.temp('simple-keywords-custom.txt'), self.base('src/bits/functional.txt')),
                self.left(self.temp('simple-keywords-custom.txt'), self.base('src/bits/months.txt')),
                self.left(self.temp('simple-keywords-custom.txt'), self.base('src/bits/numbers-all.txt')),
                self.left(self.temp('simple-keywords-custom.txt'), self.base('src/bits/separators.txt')),
                self.left(self.temp('simple-keywords-custom.txt'), self.base('src/bits/years-current.txt')),
                self.left(self.temp('years-current+hax0r-keywords-custom.txt'), self.base('src/bits/extra-all.txt')),
                self.left(self.temp('years-current+hax0r-keywords-custom.txt'), self.base('src/bits/months.txt')),
                self.left(self.temp('years-current+hax0r-keywords-custom.txt'), self.base('src/bits/separators.txt')),
                self.left(self.temp('years-current+repeat-keywords-custom.txt'), self.base('src/bits/extra-all.txt')),
                self.left(self.temp('years-current+repeat-keywords-custom.txt'), self.base('src/bits/months.txt')),
                self.left(self.temp('years-current+repeat-keywords-custom.txt'), self.base('src/bits/separators.txt')),
                self.left(self.temp('years-current+separators+hax0r-keywords-custom.txt'), self.base('src/bits/months.txt')),
                self.left(self.temp('years-current+separators+repeat-keywords-custom.txt'), self.base('src/bits/months.txt')),
                self.left(self.temp('years-current+separators+simple-keywords-custom.txt'), self.base('src/bits/months.txt')),
                self.left(self.temp('years-current+simple-keywords-custom.txt'), self.base('src/bits/extra-all.txt')),
                self.left(self.temp('years-current+simple-keywords-custom.txt'), self.base('src/bits/months.txt')),
                self.left(self.temp('years-current+simple-keywords-custom.txt'), self.base('src/bits/separators.txt')),
                self.right(self.temp('extra-all+hax0r-keywords-custom.txt'), self.base('src/bits/months.txt')),
                self.right(self.temp('extra-all+hax0r-keywords-custom.txt'), self.base('src/bits/years-current.txt')),
                self.right(self.temp('extra-all+repeat-keywords-custom.txt'), self.base('src/bits/months.txt')),
                self.right(self.temp('extra-all+repeat-keywords-custom.txt'), self.base('src/bits/years-current.txt')),
                self.right(self.temp('extra-all+simple-keywords-custom.txt'), self.base('src/bits/months.txt')),
                self.right(self.temp('extra-all+simple-keywords-custom.txt'), self.base('src/bits/years-all.txt')),
                self.right(self.temp('extra-all+simple-keywords-custom.txt'), self.base('src/bits/years-current.txt')),
                self.right(self.temp('hax0r-keywords-custom+extra-all.txt'), self.base('src/bits/months.txt')),
                self.right(self.temp('hax0r-keywords-custom+extra-all.txt'), self.base('src/bits/years-current.txt')),
                self.right(self.temp('hax0r-keywords-custom+months+separators.txt'), self.base('src/bits/years-current.txt')),
                self.right(self.temp('hax0r-keywords-custom+months.txt'), self.base('src/bits/extra-all.txt')),
                self.right(self.temp('hax0r-keywords-custom+months.txt'), self.base('src/bits/separators.txt')),
                self.right(self.temp('hax0r-keywords-custom+numbers-all.txt'), self.base('src/bits/extra-all.txt')),
                self.right(self.temp('hax0r-keywords-custom+separators+months.txt'), self.base('src/bits/years-current.txt')),
                self.right(self.temp('hax0r-keywords-custom+separators+years-current.txt'), self.base('src/bits/months.txt')),
                self.right(self.temp('hax0r-keywords-custom+separators.txt'), self.base('src/bits/functional.txt')),
                self.right(self.temp('hax0r-keywords-custom+separators.txt'), self.base('src/bits/months.txt')),
                self.right(self.temp('hax0r-keywords-custom+separators.txt'), self.base('src/bits/years-current.txt')),
                self.right(self.temp('hax0r-keywords-custom+years-current+separators.txt'), self.base('src/bits/months.txt')),
                self.right(self.temp('hax0r-keywords-custom+years-current.txt'), self.base('src/bits/extra-all.txt')),
                self.right(self.temp('hax0r-keywords-custom+years-current.txt'), self.base('src/bits/months.txt')),
                self.right(self.temp('hax0r-keywords-custom+years-current.txt'), self.base('src/bits/separators.txt')),
                self.right(self.temp('hax0r-keywords-custom.txt'), self.base('src/bits/extra-all.txt')),
                self.right(self.temp('hax0r-keywords-custom.txt'), self.base('src/bits/months.txt')),
                self.right(self.temp('hax0r-keywords-custom.txt'), self.base('src/bits/numbers-all.txt')),
                self.right(self.temp('hax0r-keywords-custom.txt'), self.base('src/bits/separators.txt')),
                self.right(self.temp('hax0r-keywords-custom.txt'), self.base('src/bits/years-current.txt')),
                self.right(self.temp('months+hax0r-keywords-custom.txt'), self.base('src/bits/extra-all.txt')),
                self.right(self.temp('months+repeat-keywords-custom.txt'), self.base('src/bits/extra-all.txt')),
                self.right(self.temp('months+separators+simple-keywords-custom.txt'), self.base('src/bits/extra-all.txt')),
                self.right(self.temp('months+simple-keywords-custom.txt'), self.base('src/bits/extra-all.txt')),
                self.right(self.temp('numbers-all+hax0r-keywords-custom.txt'), self.base('src/bits/extra-all.txt')),
                self.right(self.temp('numbers-all+repeat-keywords-custom.txt'), self.base('src/bits/extra-all.txt')),
                self.right(self.temp('numbers-all+simple-keywords-custom.txt'), self.base('src/bits/extra-all.txt')),
                self.right(self.temp('repeat-keywords-custom+numbers-all.txt'), self.base('src/bits/extra-all.txt')),
                self.right(self.temp('repeat-keywords-custom.txt'), self.base('src/bits/extra-all.txt')),
                self.right(self.temp('repeat-keywords-custom.txt'), self.base('src/bits/numbers-all.txt')),
                self.right(self.temp('simple-keywords-custom+extra-all.txt'), self.base('src/bits/extra-all.txt')),
                self.right(self.temp('simple-keywords-custom+extra-all.txt'), self.base('src/bits/months.txt')),
                self.right(self.temp('simple-keywords-custom+extra-all.txt'), self.base('src/bits/years-all.txt')),
                self.right(self.temp('simple-keywords-custom+extra-all.txt'), self.base('src/bits/years-current.txt')),
                self.right(self.temp('simple-keywords-custom+months+separators.txt'), self.base('src/bits/years-all.txt')),
                self.right(self.temp('simple-keywords-custom+months+separators.txt'), self.base('src/bits/years-current.txt')),
                self.right(self.temp('simple-keywords-custom+months.txt'), self.base('src/bits/extra-all.txt')),
                self.right(self.temp('simple-keywords-custom+months.txt'), self.base('src/bits/separators.txt')),
                self.right(self.temp('simple-keywords-custom+numbers-all.txt'), self.base('src/bits/extra-all.txt')),
                self.right(self.temp('simple-keywords-custom+separators+months+separators.txt'), self.base('src/bits/years-all.txt')),
                self.right(self.temp('simple-keywords-custom+separators+months.txt'), self.base('src/bits/separators.txt')),
                self.right(self.temp('simple-keywords-custom+separators+months.txt'), self.base('src/bits/years-all.txt')),
                self.right(self.temp('simple-keywords-custom+separators+months.txt'), self.base('src/bits/years-current.txt')),
                self.right(self.temp('simple-keywords-custom+separators+years-all.txt'), self.base('src/bits/months.txt')),
                self.right(self.temp('simple-keywords-custom+separators+years-current.txt'), self.base('src/bits/months.txt')),
                self.right(self.temp('simple-keywords-custom+separators.txt'), self.base('src/bits/extra-all.txt')),
                self.right(self.temp('simple-keywords-custom+separators.txt'), self.base('src/bits/functional.txt')),
                self.right(self.temp('simple-keywords-custom+separators.txt'), self.base('src/bits/months.txt')),
                self.right(self.temp('simple-keywords-custom+separators.txt'), self.base('src/bits/numbers-all.txt')),
                self.right(self.temp('simple-keywords-custom+separators.txt'), self.base('src/bits/years-all.txt')),
                self.right(self.temp('simple-keywords-custom+separators.txt'), self.base('src/bits/years-current.txt')),
                self.right(self.temp('simple-keywords-custom+years-all+separators.txt'), self.base('src/bits/months.txt')),
                self.right(self.temp('simple-keywords-custom+years-all.txt'), self.base('src/bits/extra-all.txt')),
                self.right(self.temp('simple-keywords-custom+years-all.txt'), self.base('src/bits/months.txt')),
                self.right(self.temp('simple-keywords-custom+years-current+separators.txt'), self.base('src/bits/months.txt')),
                self.right(self.temp('simple-keywords-custom+years-current.txt'), self.base('src/bits/extra-all.txt')),
                self.right(self.temp('simple-keywords-custom+years-current.txt'), self.base('src/bits/months.txt')),
                self.right(self.temp('simple-keywords-custom+years-current.txt'), self.base('src/bits/separators.txt')),
                self.right(self.temp('simple-keywords-custom.txt'), self.base('src/bits/extra-all.txt')),
                self.right(self.temp('simple-keywords-custom.txt'), self.base('src/bits/extra-top.txt')),
                self.right(self.temp('simple-keywords-custom.txt'), self.base('src/bits/functional.txt')),
                self.right(self.temp('simple-keywords-custom.txt'), self.base('src/bits/months.txt')),
                self.right(self.temp('simple-keywords-custom.txt'), self.base('src/bits/numbers-all.txt')),
                self.right(self.temp('simple-keywords-custom.txt'), self.base('src/bits/separators.txt')),
                self.right(self.temp('simple-keywords-custom.txt'), self.base('src/bits/years-all.txt')),
                self.right(self.temp('simple-keywords-custom.txt'), self.base('src/bits/years-current.txt')),
                self.right(self.temp('years-current+separators+hax0r-keywords-custom.txt'), self.base('src/bits/extra-all.txt')),
                self.right(self.temp('years-current+separators+repeat-keywords-custom.txt'), self.base('src/bits/extra-all.txt')),
                self.right(self.temp('years-current+separators+simple-keywords-custom.txt'), self.base('src/bits/extra-all.txt')),
                self.rule(self.temp('extra-all+hax0r-keywords-custom.txt'), self.base('src/rules/complex.rule')),
                self.rule(self.temp('extra-all+repeat-keywords-custom.txt'), self.base('src/rules/complex.rule')),
                self.rule(self.temp('extra-all+simple-keywords-custom.txt'), self.base('src/rules/complex.rule')),
                self.rule(self.temp('hax0r-keywords-custom+extra-all.txt'), self.base('src/rules/capitalize.rule')),
                self.rule(self.temp('hax0r-keywords-custom+extra-all.txt'), self.base('src/rules/complex.rule')),
                self.rule(self.temp('hax0r-keywords-custom+numbers-all.txt'), self.base('src/rules/complex.rule')),
                self.rule(self.temp('hax0r-keywords-custom.txt'), self.base('src/rules/capitalize.rule')),
                self.rule(self.temp('numbers-all+hax0r-keywords-custom.txt'), self.base('src/rules/complex.rule')),
                self.rule(self.temp('numbers-all+repeat-keywords-custom.txt'), self.base('src/rules/complex.rule')),
                self.rule(self.temp('numbers-all+simple-keywords-custom.txt'), self.base('src/rules/complex.rule')),
                self.rule(self.temp('repeat-keywords-custom+extra-all.txt'), self.base('src/rules/complex.rule')),
                self.rule(self.temp('repeat-keywords-custom+numbers-all.txt'), self.base('src/rules/complex.rule')),
                self.rule(self.temp('simple-keywords-custom+numbers-all.txt'), self.base('src/rules/complex.rule')),
                self.rule(self.temp('simple-keywords-custom.txt'), self.base('src/rules/both.rule')),
                self.rule(self.temp('simple-keywords-custom.txt'), self.base('src/rules/repeat.rule')),
                self.rule(self.temp('repeat-tmp-simple-keywords-custom.txt'), self.base('src/rules/both.rule')),
                self.temp('both-tmp-repeat-tmp-simple-keywords-custom.txt'),
                self.temp('both-tmp-simple-keywords-custom.txt'),
                self.temp('capitalize-tmp-hax0r-keywords-custom+extra-all.txt'),
                self.temp('capitalize-tmp-hax0r-keywords-custom.txt'),
                self.temp('complex-keywords-custom.txt'),
                self.temp('hax0r-keywords-custom.txt'),
                self.temp('overkill-keywords-custom.txt'),
                self.temp('repeat-keywords-custom.txt'),
                self.temp('repeat-tmp-simple-keywords-custom.txt'),
                self.temp('simple-keywords-custom.txt'),
            )
        )


class OrganizationNamePasswords(Passwords):

    wordlists = (
        'src/keywords/custom.txt',
    )
    rules = (
        'src/rules/simple.rule',
    )

    def process(self):
        self.merge(
            self.output('wordlists/passwords/custom.txt'),
            (
                self.left(self.temp('simple-keywords-custom.txt'), self.base('src/bits/extra-basic.txt')),
                self.left(self.temp('simple-keywords-custom.txt'), self.base('src/bits/functional.txt')),
                self.left(self.temp('simple-keywords-custom.txt'), self.base('src/bits/months.txt')),
                self.left(self.temp('simple-keywords-custom.txt'), self.base('src/bits/numbers-basic.txt')),
                self.left(self.temp('simple-keywords-custom.txt'), self.base('src/bits/years-current.txt')),
                self.right(self.temp('simple-keywords-custom.txt'), self.base('src/bits/extra-basic.txt')),
                self.right(self.temp('simple-keywords-custom.txt'), self.base('src/bits/functional.txt')),
                self.right(self.temp('simple-keywords-custom.txt'), self.base('src/bits/months.txt')),
                self.right(self.temp('simple-keywords-custom.txt'), self.base('src/bits/numbers-basic.txt')),
                self.right(self.temp('simple-keywords-custom.txt'), self.base('src/bits/years-current.txt')),
                self.temp('simple-keywords-custom.txt'),
            )
        )


class OrganizationKeywordsPasswords(Passwords):

    wordlists = (
        'src/keywords/custom.txt',
    )
    rules = (
        'src/rules/simple.rule',
    )

    def process(self):
        self.merge(
            self.output('wordlists/passwords/custom.txt'),
            (
                self.left(self.temp('simple-keywords-custom.txt'), self.base('src/bits/extra-basic.txt')),
                self.left(self.temp('simple-keywords-custom.txt'), self.base('src/bits/numbers-basic.txt')),
                self.left(self.temp('simple-keywords-custom.txt'), self.base('src/bits/years-current.txt')),
                self.right(self.temp('simple-keywords-custom.txt'), self.base('src/bits/extra-basic.txt')),
                self.right(self.temp('simple-keywords-custom.txt'), self.base('src/bits/numbers-basic.txt')),
                self.right(self.temp('simple-keywords-custom.txt'), self.base('src/bits/years-current.txt')),
                self.temp('simple-keywords-custom.txt'),
            )
        )


class MergeAll(Combinator):

    def process(self):
        self.concat(
            self.output('wordlists/passwords/all.txt'),
            (
                self.base('wordlists/passwords/1-xxs.txt'),
                self.base('wordlists/passwords/2-xs.txt'),
                self.base('wordlists/passwords/3-s.txt'),
                self.base('wordlists/passwords/4-m.txt'),
                self.base('wordlists/passwords/5-l.txt'),
                self.base('wordlists/passwords/6-xl.txt'),
                self.base('wordlists/passwords/7-xxl.txt'),
            )
        )
