.PHONY: all

all: clean app

app:
	cd src && $(MAKE) $@
clean:
	-rm bin/* && cd src && $(MAKE) $@
