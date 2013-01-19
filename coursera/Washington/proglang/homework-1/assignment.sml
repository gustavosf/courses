(* ex 1 *)
fun is_older (d1 : int*int*int, d2 : int*int*int) =
	(#1 d1) * 356 + (#2 d1) * 30 + (#3 d1) < (#1 d2) * 356 + (#2 d2) * 30 + (#3 d2)

(* ex 2 *)
fun number_in_month (dates : (int*int*int) list, month : int) =
	if null dates
	then 0
	else number_in_month(tl dates, month) + (if (#2 (hd dates)) = month then 1 else 0)

(* ex 3 *)
fun number_in_months (dates : (int*int*int) list, months : int list) =
	if null months
	then 0
	else number_in_month(dates, hd months) + number_in_months(dates, tl months)

(* ex 4 *)
fun dates_in_month (dates: (int*int*int) list, month : int) =
	if null dates
	then []
	else if (#2 (hd dates)) = month
	then (hd dates)::dates_in_month(tl dates, month)
	else dates_in_month(tl dates, month)

(* ex 5 *)
fun dates_in_months (dates : (int*int*int) list, months : int list) =
	if null months
	then []
	else dates_in_month(dates, hd months) @ dates_in_months(dates, tl months)

(* ex 6 *)
fun get_nth (words : string list, n : int) =
	if n = 1
	then hd words
	else if null (tl words)
	then ""
	else get_nth(tl words, n-1)

(* ex 7 *)
fun date_to_string (date : int*int*int) =
	let
		val months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
	in 
		get_nth(months, #2 date) ^ " " ^ Int.toString(#3 date) ^ ", " ^ Int.toString(#1 date)
	end

(* ex 8 *)
fun number_before_reaching_sum (sum : int, numbers : int list) =
	if sum <= 0
	then ~1
	else 1 + number_before_reaching_sum(sum - (hd numbers), tl numbers)

(* ex 9 *)
fun what_month (day : int) =
	let
		val days = [31,28,31,30,31,30,31,31,30,31,30,31]
	in
		1 + number_before_reaching_sum(day, days)
	end

(* ex 10 *)
fun month_range (day1 : int, day2 : int) =
	List.tabulate(day2 - day1 + 1, fn x => what_month(day1+x))

(* ex 11 *)
fun oldest (dates : (int*int*int) list) =
	if null dates
	then NONE
	else
		let val tl_oldest = oldest(tl dates)
		in if isSome tl_oldest andalso is_older(valOf tl_oldest, hd dates)
		   then tl_oldest
		   else SOME (hd dates)
		end

(* ex 12 *)
fun number_in_months_challenge (dates : (int*int*int) list, months : int list) =
	let fun delete A nil = nil 
	      | delete A (B::R) = if (A=B) then (delete A R) else (B::(delete A R));
		fun remDup nil = nil
	      | remDup (A::R) = (A::(remDup (delete A R)));
	in
		number_in_months(dates, remDup(months))
	end

(* ex 13 *)
fun reasonable_date (date : int * int * int) =
	let val month_days = [31,29,31,30,31,30,31,31,30,31,30,31]
		fun get_nth (days : int list, n : int) =
			if n = 1
			then hd days
			else if null (tl days)
			then 0
			else get_nth(tl days, n-1)
	in
		if (#1 date) < 1 then false
		else if (#2 date) < 1 orelse (#2 date) > 12 then false
		else if (#3 date) < 0 orelse (#3 date) > get_nth(month_days, #2 date) then false
		else if (#2 date) = 2 andalso (#3 date) = 29 andalso not (((#1 date) mod 400) = 0 orelse (((#1 date) mod 100) <> 0 andalso ((#1 date) mod 4) = 0)) then false
		else true
	end