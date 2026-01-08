const { Calculator } = require("./Calculator");
const calciObj = new Calculator(5);

let result = calciObj.add(10).subtract(3).multiply(3).division(8);

console.log(calciObj.getResult());

// Working with Promises

function fetchData() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            const success = false;

            if (success) {
                resolve("Data fetched successfully");
            } else {
                reject("Data fetch failed");
            }
        }, 2000);
    });
}

fetchData()
    .then((message) => {
        console.log(message);
    })
    .catch((err) => {
        console.log(err);
    });
