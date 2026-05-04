# Makefile for behave + Playwright + BrowserStack SDK sample.
#
# The SDK only reads ./browserstack.yml, so the `single` and `local` targets
# swap in an alternate config from config/ for the duration of the run and
# restore the parallel default afterwards (even on failure).

PARALLEL_CMD := browserstack-sdk behave features/sample.feature
LOCAL_CMD    := browserstack-sdk behave features/local.feature

.PHONY: parallel single local install

# Default: parallel run uses the committed browserstack.yml (3 platforms).
parallel:
	$(PARALLEL_CMD)

# Single-platform run: swap in config/browserstack.single.yml.
single:
	@cp browserstack.yml browserstack.yml.bak; \
	cp config/browserstack.single.yml browserstack.yml; \
	$(PARALLEL_CMD); status=$$?; \
	mv browserstack.yml.bak browserstack.yml; \
	exit $$status

# Local-tunnel run: serve a small HTML page on :45454 and point a localhost
# scenario at it. The SDK starts/stops the BrowserStack Local tunnel because
# the alternate config sets `browserstackLocal: true`.
local:
	@cp browserstack.yml browserstack.yml.bak; \
	cp config/browserstack.local.yml browserstack.yml; \
	python3 -m http.server 45454 --directory features/local-html >/tmp/bspl-local-server.log 2>&1 & \
	server_pid=$$!; \
	sleep 1; \
	$(LOCAL_CMD); status=$$?; \
	kill $$server_pid 2>/dev/null; \
	mv browserstack.yml.bak browserstack.yml; \
	exit $$status

install:
	pip install -r requirements.txt
	playwright install chromium
