#!/usr/bin/perl

use strict;
use warnings;

# Iterate through each line from standard input
while (<STDIN>) {
    # Try to match content within <loc> tags using regular expression
    if (/<loc>(.*?)<\/loc>/) {
        # Print the content
        print "$1\n";
    }
}

