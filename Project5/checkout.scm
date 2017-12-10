;;;; This is a checkout function. This takes two values to calculate a total
;;;; sum of money to pay with tax.

;;This is the function that does the math and calculations
(define (checkOut value subtotal)
	(cond
		(
			(< value 0)
			(display "Final Value: ")
			(display (+ subtotal (* subtotal .065)))#t
		)
		(else 
			(display "Enter Value: ")
			(let ((x (read)))(checkout x (+ value subtotal)))
		)
	)
)
;; This is a start function that begins the program
(define (start)
	(display "Welcome to this checkout function")
	(newline)
	(display "Enter a starting amount: (-1 to close)")
	(let ((x (read)))(checkout x 0))
)

