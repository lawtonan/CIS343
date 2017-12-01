(define (fact num)
(cond 
	((<= num 1) num)
	(else(* num (fact (- num 1))))))
