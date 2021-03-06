(define (make-absolute a)
  (if (< a 0)
      (- 0 a)
      a))
(define (stream-limit s diff)
  (let ((a (stream-car s))
	(b (stream-car (stream-cdr s))))
    (if (< (make-absolute (- a b)) diff)
	b
	(stream-limit (stream-cdr s) diff))))
