.PHONY: all clean app

all: clean app
objs=exponentiation.o

app: $(objs)
	cd ../bin && cc $< -o $@

.c.o:
	cc -c $< -o ../bin/$@
#	cc -c $<
clean:
	-rm *.o
