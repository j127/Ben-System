<?php

// PLACE YOUR SYSTEM INTO THESE ARRAYS AND THE SCRIPT DOES THE REST
// YOU'LL PROBABLY JUST NEED TO MODIFY THE LETTERS AND THE ORDER OF SUITS
$first_letters = array('s','t','n','m','r','l','g/j','k','f/th','b','p','h','sk/sn/sm','st/sp','sh/sl/sw','d',NULL,NULL,NULL);
$middle_letters = array('oo','a','e','i','o','u','A','E','I','O',NULL,NULL,NULL,NULL,NULL,NULL,'ow','or','ar');
$final_letters = array('s','t','n','m','r','l','g','k','f/th','b',NULL,NULL,NULL,NULL,NULL,NULL,'j/sh/ch','p','d');
$decimals = array(0,1,2,3,4,5,6,7,8,9,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
$binaries = array(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,NULL,NULL,NULL);
$suits = array('ss','cd','ch','cs','dc','dh','ds','cc','hc','hd','hs','hh','sc','sd','sh','dd',NULL,NULL,NULL);
$cards = array("10","A","2","3","4","5","6","7","8","9",NULL,NULL,NULL,NULL,NULL,NULL,"J","Q","K");

//counter
$counter = 0;
$decimal_counter = 0;
$binary_counter = 0;
$card_counter = 0;

for ($row1 = 0; $row1 < 19; $row1++) {

    for ($row2 = 0; $row2 < 19; $row2++) {
        for ($row3 = 0; $row3 < 19; $row3++) {

            //construct the binary number as $bin
            if(($row3 < 8) && ($row1 < 16) && ($row2 < 8)) {
                $bin1 = decbin($binaries[$row1]);
                $bin1 = str_pad($bin1,4,"0",STR_PAD_LEFT);
                $bin2 = decbin($binaries[$row2]);
                $bin2 = str_pad($bin2,3,"0",STR_PAD_LEFT);
                $bin3 = decbin($binaries[$row3]);
                $bin3 = str_pad($bin3,3,"0",STR_PAD_LEFT);
                $bins = "$bin1 $bin2 $bin3";
            } else {
                $bins = NULL;
            }

            //construct the decimals as $dec
            if($row3 < 10) {
                $dec = $decimals[$row1] . $decimals[$row2] . $decimals[$row3];
            } else {
                $dec = NULL;
            }

            //construct letters as $let
            if($row3 < 19) { // this probably isn't needed, but was left over from before and I don't want to break anything
                $let = "$first_letters[$row1], $middle_letters[$row2], $final_letters[$row3]";
            } else {
                $let = NULL;
            }

            //construct cards as $car
            //get the correct suit pair
            $card_suits = $suits[$row1];
            //split suit pair in half
            $card_suit = str_split($card_suits);

            //put each suit in a string
            $card_suit1 = $card_suit[0];
            $card_suit2 = $card_suit[1];

            //turn suit codes into colored suit symbols
            switch ($card_suit1) {
                case 's':
                    $suit_code1 = '♠';
                break;
                case 'h':
                    $suit_code1 = '♥';
                break;
                case 'd':
                    $suit_code1 = '♦';
                break;
                case 'c':
                    $suit_code1 = '♣';
                break;
            }
            switch ($card_suit2) {
                case 's':
                    $suit_code2 = '♠';
                break;
                case 'h':
                    $suit_code2 = '♥';
                break;
                case 'd':
                    $suit_code2 = '♦';
                break;
                case 'c':
                    $suit_code2 = '♣';
                break;
            }
            //assemble pairs
            $card1 = $cards[$row2].$suit_code1;
            $card2 = $cards[$row3].$suit_code2;

            // Duplicates are not removed here.
            $car = "$card1 $card2";

            //check if anything should be removed
            if (strlen($dec) == 3) {
                $dec_check = 1;
            } else {
                $dec_check = 0;
            }
            if (strlen($bins) == 12) {
                $bin_check = 1;
            } else {
                $bin_check = 0;
            }

            //card check to make sure there is something worth printing
            if(($cards[$row2] != "") && ($cards[$row3] != "") && ($suits[$row1] != "") && ($car != NULL)) {
                $card_check = 1;
            } else {
                $card_check = 0;
            }

            // if there is something there, print to browser
            if(($dec_check == 1) || ($bin_check == 1) || ($card_check == 1)) {
                $counter ++;

                //echo "<tr>\n";

                //add a counter column if you want
                //echo "<td style=\"color:#eee;\" class=\"a\">$counter</td>";

                //echo "\t<td class=\"b\">";
                if ($dec_check == 1) {
                    echo "$dec";
                    $decimal_counter++;
                }
                echo "\t";

                //echo "\t<td class=\"c\">";
                if ($bin_check == 1) {
                    echo "$bins";
                    $binary_counter++;
                }
                echo "\t";

                //echo "\t<td class=\"d\">";
                if ($card_check == 1) {
                    echo "$car"; // read the suit pair with $suits[$row1]
                    $card_counter++;
                }
                echo "\t";

                echo "$let\n";

                //echo "</tr>\n";
            }
        }
    }
}

?>
