/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    let count = 0;
    return function() {
        if (count == 0){
            count += 1;
            return n;
        } else {
            count += 1;
            return n += 1;
        }
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */