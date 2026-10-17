# daehakim-waterlab.github.io

Homepage of Daeha Kim's hydrology and water resources group, Department of Civil Engineering, Jeonbuk National University: <https://daehakim-waterlab.github.io>

Built with the [al-folio](https://github.com/alshedivat/al-folio) Jekyll template (v1.x). `.github/workflows/deploy.yml` builds the site on every push to `main` and publishes it to the `gh-pages` branch.

## Where things are

| Menu | URL | Edit |
| --- | --- | --- |
| Home | `/` | `_pages/about.md`; news items in `_news/` |
| Research | `/research/` | `_pages/research.md` |
| People | `/people/` | `_pages/people.md`; members and alumni in `_data/people.yml` |
| Publications ▾ | `/publications/…` | `_bibliography/papers.bib`; pages in `_pages/publications/` |
| Projects | `/projects/` | `_data/projects.yml` |
| Teaching ▾ | `/teaching/…` | one file per course in `_teachings/` |
| Blog (hidden) | `/blog/` | posts in `_posts/`; menu switch in `_pages/blog.md` |
| Join us | `/join/` | `_pages/join.md` |

Site-wide settings (name, footer with contact details, feature flags) are in `_config.yml`; contact links are in `_data/socials.yml`.

## Common tasks

**Add a news item.** Create `_news/YYYY-MM-DD-short-name.md`:

```markdown
---
layout: post
date: 2026-11-01
inline: true
related_posts: false
---

New paper in _Journal Name_: one-sentence summary. [DOI](https://doi.org/...)
```

The five most recent items appear on Home; all of them are at `/news/`.

**Add a publication.** Add an entry to `_bibliography/papers.bib`. The entry type decides the sub-page: `@article` (journal articles), `@incollection` (book chapters), `@techreport` (technical reports). Conference presentations are not listed on the site. Copy a neighbouring entry so the `abbr`, `doi`, and `additional_info` fields stay consistent. Only list papers that are published or in press; for an in-press paper add `note = {In press}`.

**Add a lab member or alumnus.** After the person agrees to be listed, add them to `_data/people.yml`. The Lab members and Alumni sections appear automatically once they have an entry.

**Link an online textbook.** In the course file in `_teachings/`, uncomment the `textbook:` line and set the URL. "Online textbook — coming soon" is replaced by the link on the course page and on the Teaching page.

**Publish the first blog post.** Add `_posts/YYYY-MM-DD-title.md` with `categories: paper-highlights` or `categories: notes`, then set `nav: true` in `_pages/blog.md` and `latest_posts.enabled: true` in `_pages/about.md`.

**Add the PI photo.** Save it as `assets/img/prof_pic.jpg` and uncomment `image: prof_pic.jpg` in `_pages/about.md`.

## Building locally

Requires Ruby 3.3+ and Node 20 (CI uses Ruby 3.3.5 and Node 20).

```bash
bundle install
npm ci
bundle exec jekyll serve
```

The site is then at <http://localhost:4000/>. There is no `baseurl`: this is a user site served from the domain root.

## Content rules

See [CLAUDE.md](CLAUDE.md#content-rules).
