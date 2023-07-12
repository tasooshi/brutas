# Changelog

The repository had grown to the point it was too slow to pull because of no longer needed artifacts, so I decided to "squash" everything and erase the history. The old logs will be kept here though. This may happen some day in the future, again.

**2023/07/11**
```
    Added new "objects" lists for enumerating HTTP parameters
```

**2023/01/29**
```
    New patterns, extra custom classes
```

**2023/01/20**
```
    Fixed order
```

**2023/01/19**
```
    Removed redundant rules from CustomPasswords and extended combinations
```

**2023/01/17**
```
    Updated hosted files
```

**2023/01/15**
```
    Updated docs, more building blocks, current year, changed priorities in build process, shorter build time, new rules, patterns and common passwords, more changes in the wordz package
```

**2023/01/12**
```
    Updated docs, allow custom output directory in helper scripts
```

**2023/01/09**
```
    First batch of updated dictionaries
```

**2022/09/01**
```
    Added new extensions to the BigQuery set
```

**2022/08/01**
```
    Extended basic list (added some popular languages keywords to make it more international), verified against Google Search API, extracted new keyboard patterns, other minor improvements
```

**2022/07/29**
```
    A few new "standards", extra rules and bits, cleaned up common keywords, reduced number of basic usernames, added new generic-1k list
```

**2022/07/16**
```
    Update README.md
```

**2022/07/14**
```
    Major refactoring, wordlists now in separate directories, helper tools moved to external repo and in pypi with coverage > 90%, simplified building process
```

**2022/06/23**
```
    Rebuilt password lists due to classics update
```

**2022/06/22**
```
    Script for translating wordlists, preparing for i18n
```

**2022/06/21**
```
    A few more classics for Passw0rds
```

**2022/06/15**
```
    Closes #2 Improved handling hashcat binaries
```

**2022/06/11**
```
    Added BigQuery+Github file lists, reorganized README
```

**2022/06/10**
```
    Recompiled lists, ignore case when sorting lists, some refactoring, dedicated class for managing extensions
```

**2022/06/09**
```
    HTTP discovery lists update
```

**2022/06/01**
```
    Improved HTTP discovery lists, revision of the minimal password dict, some extra patterns/tops observed in the wild, cleaned up old dicts
```

**2022/05/28**
```
    Update README.md
```

**2022/05/20**
```
    Added stats
```

**2022/05/10**
```
    Major refactoring
    - Generator classes (hopefully) easier to read & write
    - Generators for HTTP paths/params
    - Improved README
    - Some small optimizations, still a lot of work to do
    - Duplicates are now removed from all previous password lists
    - Dropped `brutas-http-files-*` lists, working on a better approach
    - Standardized sort args, temporarily disabled "compress-program" (duplicates), all cmds now executed in subshell with LC_ALL passed by default
```

**2022/05/09**
```
    Massive update:
    - Renamed closekeys list to patterns
    - Missed a few classic & unique passwords, new "both-sides" rule
    - Several improvements based on research papers
    - Added minimal length by default, new extra list (`extra-most-common.txt`) to support a specific use case,
    - Removing duplicates from all previous sets
    - New sizes for passwords lists, xxl is back
```

**2022/03/16**
```
    Freshies, reworked priorities in extra bits / suffixes
```

**2022/03/14**
```
    Updated README
```

**2022/03/12**
```
    Avoid writing to temp if nothing to compare with, removed unused logic
```

**2022/03/12**
```
    Combination fix...
```

**2022/03/12**
```
    Still a bit of an overkill
```

**2022/03/12**
```
    Paths fix
```

**2022/03/11**
```
    Turned out to be overkill even for a 1TB cache when some extras are modified (eg custom months)
```

**2022/03/07**
```
    Simplified and refactored, improved path handling, removed excessive repeat rule
```

**2022/03/02**
```
    Updated README
```

**2022/03/01**
```
    Build script optimizations, new additions, updated readme, smaller 1-xxs & 2-xs, cleaned up classics and tops, new close keys
```

**2022/02/28**
```
    Parallel sorting improvements, ignore errors when removing non-existing files, new passwords, new language (brutas-lang-no.txt)
```

**2021/12/07**
```
    Recompiled with latest changes
```

**2021/12/07**
```
    New close key combinations, improved typical extensions for HTTP dir enum
```

**2021/11/05**
```
    Regular update: new uniques, extra rules and keywords
```

**2021/09/26**
```
    Refactoring, added new Custom generator for... custom keywords
```

**2021/09/25**
```
    Build with latest changes
    Updated most common usernames
```

**2021/09/25**
```
    New close keys findings
```

**2021/09/06**
```
    Extra bits for generating "complex" passwords, smartphones related passwords,
```

**2021/08/26**
```
    Cleaning up, some small innovations with top/classics
```

**2021/08/26**
```
    New top passwords, extra lists for common files and extensions used in Web applications
```

