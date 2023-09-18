CFLAGS = -Og -g -gdwarf-2 -c -Wall -Wno-unused -std=c++20 \
		 -I/usr/local/include -I$(.CURDIR)/include

LDFLAGS = -L/usr/local/lib

.undef CC
.ifndef CC
CC = clang++
.endif

.SUFFIXES: .cpp .o
.PHONY: clean
.PATH: $(.CURDIR)/src
.PATH: $(.CURDIR)/test

# .OBJDIR tries to chdir(2) into MAKEOBJDIR only at startup. If it's created
# later, it doesn't chdir(2) to .OBJDIR even if the macro is forced to a value.
# In other words, if obj/ already exists, it will have one behaviour, but if we
# try to create at runtime (in .BEGIN for instance), the behaviour changes. For
# now, assume obj/ should exist.
#MAKEOBJDIR = obj
#.OBJDIR = $(.CURDIR)/$(MAKEOBJDIR)

#.BEGIN:
#	mkdir -p $(.CURDIR)/$(MAKEOBJDIR)

.cpp.o:
	$(CC) $(CFLAGS) $<

main: main.o pb.o
	$(CC) $(LDFLAGS) -o $@ main.o pb.o

test: test.o pb.o
	$(CC) $(LDFLAGS) -o $@ -lgtest_main -lgtest test.o pb.o

clean:
		rm -f $(.OBJDIR)/*.o $(.OBJDIR)/main
