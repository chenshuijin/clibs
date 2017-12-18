.PHONY: all app clean test so

app:
	cd src && $(MAKE) $@
so:
	cd src && $(MAKE) $@

test:
	@echo '********begin run python test*******'
#	./test/*.py
	cd ./test && ./test.sh
	@echo '********end run python test*******'

clean:
	-rm bin/* && cd src && $(MAKE) $@
