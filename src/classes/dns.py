from wordz import (
    Combinator,
    logs,
)


class Subdomains(Combinator):

    def process(self):
        logs.logger.info('Generating subdomains')
        self.sort(self.base('src/keywords/dns/basic.txt'), self.temp('subdomains-basic.txt'))
        self.sort(self.base('src/keywords/dns/extended.txt'), self.temp('subdomains-extended.txt'))
        self.copy(self.temp('subdomains-basic.txt'), self.base('wordlists/dns/basic.txt'))
        self.compare(self.temp('subdomains-basic.txt'), self.temp('subdomains-extended.txt'), self.base('wordlists/dns/basic.txt'), append=True)
        self.copy(self.base('wordlists/dns/basic.txt'), self.base('wordlists/dns/extended.txt'))
        self.run_shell(f'{self.bin_hashcat} --stdout -r {self.base_dir}/src/rules/subdomains.rule {self.temp_dir}/subdomains-basic.txt >> {self.base_dir}/wordlists/dns/extended.txt')
