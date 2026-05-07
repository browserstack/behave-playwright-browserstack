behave-playwright-browserstack (BrowserStack SDK + Playwright)
===============================================================

This repo shows how to run [behave](https://behave.readthedocs.io/) tests on BrowserStack using the [BrowserStack Python SDK](https://pypi.org/project/browserstack-sdk/) and [Playwright Python](https://playwright.dev/python/). The SDK handles capability injection, BrowserStack routing for Playwright launches, parallelization, and BrowserStack Local for you — you describe platforms once in `browserstack.yml` and run the test command unchanged.

## Setup
* Clone this repo
* Install dependencies (creates the BrowserStack SDK CLI on `PATH` and downloads Playwright Chromium)
  ```sh
  pip install -r requirements.txt
  playwright install chromium
  ```
* Set `BROWSERSTACK_USERNAME` and `BROWSERSTACK_ACCESS_KEY` as environment variables, or replace `userName` and `accessKey` directly in `browserstack.yml` with your [BrowserStack Username and Access Key](https://www.browserstack.com/accounts/settings). Env vars take precedence.

### Running your tests
Run the sample in parallel across the 3 Playwright browser engines (chromium / firefox / webkit) declared in `browserstack.yml`:

```sh
browserstack-sdk behave features/sample.feature
```

Understand how many parallel sessions you need by using our [Parallel Test Calculator](https://www.browserstack.com/automate/parallel-calculator?ref=github).

Alternatively the variables can be set in the environment using env or your CI framework (like GitHub Actions or Jenkins). See `.github/workflows/build.yml` for a GitHub Actions example — it runs on `workflow_dispatch` (manual trigger) with a commit SHA input and posts a status check back to that commit.

### Testing a private host (BrowserStack Local)
If your app lives on `localhost`, a staging host, or behind a firewall, set `browserstackLocal: true` in `browserstack.yml` and rerun the same command. The SDK starts and stops the BrowserStack Local tunnel for you — no manual binary download or lifecycle management. Then point your scenarios at `http://bs-local.com:<port>/` (a hostname BrowserStack Local resolves to your machine) instead of a public URL.

### How the SDK changes things
- **One `browserstack.yml`** declares platforms; the SDK picks them up automatically.
- **The SDK runs platforms in parallel for you** — no hand-rolled parallel runner; the SDK forks one behave run per `(platform × parallelsPerPlatform)` cell.
- **The SDK monkeypatches Playwright's browser launches** — the test code calls `chromium.launch()` and the SDK transparently routes the launch to the per-platform browser configured in `browserstack.yml` (chromium, firefox, or webkit). No `chromium.connect(wss_url)` plumbing is needed in customer code.
- **The CLI is `browserstack-sdk behave …`** — wraps `behave` and injects the SDK at runtime.

### Repo layout
```
.
├── browserstack.yml           # SDK config: credentials, 3 parallel platforms, Local toggle, reporting
├── requirements.txt
└── features/
    ├── sample.feature         # bstackdemo add-to-cart scenario
    ├── environment.py         # behave hooks: launch browser, hand to context.page
    └── steps/
        └── sample_steps.py
```

### Further Reading
- [behave](https://behave.readthedocs.io/)
- [Playwright Python](https://playwright.dev/python/)
- [BrowserStack documentation for Playwright](https://www.browserstack.com/docs/automate/playwright)
- [BrowserStack Python SDK on PyPI](https://pypi.org/project/browserstack-sdk/)

Happy Testing!
