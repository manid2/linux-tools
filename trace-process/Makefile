CC=gcc
RM=rm -f

CFLAGS=
LDFLAGS=

SRCS=$(wildcard *.c)
OBJS=$(SRCS:.c=.o)
BINS=$(basename $(SRCS))

all: $(BINS)

.PHONY: clean help

help:
	@echo "make"

clean:
	$(RM) $(OBJS)
	$(RM) $(BINS)

# TODO:
# * Add debug, stripped and profiling targets.
# * Add targets to generate trace files.
# * Put all generated files into build directory

$(BINS): %: %.o
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ $<
