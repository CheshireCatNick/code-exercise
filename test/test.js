function add(val, arr = []) {
    arr.push(val);
    return arr;
}

list1 = add(10)
list2 = add(123, [])
list3 = add('a')

console.log(list1)
console.log(list2)
console.log(list3)

