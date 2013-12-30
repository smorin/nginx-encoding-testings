

ba = bytearray();

for x in range(0, 256):
    print "We're on time %d" % (x)
    ba.append(x)

# Open a file
fo = open("python0to256bin.data", "wb")
fo.write(ba);

# Close opend file
fo.close()



# open FILE, ">:raw", 'perl0to256bin.data'  or die "Couldn't open file!";
# 
# for(my $i = 0; $i<256; $i++) {
#     my $byte = pack('C',$i);
#     print FILE $byte;
# }
# 
# close FILE;
