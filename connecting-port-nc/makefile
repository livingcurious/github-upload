.PHONY: main
main: flag

FLAG_PREFIX := $(shell echo $(FLAG_FORMAT) | sed 's/^\([a-zA-Z0-9]*\).*/\1/')
FLAG := "$(FLAG_PREFIX)$(shell nc mercury.picoctf.net 35652)"

#FLAG := $(shell nc mercury.picoctf.net 35652)
artifacts.tar.gz: flag
	tar czvf $@ $^

flag:
	@echo "$(FLAG)" > flag

metadata.json:
	@echo "Creating the metadata file..."
	@echo "{\"flag\":\"$(FLAG)\"}" > metadata.json


clean:
	rm -f flag