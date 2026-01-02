function getArray() {
    let arr = [];
    for (let i = 0; i < 11; i++) {
        arr.push(Math.floor(Math.random(100) * 100));
    }
    return arr;
}

function getSmallest(arr) {
    let smallest = arr[0];
    for (let i = 1; i < arr.length; i++) {
        if (arr[i] < smallest) {
            smallest = arr[i];
        }
    }
    return smallest;
}

function getLargest(arr) {
    let largest = arr[0];
    for (let i = 1; i < arr.length; i++) {
        if (arr[i] > largest) {
            largest = arr[i];
        }
    }
    return largest;
}

function getAvarage(arr) {
    sum = 0;
    for (let i = 0; i < arr.length; i++) {
        sum += arr[i];
    }
    return Math.floor(sum / arr.length);
}

arr = getArray();
console.log(getSmallest(arr));
console.log(getLargest(arr));
console.log(getAvarage(arr));
