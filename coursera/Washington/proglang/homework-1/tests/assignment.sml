(* tests for ex 1 *)
is_older((1970, 1, 1), (2012, 5, 7)) = true;
is_older((2012, 5, 7), (1970, 1, 1)) = false;
is_older((2012, 5, 7), (2012, 5, 7)) = false;

(* tests for ex 2 *)
val dates = [(2012, 4, 10), (2012, 5, 15), (2012, 2, 4), (2012, 2, 5)];
number_in_month(dates, 2) = 2;
number_in_month(dates, 4) = 1;
number_in_month(dates, 6) = 0;

(* tests for ex 3 *)
number_in_months(dates, [2,4]) = 3;
number_in_months(dates, [4,6]) = 1;
number_in_months(dates, [7,8]) = 0;

(* tests for ex 4 *)
dates_in_month(dates, 2) = [(2012, 2, 4), (2012, 2, 5)];
dates_in_month(dates, 4) = [(2012, 4, 10)];
dates_in_month(dates, 7) = [];

(* tests for ex 5 *)
dates_in_months(dates, [2,4]) = [(2012, 2, 4), (2012, 2, 5), (2012, 4, 10)];
dates_in_months(dates, [4,6]) = [(2012, 4, 10)];
dates_in_months(dates, [7,8]) = [];

(* tests for ex 6 *)
val fruits = ["apple", "banana", "orange", "watermelon"];
get_nth(fruits, 1) = "apple";
get_nth(fruits, 3) = "orange";
get_nth(fruits, 8) = "";

(* tests for ex 7 *)
date_to_string((2012, 2, 15)) = "February 15, 2012";
date_to_string((2013, 1, 20)) = "January 20, 2013";

(* tests for ex 8 *)
number_before_reaching_sum(4, [1,2,3,4,5,6,7,8,9,10,11,12]) = 2;
number_before_reaching_sum(10, [1,2,3,4,5,6,7,8,9,10,11,12]) = 3;
number_before_reaching_sum(30, [1,2,3,4,5,6,7,8,9,10,11,12]) = 7;
number_before_reaching_sum(1, [1,2,3,4,5,6,7,8,9,10,11,12]) = 0;

(* tests for ex 9 *)
what_month(15) = 1;
what_month(300) = 10;
what_month(59) = 2;
what_month(213) = 8;

(* tests for ex 10 *)
month_range(15, 16) = [1,1];
month_range(31, 32) = [1,2];
month_range(32, 31) = [];
month_range(5, 3) = [];

(* tests for ex 11 *)
oldest(dates) = SOME (2012, 2, 4);

(* tests for ex 12 *)
number_in_months_challenge(dates, [2,2,4]) = 3;
number_in_months_challenge(dates, [4,6,4]) = 1;
number_in_months_challenge(dates, [7,8]) = 0;

(* tests for ex 13 *)
reasonable_date((2013, 1, 19)) = true;
reasonable_date((2013, 15, 25)) = false;
reasonable_date((2013, 11, 31)) = false;
reasonable_date((0, 1, 1)) = false;
reasonable_date((~7, 1, 1)) = false;
reasonable_date((2013, 2, 29)) = false;
reasonable_date((2012, 2, 29)) = true;