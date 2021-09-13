.PHONY: main
main: flag
FLAG_PREFIX := $(shell echo $(FLAG_FORMAT) | sed 's/^\([a-zA-Z0-9]*\).*/\1/')
FLAG := "$(FLAG_PREFIX)$(shell python3 convertme.py 10)"
#FLAG := $(shell python3 convertme.py 10)
artifacts.tar.gz: flag
	tar czvf $@ $^

flag:
	@echo "$(FLAG)" > flag

metadata.json:
	@echo "Creating the metadata file..."
	@echo "{\"flag\":\"$(FLAG)\"}" > metadata.json


clean:
	rm -f flag