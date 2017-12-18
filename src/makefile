.PHONY: all clean app so

all: clean so app

objs=exponentiation.o util.o math.o
sobjs=util.so math.so

app: $(objs) $(sobjs)
	cd ../bin && cc $^ -o $@

so: $(sobjs)
#	cc -shared -fPIC $^ -o ../bin/$@

.c.o:
	cc -c $< -o ../bin/$@

%.so:$(objs)
	cd ../bin && cc -shared -fPIC $^ -o $@

clean:
	-rm *.o *.so
