/**
 * @param {number} n
 * @param {number} discount
 * @param {number[]} products
 * @param {number[]} prices
 */
var Cashier = function(n, discount, products, prices) {
    this.n = n;
    this.discount = discount;
    // id => price
    this.toCost = {};
    for (let i = 0; i < products.length; i++) {
        this.toCost[products[i]] = prices[i];
    }
    this.prices = prices;
    this.customerCount = 0;
};

/** 
 * @param {number[]} product 
 * @param {number[]} amount
 * @return {number}
 */
Cashier.prototype.getBill = function(product, amount) {
    let total = 0;
    for (let i = 0; i < product.length; i++) {
        total += this.toCost[product[i]] * amount[i];
    }
    this.customerCount++;
    if (this.customerCount === this.n) {
        // discount
        total -= (this.discount * total) / 100;
        this.customerCount = 0;
    }
    return total;
};

 var obj = new Cashier(3,50,[1,2,3,4,5,6,7],[100,200,300,400,300,200,100]);
 console.log(obj.getBill([1,2],[1,2]));
 console.log(obj.getBill([3, 7],[10,10]));
 console.log(obj.getBill([1,2,3,4,5,6,7],[1,1,1,1,1,1,1]));
 console.log(obj.getBill([4],[10]));
 console.log(obj.getBill([7,3],[10,10]));
 console.log(obj.getBill([7,5,3,1,6,4,2],[10,10,10,9,9,9,7]));
 console.log(obj.getBill([2,3,5],[5,3,2]));
