#!/usr/bin/perl -w

use strict;
use Curses::UI;
my $cui = new Curses::UI( -color_support => 1 );

my @menu = (
          { -label => 'File', 
            -submenu => [
           { -label => 'Exit      ^Q', -value => \&exit_dialog  }
                        ]
           },
        );

sub exit_dialog()
        {
                my $return = $cui->dialog(
                        -message   => "Do you really want to quit?",
                        -title     => "Are you sure???", 
                        -buttons   => ['yes', 'no'],

                );

        exit(0) if $return;
        }

my $menu = $cui->add(
                'menu','Menubar', 
                -menu => \@menu,
                -fg  => "blue",
        );

$cui->set_binding(sub {$menu->focus()}, "\cX");
$cui->set_binding( \&exit_dialog , "\cQ");

$cui->mainloop();
