
open FILE, ">:raw", 'perl0to256bin.data'  or die "Couldn't open file!";

for(my $i = 0; $i<256; $i++) {
	my $byte = pack('C',$i);
	print FILE $byte;
}

close FILE;