**2021/07/30**
```
    Added new close keys combinations, unique passwords and common keywords, updates docs
```

**2021/06/14**
```
    Updated download links
    Local configuration
```

**2021/06/10**
```
    Build script fix
```

**2021/06/09**
```
    Latest research, improved rules, new keywords, a small optimization
```

**2021/06/06**
```
    Updated README
```

**2021/06/05**
```
    Ordering fix, cores are back: turns out sort doesn't handle well virtualized envs
```

**2021/06/04**
```
    Reordering lists
    Segfault fix i.a.
```

**2021/06/03**
```
    Almost final...
```

**2021/06/02**
```
    Large dictionary split, cleaning up
    Ignore *.pyc
    Already sorted
    Further build improvements
```

**2021/06/01**
```
    Build script improvements and a little optimization
    Refactored build script
```

**2021/05/31**
```
    Further improvements, added more complex rules for the xxl dictionary, revised keywords, new close keys combinations and bits
```

**2021/05/17**
```
    Massive update: new build script, international keywords, improved and more granular rules etc.
```

**2021/05/11**
```
    New rules, new findings, removed the modest tomcat list
```

**2021/05/02**
```
    New combinations and new rules based on recent leak analysis
```

**2021/04/23**
```
    Improved rules (1st letter case toggle)
```

**2021/04/07**
```
    Updated HTTP params and paths
```

**2021/03/31**
```
    Top passwords update
```

**2021/02/28**
```
    Update as usual, new findings
```

**2021/02/23**
```
    Updated README
    More typical combinations, better distribution
    A few extra combinations and highly opinionated port lists
```

**2021/01/25**
```
    Updated rules and close keys combinations
    Subdomains update
    Updated extensions, paths, most common combinations, a few new rules
```

**2020/11/26**
```
    Updated subdomain lists
    Improved rules, extra close keys and subdomain enum ideas
```

**2020/11/15**
```
    Rule refactoring
```

**2020/11/11**
```
    New lists, refactoring, several updates
```

**2020/11/03**
```
    Fixed some rules logic, others improved, better probability distribution
```

**2020/10/27**
```
    General housekeeping, added other languages, wifi keywords, HTTP params and some new combinations
```

**2020/09/25**
```
    Fresh delivery, improved scripts, 1k list is back again
```

**2020/09/20**
```
    New subdomain and path keywords based on latest scans
```

**2020/09/13**
```
    A quick update
```

**2020/09/12**
```
    New passwords based on leak analysis, some maintenance
    New discoveries and ideas from the latest tests
```

**2020/09/01**
```
    Updated HTTP wordlist, keyboard close combinations, leet speek and extra rules
```

**2020/08/04**
```
    Extended close keys dict, added a few rules, removed redundant ones
```

**2020/07/31**
```
    MASSIVE update, handpicked thousands of lines and changed approach in general so the lists are more effective and easier to maintain
```

**2020/07/24**
```
    Just a regular update
```

**2020/07/23**
```
    Subdomain enum update, username update
```

**2020/07/21**
```
    Updated usernames, build fix
```

**2020/07/20**
```
    Just a regular update and improvements
```

**2020/07/19**
```
    Updated usernames and basic password lists
```

**2020/07/12**
```
    Combined passwords
    Yet another HTTP paths update
    Updated HTTP paths with latest scans
    Updated HTTP paths
```

**2020/07/11**
```
    Updated HTTP paths
```

**2020/07/10**
```
    Usernames update, new lists: extensions and HTTP paths
```

**2020/07/07**
```
    Refreshed usernames
```

**2020/06/26**
```
    Reorganized lists into stages so it's less confusing, added new passwords
```

**2020/05/25**
```
    Updated 3k with some popular electronics brands
```

**2020/05/19**
```
    Massive update, new sets, base dictionaries (3k, 10k) are now mutually exclusive, removed old hackish-style and added one based on custom and simplified rules
```

**2020/04/29**
```
    Yet another update...
    A tiny change leading to a huge outcome
```

**2020/04/28**
```
    New additions, fixed order in 250k list
    These are "top" by definition, no need to clutter
    Some priorities changed, only names having more than one cultural context stay in top 3k, new passwords
```

**2020/04/23**
```
    A small yet essential update
```

**2020/04/20**
```
    Updated docs
    Shorter file names
    Added subdomains lists
    Oh, so you say this machine was set up in 2012...?
    A wee bit of fresh stuff
```

**2020/04/11**
```
    Updated with some fresh leaks and ideas
```

**2020/03/01**
```
    Passwords upgrade, usernames
    Changed purpose of this repository
    Almost 3000 hand-picked passwords based on real life and leaks, including common pop-culture terms: brands, comics, games etc. Some cleaning up
```

**2020/02/20**
```
    Top passwords upgrade, aiming at 1000 best of the best
```

**2020/02/04**
```
    Initial commit
```